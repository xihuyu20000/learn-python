import { defineStore } from "pinia";
import { option_mapping } from "@/store/option.js";
export const useMainStore = defineStore("main", {
  id: "main",

  state: () => ({
    // 当前选中的数据文件
    current_datafile_index: "0",
    // 激活的图表面板
    active_chart_collapse_item: "0",
    // 当前选中的图表类型
    current_chartstyle_index: "0",
    // 当前图表的配置信息
    current_chart_option: undefined,
  }),

  getters: {
    get_current_datafile_index: (state) => {
      return state.current_datafile_index;
    },
    get_active_chart_collapse_item: (state) => {
      return state.active_chart_collapse_item;
    },
    get_current_chartstyle_index: (state) => {
      return state.current_chartstyle_index;
    },
    get_current_chart_option: (state) => {
      if (undefined == state.current_chart_option) {
        let default_option = option_mapping(state.get_current_chartstyle_index);
        state.save_current_chart_option(default_option);
      }
      return state.current_chart_option;
    },
  },

  actions: {
    save_current_datafile_index(i) {
      this.current_datafile_index = i;
    },
    save_active_chart_collapse_item(i) {
      this.active_chart_collapse_item = i;
    },
    save_current_chartstyle_index(i) {
      this.current_chartstyle_index = i;
    },
    save_current_chart_option(i) {
      this.current_chart_option = i;
    },
  },

  persist: {
    enabled: true,
    key: "scitools",
    storage: sessionStorage,
    serializer: {
      deserialize: JSON.parse,
      serialize: JSON.stringify,
    },
    beforeRestore: (ctx) => {
      console.log(`about to restore '${ctx.store.$id}'`);
    },
    afterRestore: (ctx) => {
      console.log(`just restored '${ctx.store.$id}'`);
    },
    debug: true,
  },
});
