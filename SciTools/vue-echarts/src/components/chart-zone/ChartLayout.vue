<template>
  <div style="width: 100%; height: 100%; display: flex">
    <chart-icons-table></chart-icons-table>
    <chart-data-style></chart-data-style>
    <div style="flex: 1">
      <sub-chart-1001
        v-if="1001 == mainStore.get_current_chartstyle_index"
      ></sub-chart-1001>
      <sub-chart-1002
        v-if="1002 == mainStore.get_current_chartstyle_index"
      ></sub-chart-1002>
    </div>
  </div>
</template>

<script setup>
import { useMainStore } from "../../store";
// 数据存储对象
const mainStore = useMainStore();
</script>
<style scoped>
</style>
