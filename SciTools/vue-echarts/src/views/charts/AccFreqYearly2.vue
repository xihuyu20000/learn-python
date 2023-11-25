<script setup>
import { line_option } from "../../utils/echarts_option";
import { acc_freq_yearly2 } from "../../api/data";
const option = ref({});

onMounted(async () => {
  let result = await acc_freq_yearly2();
  option.value = line_option(result.data.title, result.data.x, result.data.y);
});
</script>

<template>
  <basic-echart :option="option"></basic-echart>
</template>

<style scoped></style>

