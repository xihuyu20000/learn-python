<template>
  <div
    style="
      width: 150px;
      max-width: 250px;
      display: flex;
      flex-direction: column;
    "
  >
    <!-- 显示数据文件夹 -->
    <vxe-button
      @click="click_datafiles_dir"
      :title="dataDir"
      type="text"
      class="data-dir-btn"
      >{{ dataDir }}</vxe-button
    >
    <!-- 工具栏 -->
    <div class="data-toolbar">
      <vxe-button
        type="text"
        title="重新加载数据文件列表"
        @click="click_load_datafiles"
        >加载</vxe-button
      >
      <combine-files ref="combineFilesCmp" :tableData="tableData"
        >合并</combine-files
      >
      <vxe-button type="text" transfer title="解析数据文件，结果展示在右侧表格">
        <template #default>解析</template>
        <template #dropdowns>
          <vxe-button
            type="text"
            @click="click_parse_datafile($event, 'cnki')"
            content="CNKI"
          ></vxe-button>
          <vxe-button
            type="text"
            @click="click_parse_datafile($event, 'wos')"
            content="WOS"
          ></vxe-button>
        </template>
      </vxe-button>
    </div>

    <!-- 表格 -->
    <div style="flex: 1">
      <vxe-table
        height="auto"
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
import { VXETable } from "vxe-table";

// 数据文件夹名称
const dataDir = ref("【没有设置数据文件夹】");
// 合并数据文件
const combineFilesCmp = ref();
// 表格本身
const tableRef = ref();
// 表格中的数据
const tableData = ref([]);
// 数据存储对象
const mainStore = useMainStore();
//--------------------------------------------------------------------------------------------

/**
 * 点击数据文件夹
 */
function click_datafiles_dir() {
  let path = prompt("请输入数据文件夹路径", dataDir.value);
  if (path != null) {
    dataDir.value = path;
    save_config({ data_dir: path });
  }
}

/**
 * 加载数据文件夹
 */
async function get_datadir() {
  let resp = await get_config_datadir();
  dataDir.value = resp;
  console.info("加载数据文件夹", new Date().getTime());
}
/**
 * 加载数据文件
 */
async function click_load_datafiles() {
  tableData.value = [];
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
  VXETable.modal.message({ content: "加载数据文件", status: "success" });
  console.info("加载数据文件", new Date().getTime());
}

/**
 * 解析数据文件
 */
const emit = defineEmits(["refresh"]);
function click_parse_datafile(event, style) {
  let current = tableRef.value.getCurrentRecord();
  mainStore.save_current_datafile_index(current.id);
  // 调用父组件中的方法
  emit("refresh", style, current.id);
  console.info("解析数据文件", style, new Date().getTime());
}
/**
 * 选中行的颜色
 * @param {Object} row
 * @param {int} rowIndex
 */
function currentRowClass({ row, rowIndex }) {
  if (mainStore.current_datafile_index == rowIndex) {
    return { "background-color": "#1cb1f5" };
  }
}
//------------------------------------------------------------------------------------------------
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
.vxe-button--dropdown {
  padding-top: 6px;
}
</style>