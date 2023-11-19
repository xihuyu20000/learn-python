<template>
  <div class="son">
    子组件
    <hr />
    {{ option }}
  </div>
</template>
    
<script setup>
const props = defineProps({ option: {} });
</script>
    
<style scoped>
.son {
  width: 300px;
  height: 300px;
  background-color: #e6e6e6;
  padding: 30px;
}
</style>