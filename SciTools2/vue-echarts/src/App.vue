<script setup>
import * as echarts from "echarts";
provide("echarts", echarts);
</script>

<template>
  <div
    style="display: flex; width: 100%; height: 100%; background-color: #f2f2f2"
  >
    <div style="width: 50px; min-width: 50px" class="navcontainer">
      <div class="navitem"><router-link to="/table">数据</router-link></div>
      <div class="navitem"><router-link to="/chart">组件</router-link></div>
      <div class="navitem"><router-link to="/schema">分析</router-link></div>
      <div class="navitem"><router-link to="/graph">图谱</router-link></div>
      <div class="navitem"><router-link to="/report">报告</router-link></div>
      <div class="navitem">
        <router-link to="/settings">配置</router-link>
      </div>
      <div class="navitem">
        <router-link to="/mine">我</router-link>
      </div>
    </div>
    <div style="flex-grow: 1"><router-view></router-view></div>
  </div>
</template>


<style lang="scss" scoped>
.navcontainer {
  width: 50px;
  height: 100vh;
  background-color: DodgerBlue;
  display: flex;
  flex-direction: column;

  .navitem {
    background-color: #cdcccc;
    width: 50px;
    height: 50px;
    margin-top: 10px;
    text-align: center;
    line-height: 60px;
    border-radius: 2px;
    cursor: pointer;

    a:link {
      text-decoration: none;
    }
  }
}

.el-main {
  --el-main-padding: 5px;
}
</style>

