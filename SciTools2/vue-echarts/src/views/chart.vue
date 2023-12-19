<script setup>
import { freq_yearly } from "../api/data";
import { line_option } from "@/store/option.js";
const option = ref({});

// onMounted(async () => {
//   let result = await freq_yearly();
//   option.value = line_option(result.data.title, result.data.x, result.data.y);
// });
</script>

<template>
  <chart-layout :option="option"></chart-layout>
</template>

<style scoped></style>

