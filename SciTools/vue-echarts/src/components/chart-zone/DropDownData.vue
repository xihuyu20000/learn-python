<template>
  <div class="dropdown-item">
    <span class="dropdown-label">维度</span
    ><vxe-input style="width: 100%"></vxe-input>
  </div>
  <div class="dropdown-item">
    <span class="dropdown-label">指标</span>
    <vxe-input style="width: 100%"></vxe-input>
  </div>
</template>
    
<script setup lang='ts'>
</script>
    
<style >
.dropdown-item {
  display: flex;
  flex-wrap: nowrap;
  margin-bottom: 5px;
}
.dropdown-label {
  width: 40px;
}
</style>