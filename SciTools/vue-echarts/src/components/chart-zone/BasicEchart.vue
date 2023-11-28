<template>
  <div style="width: 100%; height: 100%; display: flex">
    <chart-icons-table></chart-icons-table>
    <column-names></column-names>
    <div style="flex: 1">
      <sub-chart-1001
        :option="option"
        v-if="1001 == mainStore.current_chartstyle_index"
      ></sub-chart-1001>
      <sub-chart-1002
        v-if="1002 == mainStore.current_chartstyle_index"
      ></sub-chart-1002>
    </div>
  </div>
</template>

<script setup>
import { useMainStore } from "../../store";
// 数据存储对象
const mainStore = useMainStore();

const option = ref({
  xAxis: {
    type: "category",
    data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      data: [150, 230, 224, 218, 135, 147, 260],
      type: "line",
    },
  ],
});
</script>
<style scoped>
</style>
