<!-- echarts组件 -->
<template>
  <div ref="chart1" style="width: 100%; height: 100%"></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const chart1 = ref(null); // 创建dom引用

// 防抖
const throttle = function (fn, wait) {
  let timer = null;
  return function () {
    let context = this;
    let args = arguments;
    if (!timer) {
      // 当延迟时间结束后，执行函数
      timer = setTimeout(() => {
        timer = null;
        fn.apply(context, args);
      }, wait);
    }
  };
};
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

  new ResizeObserver((entries) => {
    throttle(() => {
      myChart.resize({
        width: entries[0].contentRect.width,
        height: entries[0].contentRect.height,
      });
    }, 500)();
  }).observe(chart1.value);
});
</script>
<style lang='scss' scoped>
</style>