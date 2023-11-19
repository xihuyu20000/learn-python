<script setup>
import { relation_option } from "../utils/echarts_option";
import { co_kws } from "../api/data";
const option = ref({});

onMounted(async () => {
  let result = await co_kws();
  option.value = relation_option(
    result.data.nodes,
    result.data.links,
    result.data.categories
  );
});
</script>

<template>
  <base-echart class="echarts" :option="option"></base-echart>
</template>

<style scoped>
.echarts {
  background-color: #e4e4e4;
}
</style>

