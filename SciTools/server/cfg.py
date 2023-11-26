from configparser import ConfigParser

conf_path = 'cfg.ini'
PATH_INFO = 'path'

class PathInfo:
    @staticmethod
    def init():
        conf = ConfigParser()
        conf[PATH_INFO] = {
            'data_dir': 'C:\Program Files (x86)\Microsoft Visual Studio\Installer\zh-hant'
        }

        with open(conf_path, 'w') as configfile:
            conf.write(configfile)

    @staticmethod
    def get(key):
        online = ConfigParser()
        online.read(conf_path)
        return online.get(PATH_INFO, key)

    @staticmethod
    def update(name, value):
        conf = ConfigParser()
        conf.read(conf_path)
        conf.set(PATH_INFO, name, value)
        conf.write(open(conf_path, "w"))

if __name__ == "__main__":
    PathInfo.init()