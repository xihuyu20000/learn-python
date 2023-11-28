import CytoChart from "./chart-zone/CytoChart.vue";
import ChartLayout from "./chart-zone/ChartLayout.vue";
import TableLayout from "./table-zone/TableLayout.vue";

export default {
  install(Vue) {
    Vue.component("CytoChart", CytoChart);
    Vue.component("ChartLayout", ChartLayout);
    Vue.component("TableLayout", TableLayout);
  },
};
