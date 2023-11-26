import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
const app = createApp(App);

// 路由
import router from "./router/index";
app.use(router);
// 全局组件
import components from "./components/index";
app.use(components);
// vxe-table
import VXETable from "vxe-table";
import "vxe-table/lib/style.css";
VXETable.config({ size: "mini" });
app.use(VXETable);
//pinia
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(pinia);

app.mount("#app");
