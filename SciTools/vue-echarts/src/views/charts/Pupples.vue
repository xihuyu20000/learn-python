<script setup>
const echarts = inject("echarts");
const option = ref({});

const list = [
  {
    name: "内部运价",
    data: [
      { value: 20, symbolSize: 28 },
      { value: 50, symbolSize: 20 },
      { value: 100, symbolSize: 86 },
      { value: 150, symbolSize: 45 },
      { value: 260, symbolSize: 88 },
      { value: 550, symbolSize: 45 },
      { value: 750, symbolSize: 66 },
    ],
  },
  {
    name: "G7易流运价",
    data: [
      { value: 30, symbolSize: 10 },
      { value: 50, symbolSize: 20 },
      { value: 80, symbolSize: 35 },
      { value: 150, symbolSize: 15 },
      { value: 225, symbolSize: 35 },
      { value: 350, symbolSize: 85 },
      { value: 550, symbolSize: 62 },
    ],
  },
];
const color = ["RGB(101,148,249)", "RGB(99,218,171)"];
const seriesList = [];
var i = {};
list.forEach((item, index) => {
  i = {
    name: item.name,
    type: "line",
    smooth: true,
    symbol: "circle", //拐点设置为实心
    animation: true, //false: hover圆点不缩放 .true:hover圆点默认缩放
    lineStyle: {
      normal: {
        width: "2", //折线粗细
      },
    },
    itemStyle: {
      normal: {
        color: color[index], //拐点颜色
      },
    },
    data: item.data,
  };
  seriesList.push(i);
}),
  onMounted(async () => {
    option.value = {
      title: {
        // text: '堆叠区域图'
      },
      legend: {
        data: list.map(function (item) {
          return item.name;
        }),
      },
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "cross",
          label: {
            backgroundColor: "#6a7985",
          },
        },
        formatter(params) {
          var content = "";
          params.forEach((item) => {
            content +=
              item.marker +
              item.seriesName +
              "￥" +
              item.data.value +
              " | " +
              item.data.symbolSize +
              "单" +
              "<br>";
          });
          return (
            '<div style="border-bottom: 1px dotted rgba(237, 72, 69, 0.3); font-size: 16px;padding-bottom: 7px;margin-bottom: 7px">' +
            params[0].name +
            "</div>" +
            content
          );
        },
      },
      toolbox: {
        feature: {
          // saveAsImage: {}
        },
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      xAxis: [
        {
          type: "category",
          name: "日期",
          boundaryGap: false,
          data: ["05-10", "05-11", "05-12", "05-13", "05-14", "05-15", "05-16"],
        },
      ],
      yAxis: [
        {
          type: "value",
          name: "运价(元)",
        },
      ],
      series: seriesList,
    };
  });
</script>

<template>
  <basic-echart class="echarts" :option="option"></basic-echart>
</template>

<style scoped>
.echarts {
}
</style>

