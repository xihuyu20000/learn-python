<script setup>
import { freq_authors } from "../../api/data";
import { rose_option } from "../../utils/echarts_option";
const option = ref({});

onMounted(async () => {
  let result = await freq_authors();
  option.value = rose_option(result.data.title, result.data.y);
});
</script>

<template>
  <base-echart :option="option"></base-echart>
</template>

<style scoped></style>

