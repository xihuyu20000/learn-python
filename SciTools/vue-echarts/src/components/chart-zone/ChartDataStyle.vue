<template>
  <div style="width: 200px; height: 100vh">
    <el-tabs v-model="activeTabPane" class="operations-tabs">
      <el-tab-pane label="数据" name="data">
        <chart-data-style-data></chart-data-style-data>
      </el-tab-pane>
      <el-tab-pane label="样式" name="style">
        <chart-data-style-style></chart-data-style-style>
      </el-tab-pane>
      <el-tab-pane label="事件" name="event">事件</el-tab-pane>
    </el-tabs>
  </div>
</template>
<script setup>
import { ref } from "vue";
// 激活的标签页
const activeTabPane = "style";
</script>
<style scoped>
.operations-tabs .el-tabs__content {
  padding: 20px;
  color: #6b778c;
  font-size: 1em;
}
</style>