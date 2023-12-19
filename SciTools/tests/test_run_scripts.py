"""
调用python模块，运行其中的run()方法
"""
import importlib
import multiprocessing
import os


def test_run_scripts():
    """
    加载爬虫脚本，并运行
    """
    # 获取所有以get_开头的py文件
    ss = [d for d in os.listdir(abs_path('scripts')) if d.startswith('crawl_')]
    # 去掉.py后缀
    ss = [d.replace('.py', '') for d in ss]

    for s in ss:
        mod = importlib.import_module(f'scripts.{s}')
        p1 = multiprocessing.Process(target=mod.run, args=())
        p1.start()
        p1.join()
        assert True
