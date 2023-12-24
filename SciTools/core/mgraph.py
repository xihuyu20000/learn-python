"""
参考文档  https://pyecharts.org/#/zh-cn/quickstart
"""
import collections
import os
from typing import List

import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Pie, WordCloud, Graph, Sankey
from pyecharts.globals import SymbolType

from core.const import abs_path


class GraphData:
    def __init__(self):
        self._canvas_width = '900px'
        self._canvas_height = '600px'
        self._canvas_bg_color = None
        self._chart_style = ''
        self._xaxis: List = []
        self._series_name = ''
        self._yaxis = []

    @property
    def canvas_width(self) -> str:
        return self._canvas_width

    @canvas_width.setter
    def canvas_width(self, value: int):
        assert isinstance(value, int)
        self._canvas_width = f'{value}px'

    @property
    def canvas_height(self) -> str:
        return self._canvas_height

    @canvas_height.setter
    def canvas_height(self, value: int):
        assert isinstance(value, int)
        self._canvas_height = f'{value}px'

    @property
    def canvas_bg_color(self) -> str:
        return self._canvas_bg_color

    @canvas_bg_color.setter
    def canvas_bg_color(self, value: str):
        self._canvas_bg_color = value

    @property
    def chart_style(self):
        return self._chart_style

    @chart_style.setter
    def chart_style(self, value: str):
        self._chart_style = value

    @property
    def xaxis(self) -> List:
        return self._xaxis

    @xaxis.setter
    def xaxis(self, value: List):
        self._xaxis = value

    @property
    def series_name(self) -> str:
        return self._series_name

    @series_name.setter
    def series_name(self, value: str):
        self._series_name = value

    @property
    def yaxis(self) -> List:
        return self._yaxis

    @yaxis.setter
    def yaxis(self, value: List):
        self._yaxis = value

    def __repr__(self):
        return f'\r\n{self.canvas_width=}\r\n{self.canvas_height=}\r\n{self.chart_style=}\r\n{self.xaxis=}\r\n{self.series_name=}\r\n{self.yaxis=}'


DrawInfo = collections.namedtuple('DrawInfo', ['style', 'label', 'func'])


class Draw:
    infos = [
        DrawInfo(style='line', label='折线图', func='_draw_line'),
        DrawInfo(style='bar', label='柱状图', func='_draw_bar'),
        DrawInfo(style='pie', label='饼图', func='_draw_pie'),
        DrawInfo(style='circle', label='环形图', func='_draw_circle'),
        DrawInfo(style='rose', label='玫瑰图', func='_draw_rose'),
        DrawInfo(style='wordcloud', label='词云图', func='_draw_wordcloud'),
        DrawInfo(style='graph_base', label='关系图', func='_draw_graph_base'),
        DrawInfo(style='sankey', label='桑吉图', func='_draw_sankey')
    ]

    def draw(self, data: GraphData):
        assert isinstance(data, GraphData)

        if len(data.chart_style.strip()) == 0:
            raise Exception('请选择图表类型')

        # 初始化选项
        self.init_opts = opts.InitOpts(
            width=data.canvas_width,
            height=data.canvas_height,
            renderer='svg',
            bg_color=data.canvas_bg_color,
            page_title='',
            theme = "white",
        )
        self.render_opts = opts.RenderOpts(True)
        self.title_opts = opts.TitleOpts(title="我是标题")
        self.toolbox_opts = opts.ToolboxOpts(
            is_show=True,
            feature=opts.ToolBoxFeatureOpts(
                save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                    type_='png',
                    name="图片",
                    background_color='#FFFFFF',
                    is_show=True,
                    title="保存为图片",
                ),
                restore=opts.ToolBoxFeatureRestoreOpts(
                    is_show=False
                ),
                data_view=opts.ToolBoxFeatureDataViewOpts(
                    is_show=False
                ),
                data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                    is_show=False
                ),
                brush=opts.ToolBoxFeatureBrushOpts(
                    type_="clear"
                )
            )
        )

        self.legend_opts = opts.LegendOpts(
            type_='plain',
            selected_mode=True,
            is_show=True,
            pos_left=None,
            pos_right=None,
            pos_top=None,
            pos_bottom=None,
            orient='horizontal',
            align='auto',
            padding=5,
            item_gap=10,
            item_width=25,
            item_height=14,
            inactive_color='#ccc',
            textstyle_opts=None,
            legend_icon=None
        )
        for info in Draw.infos:
            if info.label == data.chart_style:
                func = getattr(self, info.func)
                g = func(self.init_opts, self.render_opts, data)
                g.set_global_opts(title_opts=self.title_opts,
                                  legend_opts=self.legend_opts,
                                  toolbox_opts=self.toolbox_opts)
                result = g.render(os.path.join(abs_path, '../chart.html'))
                return result

        raise Exception('不识别的图表类型' + info.label)

    def _draw_line(self, init_opts, render_opts, data: GraphData):
        g = Line(init_opts=init_opts, render_opts=render_opts)
        g.add_xaxis(data.xaxis)
        g.add_yaxis(data.series_name, data.yaxis)

        return g

    def _draw_bar(self, init_opts, render_opts, data: GraphData):
        g = Bar(init_opts=init_opts, render_opts=render_opts)
        g.add_xaxis(data.xaxis)
        g.add_yaxis(data.series_name, data.yaxis)

        return g

    def _draw_pie(self, init_opts, render_opts, data: GraphData):
        g = Pie(init_opts=init_opts, render_opts=render_opts)
        g.add(series_name=data.series_name, data_pair=[(j, i) for i, j in zip(data.yaxis, data.xaxis)])

        return g

    def _draw_circle(self, init_opts, render_opts, data: GraphData):
        g = Pie(init_opts=init_opts, render_opts=render_opts)
        g.add(series_name=data.series_name, radius=['40%', '75%'],
              data_pair=[(j, i) for i, j in zip(data.yaxis, data.xaxis)])

        return g

    def _draw_rose(self, init_opts, render_opts, data: GraphData):
        g = Pie(init_opts=init_opts, render_opts=render_opts)
        g.add(series_name=data.series_name, rosetype='radius',
              data_pair=[(j, i) for i, j in zip(data.yaxis, data.xaxis)])

        return g

    def _draw_wordcloud(self, init_opts, render_opts, data: GraphData):
        g = WordCloud(init_opts=init_opts, render_opts=render_opts)
        g.add(series_name=data.series_name, word_size_range=[20, 100], shape=SymbolType.DIAMOND,
              data_pair=[(j, i) for i, j in zip(data.yaxis, data.xaxis)])

        return g

    def _draw_graph_base(self, init_opts, render_opts, data: GraphData):
        g = Graph(init_opts=init_opts, render_opts=render_opts)

        nodes = []

        for val, cat in zip(data.yaxis, data.xaxis):
            nodes.append({"name": cat, "symbolSize": val})

        links = []
        for i in nodes:
            for j in nodes:
                links.append({"source": i.get("name"), "target": j.get("name")})

        g.add("", nodes, links, repulsion=8000)

        return g

    def _draw_sankey(self, init_opts, render_opts, data: GraphData):

        nodes = [
            {'name': '电气类'}
            , {'name': '电子信息类'}
            , {'name': '核工程类'}
            , {'name': '管理科学与工程类'}
            , {'name': '工商管理类'}
            , {'name': '经济学类'}
            , {'name': '水利类'}
            , {'name': '北京'}
            , {'name': '天津'}
            , {'name': '河北'}
            , {'name': '山西'}
            , {'name': '内蒙古'}
        ]
        links = [
            {'source': '北京', 'target': '电气类', 'value': 20}
            , {'source': '北京', 'target': '电子信息类', 'value': 13}
            , {'source': '北京', 'target': '核工程类', 'value': 6}
            , {'source': '北京', 'target': '管理科学与工程类', 'value': 8}
            , {'source': '北京', 'target': '工商管理类', 'value': 16}
            , {'source': '北京', 'target': '经济学类', 'value': 6}
            , {'source': '北京', 'target': '水利类', 'value': 2}

            , {'source': '天津', 'target': '电气类', 'value': 11}
            , {'source': '天津', 'target': '电子信息类', 'value': 4}
            , {'source': '天津', 'target': '核工程类', 'value': 1}
            , {'source': '天津', 'target': '管理科学与工程类', 'value': 2}
            , {'source': '天津', 'target': '工商管理类', 'value': 6}
            , {'source': '天津', 'target': '经济学类', 'value': 2}
            , {'source': '天津', 'target': '水利类', 'value': 2}

            , {'source': '河北', 'target': '电气类', 'value': 15}
            , {'source': '河北', 'target': '电子信息类', 'value': 6}
            , {'source': '河北', 'target': '核工程类', 'value': 5}
            , {'source': '河北', 'target': '管理科学与工程类', 'value': 4}
            , {'source': '河北', 'target': '工商管理类', 'value': 8}
            , {'source': '河北', 'target': '经济学类', 'value': 2}
            , {'source': '河北', 'target': '水利类', 'value': 2}

            , {'source': '山西', 'target': '电气类', 'value': 15}
            , {'source': '山西', 'target': '电子信息类', 'value': 9}
            , {'source': '山西', 'target': '核工程类', 'value': 5}
            , {'source': '山西', 'target': '管理科学与工程类', 'value': 6}
            , {'source': '山西', 'target': '工商管理类', 'value': 8}
            , {'source': '山西', 'target': '经济学类', 'value': 6}
            , {'source': '山西', 'target': '水利类', 'value': 3}

            , {'source': '内蒙古', 'target': '电气类', 'value': 13}
            , {'source': '内蒙古', 'target': '电子信息类', 'value': 3}
            , {'source': '内蒙古', 'target': '核工程类', 'value': 2}
            , {'source': '内蒙古', 'target': '管理科学与工程类', 'value': 2}
            , {'source': '内蒙古', 'target': '工商管理类', 'value': 4}
            , {'source': '内蒙古', 'target': '经济学类', 'value': 2}
            , {'source': '内蒙古', 'target': '水利类', 'value': 2}
        ]

        g = Sankey(init_opts=init_opts, render_opts=render_opts)

        g.add(

            series_name='测试中'
            , nodes=nodes
            , links=links
            , linestyle_opt=opts.LineStyleOpts(
                opacity=0.2  ###透明度设置
                , curve=0.5  ###信息流的曲线弯曲度设置
                , color="source"  ##颜色设置，source表示使用节点的颜色
            )  ##线条格式 ,设置所有线条的格式
            , label_opts=opts.LabelOpts(
                font_size=16
                , position='right'
            )  ##标签配置，具体参数详见opts.LabelOpts()
            , levels=[
                opts.SankeyLevelsOpts(
                    depth=0,  ##第一层的配置
                    itemstyle_opts=opts.ItemStyleOpts(color="#fbb4ae"),  ##节点格式的配置
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.2, curve=0.5))
                , opts.SankeyLevelsOpts(
                    depth=1,  ##第二层的配置
                    itemstyle_opts=opts.ItemStyleOpts(color="#b3cde3"),  ##节点格式的配置
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.2, curve=0.5))  ##信息的配置
                , opts.SankeyLevelsOpts(
                    depth=2,  ##第三层的配置
                    itemstyle_opts=opts.ItemStyleOpts(color="#ccebc5"),  ##节点格式的配置
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.2, curve=0.5))  ##信息的配置
            ]  # 桑基图每一层的设置。可以逐层设置
        )

        return g
