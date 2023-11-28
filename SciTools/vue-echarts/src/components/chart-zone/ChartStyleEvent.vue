<template>
  <el-tabs
    v-model="activeName"
    class="operations-tabs"
    @tab-click="handleClick"
  >
    <el-tab-pane label="样式" name="first">User</el-tab-pane>
    <el-tab-pane label="事件" name="second">Config</el-tab-pane>
    <el-tab-pane label="数据" name="third">Role</el-tab-pane>
  </el-tabs>
</template>
<script setup>
import { ref } from "vue";

const activeName = ref("first");

const handleClick = (tab, event) => {
  console.log(tab, event);
};
</script>
<style>
.operations-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 1em;
  font-weight: 600;
}
</style>