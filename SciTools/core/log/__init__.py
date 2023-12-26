import os
import sys

import loguru

format_info = '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> ' \
            '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'

# 格式里面添加了process和thread记录，方便查看多进程和线程程序
format_error = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> ' \
            '| <magenta>{process}</magenta>:<yellow>{thread}</yellow> ' \
            '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'

# 使用 getattr 检查 sys.frozen 属性,判断脚本是否运行在一个EXE文件中
_abs_path = os.path.expanduser("~")
class MyLogger:
    def __init__(self):
        self.__logger = loguru.logger

        # 清空所有设置
        self.__logger.remove()

        if not getattr(sys, 'frozen', False):
            # 添加控制台输出的格式,sys.stdout为输出到屏幕;关于这些配置还需要自定义请移步官网查看相关参数说明
            self.__logger.add(sys.stdout,
                            colorize=True,
                            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "  # 颜色>时间
                                   "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                                   ":<cyan>{line}</cyan> | "  # 行号
                                   "<level>{level}</level>: "  # 等级
                                   "<level>{message}</level>",  # 日志内容
                              )

        self.__logger.add(
            sink=os.path.join(_abs_path, ".clean-info.log"),
            enqueue=True,
            rotation="4 weeks",
            retention="4 months",
            encoding="utf-8",
            backtrace=True,
            diagnose=True,
            # compression="zip",
            format=format_info,
            level="INFO",
            filter=lambda record: record["level"].no <= loguru.logger.level("INFO").no
        )

        self.__logger.add(
            sink=os.path.join(_abs_path, ".clean-error.log"),
            enqueue=True,
            encoding="utf-8",
            backtrace=True,
            diagnose=True,
            # compression="zip",
            format=format_error,
            level="ERROR",
            filter=lambda record: record["level"].no >= loguru.logger.level("INFO").no
        )

    def get_logger(self):
        return self.__logger

    # def info(self, *args):
    #     self.__logger.info(' , '.join(args))
    #
    # def error(self, *args):
    #     self.__logger.error(' , '.join(args))

logger = MyLogger().get_logger()

logger.debug('日志文件夹 {}', _abs_path)

