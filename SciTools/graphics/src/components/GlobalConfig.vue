<!-- 首页布局 -->
<template>
  <div class="global-area">
    <div class="data-chart-area">
      <div class="data-area"></div>
      <div class="chart-area">
        <base-echart :options="props.options"></base-echart>
      </div>
    </div>
    <div class="config-area"></div>
  </div>
</template>

<script setup>
import BaseEchart from "@/components/BaseEchart.vue";
import { onMounted } from "vue";

const props = defineProps({
  options: {
    type: Object,
    require: true,
  },
});

onMounted(() => {});
</script>
<style lang='scss' scoped>
.global-area {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  background-color: #fff;

  .data-chart-area {
    flex: 2;
    background-color: azure;
    display: flex;
    flex-direction: column;

    .data-area {
      flex: 1;
      background-color: burlywood;
    }

    .chart-area {
      flex: 2;
      background-color: darkseagreen;
    }
  }
  .config-area {
    flex: 1;
    background-color: rgb(104, 65, 14);
  }
}
</style>