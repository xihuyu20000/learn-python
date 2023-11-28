from typing import Dict, Any

import json

init_cfg = {'datafiles_dir' : r"D:\阿里云盘\大数据etl培训\07_项目电商用户行为分析"}


class Cfg:
    FILE_NAME: str = 'cfg.json'

    @staticmethod
    def init(content = init_cfg):
        content = json.dumps(init_cfg, ensure_ascii=False, indent=2)
        with open(Cfg.FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def load():
        return json.load(open(Cfg.FILE_NAME, 'r', encoding='utf-8'))

    @staticmethod
    def write(content):
        content = json.dumps(content, ensure_ascii=False, indent=2)
        with open(Cfg.FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(content)
            f.flush()

    @staticmethod
    def get(k):
        config = Cfg.load()
        return config[k]
    @staticmethod
    def set(k, v):
        config = Cfg.load()
        config[k] = v
        Cfg.write(config)




if __name__ == '__main__':
    cfg = Cfg.load()


