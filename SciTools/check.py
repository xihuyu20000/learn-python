"""
代码检查
"""
import _ast
import ast

from core.log import logger


def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    typeset = set()
    for node in ast.walk(tree):
        # logger.debug(node)

        if isinstance(node, _ast.Import):
            logger.debug('直接导入 {}', [n for n in node.names])
            typeset.add(type(node))
        if isinstance(node, _ast.ImportFrom):
            logger.debug('from导入 {} {} {}', node.module, [n for n in node.names], node.level)
            typeset.add(type(node))
        # if isinstance(node, _ast.Module):
        #     logger.debug(dir(node))
        # if isinstance(node, ast.FunctionDef):
        #     print(f"Function: {node.name}")
        #
        # if isinstance(node, ast.ClassDef):
        #     print(f"'{node.name}'")
    print(typeset)


analyze_file('core/runner/mrunner.py')
