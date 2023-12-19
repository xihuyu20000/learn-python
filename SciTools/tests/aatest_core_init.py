#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo2.py
@Time    :   2020/06/10 19:51:28
@Author  :   Ai Qiangyun 
@Version :   1.0
@Contact :   aqy0716@163.com
@License :   (C)Copyright 2020 SCAU
@Desc    :   None
'''

# here put the import lib

from graphviz import Digraph

#创建表
dot = Digraph(comment='The Test Table')

# 添加圆点A,A的标签是Dot A
dot.node('A', 'Dot A')

# 添加圆点 B, B的标签是Dot B
dot.node('B', 'Dot B')
# dot.view()

# 添加圆点 C, C的标签是Dot C
dot.node('C', 'Dot C')
# dot.view()

# 创建一堆边，即连接AB的两条边，连接AC的一条边。
dot.edges(['AB', 'AC', 'AB'])
# dot.view()

# 在创建两圆点之间创建一条边
dot.edge('B', 'C', 'test')

# dot.view()

#数据类型
print(type(dot))
print(type(dot.source))

# 获取DOT source源码的字符串形式
print(dot.source) 
# // The Test Table
# digraph {
#   A [label="Dot A"]
#   B [label="Dot B"]
#   C [label="Dot C"]
#   A -> B
#   A -> C
#   A -> B
#   B -> C [label=test]
# }


# 保存source到文件，并提供Graphviz引擎
dot.render(directory=r"graphviz-python",filename = "fff4.gv", format = "pdf", view=True)