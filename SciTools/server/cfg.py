from configparser import ConfigParser

conf_path = 'cfg.ini'
PATH_INFO = 'path'


class PathInfo:
    @staticmethod
    def init():
        conf = ConfigParser()
        conf['DEFAULT'] = {
            'encoding': 'utf-8'
        }
        conf[PATH_INFO] = {
            'data_dir': ''
        }

        with open(conf_path, 'w', encoding="utf-8") as configfile:
            conf.write(configfile)

    @staticmethod
    def get(key):
        online = ConfigParser()
        online.read(conf_path, encoding="utf-8")
        return online.get(PATH_INFO, key)

    @staticmethod
    def update(name, value):
        conf = ConfigParser()
        conf.read(conf_path, encoding="utf-8")
        conf.set(PATH_INFO, name, value)
        conf.write(open(conf_path, "w", encoding="utf-8"))


if __name__ == "__main__":
    PathInfo.init()
