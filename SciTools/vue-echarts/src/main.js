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

app.mount("#app");
