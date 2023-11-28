<template>
  <vxe-select v-model="dataModel" placeholder="超小尺寸" size="mini">
    <vxe-option
      v-for="num in 5"
      :key="num"
      :value="num"
      :label="`选项${num}`"
    ></vxe-option>
  </vxe-select>
</template>
    
<script setup>
const dataModel = ref();
</script>
    
<style>
</style>