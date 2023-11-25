import CytoChart from "./chart-zone/CytoChart.vue";
import BasicEChart from "./chart-zone/BasicEChart.vue";

export default {
  install(Vue) {
    Vue.component("CytoChart", CytoChart);
    Vue.component("BasicEChart", BasicEChart);
  },
};
