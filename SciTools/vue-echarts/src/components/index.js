import CytoChart from "./chart-zone/CytoChart.vue";
import BasicEChart from "./chart-zone/BasicEChart.vue";
import BaseTable from "./table-zone/BaseTable.vue";
import Uploaded from "./table-zone/Uploaded.vue";

export default {
  install(Vue) {
    Vue.component("CytoChart", CytoChart);
    Vue.component("BasicEChart", BasicEChart);
    Vue.component("BaseTable", BaseTable);
    Vue.component("Uploaded", Uploaded);
  },
};
