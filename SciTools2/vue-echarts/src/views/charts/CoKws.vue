<script setup>
import { relation_option } from "../../utils/echarts_option";
import { co_kws } from "../../api/data";
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
  <chart-layout :option="option"></chart-layout>
</template>

<style scoped>
.echarts {
}
</style>

