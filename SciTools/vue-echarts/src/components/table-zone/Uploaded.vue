<template>
  <div
    style="
      width: 150px;
      max-width: 250px;
      display: flex;
      flex-direction: column;
    "
  >
    <vxe-button
      @click="click_datafiles_dir"
      :title="dataDir"
      type="text"
      class="data-dir-btn"
      >{{ dataDir }}</vxe-button
    >
    <div class="data-toolbar">
      <vxe-button type="text" @click="click_load_datafiles">加载</vxe-button>
      <vxe-button type="text" @click="click_combine_datafiles">合并</vxe-button>
      <vxe-button type="text" @click="click_parse_datafile">解析</vxe-button>
    </div>
    <div style="flex: 1">
      <vxe-table
        ref="tableRef"
        :data="tableData"
        :row-config="{ isHover: true, isCurrent: true }"
        :row-style="currentRowClass"
      >
        <vxe-column field="name" title="数据文件"></vxe-column>
      </vxe-table>
    </div>
  </div>
</template>
<script  setup>
import { useMainStore } from "../../store";
import { onMounted, ref } from "vue";
import { list_datafiles, get_config_datadir, save_config } from "@/api/data";
const tableRef = ref();
const tableData = ref([]);
const mainStore = useMainStore();

const dataDir = ref("【没有设置数据文件夹】");
// 显示数据文件夹
const click_datafiles_dir = () => {
  let path = prompt("请输入数据文件夹路径", dataDir.value);
  if (path != null) {
    dataDir.value = path;
    save_config({ data_dir: path });
  }
  console.info("显示数据文件夹");
};

// 加载数据文件夹
async function get_datadir() {
  let resp = await get_config_datadir();
  dataDir.value = resp;
  console.info("加载数据文件夹", new Date().getTime());
}
// 加载数据文件
async function click_load_datafiles() {
  let resp = await list_datafiles();
  tableData.value = resp.map((filename, index) => ({
    id: index,
    name: filename,
  }));
  // 设置选中行的颜色
  const $table = tableRef.value;
  if ($table) {
    $table.setCurrentRow(tableData.value[mainStore.current_datafile_index]);
  }
  console.info("加载数据文件", new Date().getTime());
}
// 合并文件
const click_combine_datafiles = () => {
  console.info("合并数据文件", new Date().getTime());
};

const emit = defineEmits(["refresh"]);
// 解析数据文件
const click_parse_datafile = () => {
  let current = tableRef.value.getCurrentRecord();
  mainStore.save_current_datafile_index(current.id);
  // 调用父组件中的方法
  emit("refresh", current.id);
  console.info("解析数据文件", current, new Date().getTime());
};
// 选中行的颜色
const currentRowClass = ({ row, rowIndex }) => {
  if (mainStore.current_datafile_index == rowIndex) {
    return { "background-color": "#a8a8a8" };
  }
};
onMounted(async () => {
  get_datadir();
  click_load_datafiles();
});
</script>
<style lang="scss" scoped>
.data-dir-btn {
  height: 25px;
  border: 1px solid #8a8a8a;
  display: flex;
  flex-direction: row;
}
.data-toolbar {
  height: 40px;
  max-height: 40px;
  border-top: 1px solid #8a8a8a;
  border-bottom: 1px solid #8a8a8a;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>