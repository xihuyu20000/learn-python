<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const chart1 = ref(); // 创建dom引用

onMounted(() => {
  const myChart = echarts.init(chart1.value); // 初始化echarts实例
  const option = {
    xAxis: {
      type: "category",
      data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [150, 230, 224, 218, 135, 147, 260],
        type: "line",
      },
    ],
  };

  myChart.setOption(option);
});
</script>

<template>
   
  <div ref="chart1" style="width: 400px; height: 400px"></div>
</template>