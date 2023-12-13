
import sys

# 获取当前 Python 版本信息
python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(python_version)

import platform
arch_info = platform.architecture()
arch_info = arch_info[0]
print(arch_info)