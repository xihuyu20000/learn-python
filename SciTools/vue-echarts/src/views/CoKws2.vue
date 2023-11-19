<script setup>
const echarts = inject("echarts");
const option = ref({});

onMounted(async () => {
  option.value = {
    backgroundColor: "#1a4377",
    animationDurationUpdate: 1500, // 动画更新变化时间
    animationEasingUpdate: "quinticInOut", // 动画缓动效果
    series: [
      {
        type: "graph", // 选择关系图
        layout: "force", // 'none'无部局，需要自己添加坐标,'circular'环形布局,'force'引导布局，出来的效果随机
        force: {
          repulsion: 1000, // 节点间的斥力
          edgeLength: 50, // 两节点间距离，受斥力影响
        },
        roam: true,
        label: {
          // 节点中字的全局样式
          normal: {
            show: true,
            color: "#fff",
          },
        },
        itemStyle: {
          // 节点圆圈的全局样式
          normal: {
            // borderColor: '#fff',
            // borderWidth: 1,
            // shadowBlur: 1,
            // shadowColor: 'rgba(0, 0, 0, 0.3)'
          },
        },
        focusNodeAdjacency: true, // 鼠标悬浮一个节点时突出与它有关系的节点，淡化其它无关系的节点
        data: [
          // 各个节点数据
          {
            id: "a1",
            name: "校园大数据",
            symbolSize: 120, // 决定各个节点大小
            draggable: true, // 可拖拽
            category: 0, // 节点间分类
            itemStyle: {
              // 各圆圈自定义样式
              normal: {
                borderColor: "#b457ff",
                borderWidth: 1,
                shadowBlur: 20,
                shadowColor: "#b457ff",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "red",
                    },
                    {
                      offset: 1,
                      color: "green",
                    },
                  ],
                  global: false,
                },
              },
            },
          },
          {
            id: "2",
            name: "舆情大数据",
            symbolSize: 100,
            itemStyle: {
              normal: {
                borderColor: "#04f2a7",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#04f2a7",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(234, 242, 164, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(4, 242, 4, 1)",
                    },
                  ],
                },
              },
            },
            category: 1,
          },
          {
            id: "3",
            name: "用户分析",
            symbolSize: 80,
            category: 1,
            itemStyle: {
              normal: {
                borderColor: "#04f2a7",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#04f2a7",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(4, 242, 164, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(4, 242, 164, 1)",
                    },
                  ],
                },
              },
            },
          },
          {
            id: "4",
            name: "话题分析",
            symbolSize: 80,
            category: 1,
            itemStyle: {
              normal: {
                borderColor: "#04f2a7",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#04f2a7",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(4, 242, 164, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(4, 242, 164, 1)",
                    },
                  ],
                },
              },
            },
          },
          {
            id: "5",
            name: "评论分析",
            symbolSize: 80,
            category: 1,
            itemStyle: {
              normal: {
                borderColor: "#04f2a7",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#04f2a7",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(4, 242, 164, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(4, 242, 164, 1)",
                    },
                  ],
                },
              },
            },
          },
          {
            id: "6",
            name: "图书馆分析",
            symbolSize: 100,
            category: 2,
            itemStyle: {
              normal: {
                borderColor: "#82dffe",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#82dffe",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(130, 223, 254, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(130, 223, 254, 1)",
                    },
                  ],
                },
              },
            },
          },
          {
            id: "7",
            name: "借阅分析",
            symbolSize: 80,
            category: 2,
            itemStyle: {
              normal: {
                borderColor: "#82dffe",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#82dffe",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(130, 223, 254, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(130, 223, 254, 1)",
                    },
                  ],
                },
              },
            },
          },
          {
            id: "8",
            name: "借阅排行",
            symbolSize: 80,
            itemStyle: {
              normal: {
                borderColor: "#82dffe",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#82dffe",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(130, 223, 254, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(130, 223, 254, 1)",
                    },
                  ],
                },
              },
            },
            category: 2,
          },
          {
            id: "9",
            name: "图书收录",
            symbolSize: 80,
            itemStyle: {
              normal: {
                borderColor: "#82dffe",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#82dffe",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(130, 223, 254, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(130, 223, 254, 1)",
                    },
                  ],
                },
              },
            },
            category: 2,
          },
          {
            id: "10",
            name: "图书分析",
            symbolSize: 80,
            category: 2,
            itemStyle: {
              normal: {
                borderColor: "#82dffe",
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: "#82dffe",
                color: {
                  type: "radial",
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(130, 223, 254, 0.1)",
                    },
                    {
                      offset: 1,
                      color: "rgba(130, 223, 254, 1)",
                    },
                  ],
                },
              },
            },
          },
        ],
        links: [
          // 各个节点间的关系，可传id或name,这里选择的id
          {
            source: "a1",
            target: "2",
          },
          {
            source: "2",
            target: "3",
          },
          {
            source: "2",
            target: "4",
          },
          {
            source: "2",
            target: "5",
          },
          {
            source: "a1",
            target: "6",
          },
          {
            source: "6",
            target: "10",
          },
          {
            source: "6",
            target: "7",
          },
          {
            source: "6",
            target: "8",
          },
          {
            source: "6",
            target: "9",
          },
        ],
        lineStyle: {
          // 连线的样式
          normal: {
            opacity: 0.9,
            width: 1,
            curveness: 0.1, // 线的弯曲程度，0代表直线，数值越大越弯
          },
        },
      },
    ],
  };
});
</script>

<template>
  <base-echart class="echarts" :option="option"></base-echart>
</template>

<style scoped>
.echarts {
  background-color: #e4e4e4;
}
</style>

