<template>
  <vxe-select placeholder="员工表">
    <vxe-option
      v-for="num in 15"
      :key="num"
      :value="num"
      :label="`选项${num}`"
    ></vxe-option>
  </vxe-select>
  <hr />
  <div>员工表</div>
  <vxe-list
    class="my-table-list"
    height="200"
    :data="datalist"
    :scroll-y="{ enabled: true, gt: 60, sItem: '.my-tr' }"
  >
    <template #default="{ items }">
      <table>
        <tbody>
          <tr class="my-tr" v-for="item in items" :key="item.id">
            <td draggable="true">{{ item.label }}</td>
          </tr>
        </tbody>
      </table>
    </template>
  </vxe-list>
</template>
    
<script setup>
const datalist = ref([
  { id: 1, label: "合同签约时间" },
  { id: 2, label: "注册时间" },
  { id: 3, label: "合同付款类型" },
  { id: 4, label: "合同类型" },
]);
</script>
    
<style>
</style>