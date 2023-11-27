import os

from flask import Flask, request
from werkzeug.utils import secure_filename

import settings
from core.do_data import FreqStat, CoStat
from core.parse_data import cnki_refworks
from server import acc_sum
from cfg import PathInfo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'




def __list_datafiles():
    dir = PathInfo.get('data_dir')
    return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
@app.get('/api/list_datafiles')
def list_datafiles():
    return __list_datafiles()
@app.get('/api/get_config_datadir')
def get_config_datadir():
    return PathInfo.get('data_dir')

@app.post('/api/combine_datafiles')
def combine_datafiles():
    data = request.get_json(silent=True)

    files = [fname for i, fname in enumerate(__list_datafiles()) if i in data['ids']]

    dir = PathInfo.get('data_dir')
    with open(os.path.join(dir, data['newfilename']), 'w', encoding='utf-8') as writer:
        for f in files:
            with open(os.path.join(dir, f), encoding='utf-8') as reader:
                writer.writelines(reader.readlines())
                writer.write('\r\n')

    return "ok"

@app.post('/api/save_config')
def save_config():
    data = request.get_json(silent=True)
    PathInfo.update('data_dir', data['data_dir'])
    return 'ok'
@app.post('/api/upload')
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('d:/', filename))
    return '上传成功'

@app.get('/api/detail_table/<style>/<index>')
def detail_table(style, index):
    print('需要解析的文件类型', style)
    path = __list_datafiles()
    path = path[int(index)]

    path = os.path.join(PathInfo.get('data_dir'), path)
    # columnNames = ('doctype', 'authors', 'orgs', 'title', 'source', 'pubyear', 'kws', 'abs')
    data = cnki_refworks.parse_file(path)
    data = [m.to_dict() for m in data]
    return data


@app.route("/api/freq_yearly", methods=["GET"])
def freq_yearly():
    """
    历年发文量
    """
    data = cnki_refworks.parse_file(filename)
    freqStat = FreqStat(data)
    result = freqStat.freq_yearly()

    yearly = [t[0] for t in result]
    count = [t[1] for t in result]

    option = {'title': '历年发文量', 'x': yearly, 'y': [
        {
            'data': count,
            'type': "line",
        },
    ]}
    return option


@app.route("/api/acc_freq_yearly", methods=["GET"])
def acc_freq_yearly():
    """
    累计历年发文量
    """
    data = cnki_refworks.parse_file(filename)
    freqStat = FreqStat(data)
    result = freqStat.freq_yearly()

    yearly = [t[0] for t in result]
    count = [t[1] for t in result]
    count = acc_sum(count)

    option = {'title': '累计历年发文量', 'x': yearly, 'y': [
        {
            'data': count,
            'type': "line",
        },
    ]}
    return option


@app.route("/api/acc_freq_yearly2", methods=["GET"])
def acc_freq_yearly2():
    """
    历年发文量、累计历年发文量的 混合图
    """
    data = cnki_refworks.parse_file(filename)
    freqStat = FreqStat(data)
    result = freqStat.freq_yearly()

    yearly = [t[0] for t in result]
    count1 = [t[1] for t in result]
    count2 = acc_sum(count1)

    option = {'title': '混合历年发文量', 'x': yearly, 'y': [
        {
            'name': '历年发文',
            'data': count1,
            'type': "line",
        },
        {
            'name': '累计历年',
            'data': count2,
            'type': "line",
        },
    ]}
    return option


@app.route("/api/freq_authors", methods=["GET"])
def freq_authors():
    """
    历年发文量
    """
    data = cnki_refworks.parse_file(filename)
    freqStat = FreqStat(data)
    result = freqStat.freq_authors()
    data = [{'name': k, 'value': v} for k, v in result.items()]
    option = {'title': '作者发文量', 'y': data}
    return option


@app.route('/api/co_kws', methods=['GET'])
def co_kws():
    data = cnki_refworks.parse_file(filename)
    coStat = CoStat(data)
    coKws, weights = coStat.co_kws()

    nodes = []
    for name, weiht in weights.items():
        if name != '文献计量':
            nodes.append({'name': name, 'draggable': True, 'symbolSize': [weiht, weiht]})
    links = []
    for item in coKws:
        if item[0] != '文献计量' and item[1] != '文献计量' and item[2] > 2:
            links.append({
                'target': item[0],
                'source': item[1],
                'lineStyle': {
                    'normal': {
                        'width': item[2],
                        'curveness': 0.2,
                        'color': "#FF00FF"
                    }
                }
            })

    option = {
        "nodes": nodes,
        "links": links,
        "categories": []
    }

    return option


if __name__ == '__main__':
    app.run(port=settings.WEB_SERVER_PORT, debug=True)
