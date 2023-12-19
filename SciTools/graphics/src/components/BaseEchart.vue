<!-- echarts组件 -->
<template>
  <div id="outer-chart-box">
    <div id="inner-chart" ref="chart1" style="width: 1px; height: 1px"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const chart1 = ref(null); // 创建dom引用

const props = defineProps({
  options: {
    type: Object,
    require: true,
  },
});

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

  myChart.setOption(props.options);

  new ResizeObserver((entries) => {
    throttle(() => {
      myChart.resize({
        width: entries[0].contentRect.width,
        height: entries[0].contentRect.height,
      });
    }, 1000)();
  }).observe(document.getElementById("outer-chart-box"));
});
</script>
<style lang='scss' scoped>
#outer-chart-box {
  width: 100%;
  height: 100%;
}
</style>