import { defineStore } from "pinia";

export const useMainStore = defineStore("main", {
  id: "main",

  state: () => ({
    current_datafile_index: "",
    current_chartstyle_index: "",
  }),

  getters: {
    int: (current_datafile_index) => state.current_datafile_index,
    int: (current_chartstyle_index) => state.current_chartstyle_index,
  },

  actions: {
    save_current_datafile_index(i) {
      this.current_datafile_index = i;
    },
    save_current_chartstyle_index(i) {
      this.current_chartstyle_index = i;
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
