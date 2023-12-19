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
  xAxis: {
    type: "category",
    data: keysArray,
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      data: valuesArray,
      type: "line",
      itemStyle: { normal: { label: { show: true } } },
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