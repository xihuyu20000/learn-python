<script setup>
const echarts = inject("echarts");
const option = ref({});

const startTimeData = [
  "2021-01-01",
  "2021-01-31",
  "2021-02-25",
  "2021-03-25",
  "2021-04-01",
  "2021-04-10",
  "2021-05-25",
].map((item) => item);
const endTimeData = [
  "2021-01-01",
  "2021-01-31",
  "2021-02-25",
  "2021-04-01",
  "2021-04-10",
  "2021-05-25",
  "2021-07-25",
].map((item) => item);

onMounted(async () => {
  option.value = {
    // 鼠标移入提示工具
    tooltip: {
      trigger: "axis",
      formatter(params) {
        if (params[1].data && params[0].data) {
          return (
            `<div>开始时间：${params[1].data}</div>` +
            `<div>结束时间：${params[0].data}</div>`
          );
          // 去除时分秒
          return (
            `<div>开始时间：${params[1].data.split(" ")[0]}</div>` +
            `<div>结束时间：${params[0].data.split(" ")[0]}</div>`
          );
        } else {
          return "";
        }
      },
      axisPointer: {
        type: "shadow",
      },
    },
    grid: {
      containLabel: true,
      show: false,
      right: 80,
      left: 40,
      bottom: 40,
      top: 20,
      backgroundColor: "#fff",
    },
    legend: {
      // 图例组件
      data: ["持续时间"],
      align: "auto",
      top: "bottom",
    },
    xAxis: {
      type: "time",
      position: "top", // x 轴位置
      axisTick: {
        // 隐藏刻度
        show: false,
      },
      axisLine: {
        // 隐藏轴线
        show: false,
      },
      splitLine: {
        // 显示网格线
        show: true,
      },
    },
    yAxis: {
      inverse: true, // y 轴数据翻转，该操作是为了保证项目一放在最上面，项目七在最下面
      axisTick: {
        // 隐藏刻度
        show: false,
      },
      axisLine: {
        // 隐藏轴线
        show: false,
      },
      data: [
        "关键词一",
        "关键词二",
        "关键词三",
        "关键词四",
        "关键词五",
        "关键词六",
        "关键词七",
      ],
    },
    color: ["red", "orange", "yellow", "green", "blue", "indigo", "purple"], // 自定义调色盘的颜色
    series: [
      {
        name: "持续时间",
        type: "bar",
        stack: "duration",
        colorBy: "data", // 让数据项 data 每一项的颜色根据调色盘中的颜色按顺序进行分配
        itemStyle: {
          // color: "#007acc",
          borderColor: "#fff",
          borderWidth: 1,
        },
        zlevel: -1,
        data: [
          "2021-01-31",
          "2021-02-25",
          "2021-03-25",
          "2021-04-01",
          "2021-04-10",
          "2021-05-25",
          "2021-07-25",
        ], // 结束时间
        data: endTimeData, // 结束时间 // 结束时间
      },
      {
        name: "持续时间",
        type: "bar",
        stack: "duration", // 堆叠标识符，同个类目轴上系列配置相同的 stack 值可以堆叠放置
        itemStyle: {
          color: "#fff",
        },
        zlevel: -1, // zlevel 大的 Canvas 会放在 zlevel 小的 Canvas 的上面
        z: 9, // z值小的图形会被z值大的图形覆盖，z相比zlevel优先级更低，而且不会创建新的 Canvas
        data: [
          "2021-01-01",
          "2021-01-31",
          "2021-02-25",
          "2021-03-25",
          "2021-04-01",
          "2021-04-10",
          "2021-05-25",
        ], // 开始时间
        data: startTimeData, // 开始时间
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
}
</style>

