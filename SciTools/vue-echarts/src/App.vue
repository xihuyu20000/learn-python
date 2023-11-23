<script setup>
import * as echarts from "echarts";
provide("echarts", echarts);
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="50px" class="navcontainer">
        <div class="navitem"><router-link to="/table">数据</router-link></div>
        <div class="navitem"><router-link to="/chart">分析</router-link></div>
        <div class="navitem"><router-link to="/graph">图谱</router-link></div>
        <div class="navitem"><router-link to="/report">报告</router-link></div>
        <div class="navitem">
          <router-link to="/settings">配置</router-link>
        </div>
        <div class="navitem myicon">
          <router-link to="/profile">我</router-link>
        </div>
      </el-aside>
      <el-main> <router-view></router-view></el-main>
    </el-container>
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
  }

  .myicon {
    position: absolute;
    bottom: 0;

    border-radius: 0;
  }
}

.el-main {
  --el-main-padding: 5px;
}
</style>

