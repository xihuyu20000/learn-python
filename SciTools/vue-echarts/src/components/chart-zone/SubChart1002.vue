<template>1002</template>

<script setup>
import { onMounted } from "vue";
import { useMainStore } from "../../store";

// 数据存储对象
const mainStore = useMainStore();
const props = defineProps({
  option: Object,
});

onMounted(() => {});
</script>
<style scoped>
</style>
