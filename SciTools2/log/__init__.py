import sys

import loguru

format_info = '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> ' \
            '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'

# 格式里面添加了process和thread记录，方便查看多进程和线程程序
format_error = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> ' \
            '| <magenta>{process}</magenta>:<yellow>{thread}</yellow> ' \
            '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'




class MyLogger:
    def __init__(self):
        self.__logger = loguru.logger

        # 清空所有设置
        self.__logger.remove()

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
            sink="clean-info.log",
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
            sink="clean-error.log",
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

logger = MyLogger().get_logger()
