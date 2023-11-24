import BaseEChart from "./chart-zone/BaseEChart.vue";
import BasicEChart from "./chart-zone/BasicEChart.vue";

export default {
  install(Vue) {
    Vue.component("BaseEChart", BaseEChart);
    Vue.component("BasicEChart", BasicEChart);
  },
};
