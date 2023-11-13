import os

"""
清除一些缓存内容
"""
for ff in ('.pytest_cache', 'scripts\.pytest_cache', 'tests\.pytest_cache', 'res_html'):
    os.system(f'rd/s/q {ff}')
