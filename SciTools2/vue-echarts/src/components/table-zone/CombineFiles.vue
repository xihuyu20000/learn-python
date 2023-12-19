<template>
  <vxe-button type="text" @click="opening = true" title="合并多个文件"
    ><slot></slot
  ></vxe-button>
  <vxe-modal v-model="opening" width="600" show-footer>
    <template #title>
      <span style="color: red">合并数据文件</span>
    </template>
    <template #corner>
      <vxe-icon name="minus"></vxe-icon>
    </template>
    <template #default>
      <vxe-input
        v-model="newfilename"
        placeholder="请输入合并后的新的文件名称"
        style="width: 100%; margin-bottom: 10px"
        clearable
      ></vxe-input>
      <vxe-table
        show-overflow
        auto-resize
        height="300"
        ref="tableRef"
        :data="tableData"
      >
        <vxe-column type="checkbox" width="60"></vxe-column>
        <vxe-column field="name" title="数据文件名称"></vxe-column>
      </vxe-table>
    </template>

    <template #footer>
      <vxe-button status="primary" @click="confirmEvent">确定</vxe-button>
    </template>
  </vxe-modal>
</template>

<script setup>
import { ref } from "vue";
import { combine_datafiles } from "@/api/data";
const opening = ref(false);
const props = defineProps({
  tableData: Object,
});
const tableRef = ref();
// 新的文件名称
const newfilename = ref("");

async function confirmEvent() {
  const selectRecords = tableRef.value.getCheckboxRecords();
  const ids = selectRecords.map((row) => row.id);
  await combine_datafiles({ ids: ids, newfilename: newfilename.value });
  opening.value = false;
}
</script>
