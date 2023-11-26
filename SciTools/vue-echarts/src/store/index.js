import { defineStore } from "pinia";

export const useMainStore = defineStore("main", {
  id: "main",

  state: () => ({
    current_datafile_index: "",
  }),

  getters: {
    int: (current_datafile_index) => state.current_datafile_index,
  },

  actions: {
    save_current_datafile_index(i) {
      this.current_datafile_index = i;
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
