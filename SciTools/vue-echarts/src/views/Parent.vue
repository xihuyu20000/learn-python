
<template>
  父组件
  <button @click="add1">点击</button>
  <Child :option="option"></Child>
</template>
    
<script setup>
import { onMounted } from "vue";

const option = ref();

onMounted(() => {
  option.value = {
    xAxis: {
      type: "category",
      data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [150, 230, 224, 218, 135, 147],
        type: "line",
      },
    ],
  };
});

function add1() {
  option.value["series"][0]["data"][0] += 1;
}
</script>
    
<style>
</style>