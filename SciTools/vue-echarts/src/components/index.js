import CytoChart from "./chart-zone/CytoChart.vue";
import BasicEChart from "./chart-zone/BasicEChart.vue";
import BaseTable from "./table-zone/BaseTable.vue";

export default {
  install(Vue) {
    Vue.component("CytoChart", CytoChart);
    Vue.component("BasicEChart", BasicEChart);
    Vue.component("BaseTable", BaseTable);
  },
};
