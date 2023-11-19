<script setup>
import { freq_yearly } from "../api/data";
import { line_option } from "../utils/echarts_option";
const option = ref({});

onMounted(async () => {
  let result = await freq_yearly();
  option.value = line_option(result.data.title, result.data.x, result.data.y);
});
</script>

<template>
  <base-echart :option="option"></base-echart>
</template>

<style scoped></style>

