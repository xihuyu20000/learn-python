<template>
  <div
    style="
      width: 150px;
      max-width: 250px;
      display: flex;
      flex-direction: column;
    "
  >
    <div
      style="
        height: 40px;
        max-height: 40px;
        border-bottom: 1px solid #8a8a8a;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
      "
    >
      <vxe-button type="text">加载</vxe-button>
      <vxe-button type="text">合并</vxe-button>
      <vxe-button type="text">解析</vxe-button>
      <vxe-button type="text" @click="dialogVisible = true">设置</vxe-button>
    </div>
    <div style="flex: 1">
      <vxe-table ref="tableRef" :data="tableData">
        <vxe-column type="radio" width="20"></vxe-column>
        <vxe-column field="name" title="名称"></vxe-column>
      </vxe-table>
    </div>
  </div>

  <el-dialog
    v-model="dialogVisible"
    title="请选择数据所在的文件夹"
    width="30%"
    :before-close="handleClose"
  >
    <div style="margin-top: 15px">
      <el-input placeholder="请选择文件夹" v-model="textarea">
        <el-button
          slot="append"
          icon="el-icon-folder-opened"
          @click="openFile"
        ></el-button>
      </el-input>
      <input
        type="file"
        name="filename"
        id="open"
        style="display: none"
        @change="changeFile"
        webkitdirectory
      />
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible = false">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script  setup>
import { ref } from "vue";
import { VXETable } from "vxe-table";
const tableRef = ref();
const tableData = ref([
  {
    id: 10001,
    name: "Test1",
  },
  {
    id: 10002,
    name: "Test2",
  },
  {
    id: 10003,
    name: "Test3",
  },
  {
    id: 10004,
    name: "Test4",
  },
  {
    id: 10005,
    name: "Test5",
  },
]);

const dialogVisible = ref(false);
const handleClose = (done) => {
  ElMessageBox.confirm("Are you sure to close this dialog?")
    .then(() => {
      done();
    })
    .catch(() => {
      // catch error
    });
};
</script>
