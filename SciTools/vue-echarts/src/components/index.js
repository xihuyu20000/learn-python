import BaseEChart from "./chart-zone/BaseEChart.vue";
import Child from "./Child.vue";

import NavMenu from "./NavMenu.vue";

export default {
  install(Vue) {
    Vue.component("BaseEChart", BaseEChart);
    Vue.component("Child", Child);
    Vue.component("NavMenu", NavMenu);
  },
};
