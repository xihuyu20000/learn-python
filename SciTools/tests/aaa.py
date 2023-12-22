# from d3blocks import D3Blocks
#
# # 初始化
# d3 = D3Blocks()
#
# # 导入数据集
# df = d3.import_example('energy')
#
# # 打印出前5行数据
# print(df)
#
# # 初始化网络图
# d3.d3graph(df, showfig=False)
#
# # 每个节点打上颜色
# d3.D3graph.set_node_properties(color='cluster')
#
# # 调整每个节点的位置
# d3.D3graph.node_properties['Thermal_generation']['size'] = 20
# d3.D3graph.node_properties['Thermal_generation']['edge_color'] = '#000fff'  # 蓝色的节点
# d3.D3graph.node_properties['Thermal_generation']['edge_size'] = 3  # Node-edge Size
#
# # 调整每个连线的位置
# d3.D3graph.edge_properties['Solar', 'Solar_Thermal']['color'] = '#000fff'
# d3.D3graph.edge_properties['Solar', 'Solar_Thermal']['weight_scaled'] = 10
#
# # 绘制图表
# d3.D3graph.show()

import collections

import pandas as pd

# 假设 df2 是一个包含列表的 DataFrame
# 例如，
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])

# 使用 Counter 对每个元素的频率进行计数
total_pairs = collections.Counter(pair for row in df2.values for pair in row)
print(total_pairs)
