<script setup>
import * as echarts from "echarts";
provide("echarts", echarts);
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-container>
        <nav-menu></nav-menu>
        <el-main> <router-view></router-view></el-main>
      </el-container>
    </el-container>
  </div>
</template>


<style scoped>
.el-main {
  --el-main-padding: 5px;
}
</style>

