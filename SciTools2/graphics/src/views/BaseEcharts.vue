<template>
  <div>
    <div ref="chartRef" style="width: 1000px; height: 700px"></div>
  </div>
</template>
 
<script setup>
import * as echarts from "echarts";
const props = defineProps({
  options: {
    type: Object,
    require: true,
  },
});
//使用 vue ref 获取dom对象
const chartRef = ref();
// 在外定义储存图表 创建和销毁 的值
let myChart = null;

// vue onMounted钩子函数里执行创建echarts表格
onMounted(() => {
  myChart = echarts.init(chartRef.value);
  myChart.setOption(props.options);
});

//vue onBeforeUnmount钩子函数里 离开页面时 若存储表格的值存在则销毁表格
onBeforeUnmount(() => {
  if (myChart) {
    //echarts销毁函数
    echarts.dispose(myChart);
    myChart = null;
  }
});
</script>
 
<style></style>