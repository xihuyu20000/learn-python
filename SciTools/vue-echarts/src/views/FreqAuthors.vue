<script setup>
import { freq_authors } from "../api/data";
import { pie_option } from "../utils/echarts_option";
const option = ref({});

onMounted(async () => {
  let result = await freq_authors();
  option.value = pie_option(result.data.title, result.data.y);
});
</script>

<template>
  <base-echart :option="option"></base-echart>
</template>

<style scoped></style>

