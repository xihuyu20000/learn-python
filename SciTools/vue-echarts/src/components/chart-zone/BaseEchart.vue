<template>
  <div class="echart" ref="chartDom"></div>
</template>

<script setup>
import { useMainStore } from "@/store";
// 数据存储对象
const mainStore = useMainStore();
// 引入echarts组件
const echarts = inject("echarts");
//获取 dom 和 父组件数据 并定义"myChart"用于初始化图表
const chartDom = ref();
let myChart = null;
//重绘图表函数
const resizeHandler = () => {
  myChart.resize();
};
//设置防抖，保证无论拖动窗口大小，只执行一次获取浏览器宽高的方法
const debounce = (fun, delay) => {
  let timer;
  return function () {
    if (timer) {
      clearTimeout(timer);
    }
    timer = setTimeout(() => {
      fun();
    }, delay);
  };
};
const cancalDebounce = debounce(resizeHandler, 500);
//页面成功渲染，开始绘制图表
onMounted(() => {
  //配置为 svg 形式，预防页面缩放而出现模糊问题；图表过于复杂时建议使用 Canvas
  myChart = echarts.init(chartDom.value, null, { renderer: "svg" });
  // myChart = echarts.init(chartDom.value)
  let opt = mainStore.get_current_chart_option;
  myChart.setOption(opt, true);
  //自适应不同屏幕时改变图表尺寸
  window.addEventListener("resize", cancalDebounce);
});
//页面销毁前，销毁事件和实例
onBeforeUnmount(() => {
  window.removeEventListener("resize", cancalDebounce);
  myChart.dispose();
});
//监听图表数据时候变化，重新渲染图表
watch(
  () => [
    mainStore.get_current_chartstyle_index,
    mainStore.get_current_chart_option,
  ],
  () => {
    console.log(
      "配置项变化",
      mainStore.get_current_chartstyle_index,
      mainStore.get_current_chart_option
    );
    myChart.setOption(mainStore.get_current_chart_option, true);
  },
  { deep: true }
);
</script>
<style scoped>
.echart {
  width: 100%;
  height: 100%;
}
</style>
