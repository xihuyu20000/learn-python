<template><base-echarts :options="options"></base-echarts></template>

<script setup>
import BaseEcharts from "./BaseEcharts.vue";

const data = {
  1981: 1023,
  1996: 1023,
  1997: 1023,
  2000: 2046,
  2001: 3069,
  2002: 2046,
  2003: 3069,
  2004: 7161,
  2005: 8184,
  2006: 4092,
  2007: 15345,
  2008: 11253,
  2009: 16368,
  2010: 27621,
  2011: 27621,
  2012: 24552,
  2013: 34782,
  2014: 33759,
  2015: 37851,
  2016: 47058,
  2017: 39897,
  2018: 55243,
  2019: 186305,
  2020: 178139,
  2021: 159724,
  2022: 64510,
  2023: 467968,
};

const keysArray = [];
const valuesArray = [];

// 遍历对象的所有键值对
for (const [key, value] of Object.entries(data)) {
  keysArray.push(key);
  valuesArray.push(value);
}

const options = {
  title: {
    text: "堆叠区域图",
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "cross",
      label: {
        backgroundColor: "#6a7985",
      },
    },
  },
  legend: {
    data: ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"],
  },
  toolbox: {
    feature: {
      saveAsImage: {},
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
      boundaryGap: false,
      data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
    },
  ],
  yAxis: [
    {
      type: "value",
    },
  ],
  series: [
    {
      name: "搜索引擎",
      type: "line",
      symbol: "circle", //拐点设置为实心
      symbolSize: (value, params) => value / 80, //拐点大小
      stack: "总量",
      animation: true, //false: hover圆点不缩放 .true:hover圆点默认缩放
      lineStyle: {
        normal: {
          color: "red", //折线的颜色
          width: "1", //折线粗细
        },
      },
      itemStyle: {
        normal: {
          color: (seriesIndex, dataIndex, data, value) => "red", //拐点颜色
        },
        emphasis: {
          color: "#000000", //hover拐点颜色定义
        },
      },

      data: [520, 932, 901, 934, 1290, 1330, 1320],
    },
    {
      name: "搜索引擎",
      type: "line",
      symbol: "circle", //拐点设置为实心
      symbolSize: (value, params) => value / 80, //拐点大小
      stack: "总量",
      animation: true, //false: hover圆点不缩放 .true:hover圆点默认缩放
      lineStyle: {
        normal: {
          color: "blue", //折线的颜色
          width: "1", //折线粗细
        },
      },
      itemStyle: {
        normal: {
          color: (seriesIndex, dataIndex, data, value) => "blue", //拐点颜色
        },
        emphasis: {
          color: "#000000", //hover拐点颜色定义
        },
      },

      data: [20, 32, 191, 1934, 290, 330, 320],
    },
  ],
  toolbox: {
    show: true,
    feature: {
      dataZoom: {
        yAxisIndex: "none",
      },
      dataView: { readOnly: false },
      restore: {},
      magicType: {
        type: ["line", "bar", "stack"],
      },
      saveAsImage: { type: "png" },
    },
  },
};
</script>
  
<style>
</style>