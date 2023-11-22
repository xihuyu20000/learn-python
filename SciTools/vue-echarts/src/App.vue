<script setup>
import * as echarts from "echarts";
provide("echarts", echarts);
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="50px" class="navcontainer">
        <div class="navitem"><router-link to="/table">数据</router-link></div>
        <div class="navitem"><router-link to="/chart">组件</router-link></div>
        <div class="navitem"><router-link to="/graph">图谱</router-link></div>
        <div class="navitem"><router-link to="/report">报告</router-link></div>
        <div class="navitem">
          <router-link to="/settings">设置</router-link>
        </div>
        <div class="navitem myicon">我</div>
      </el-aside>
      <el-main> <router-view></router-view></el-main>
    </el-container>
  </div>
</template>


<style scoped>
.navcontainer {
  width: 50px;
  height: 100vh;
  background-color: DodgerBlue;
  display: flex;
  flex-direction: column;
}

.navitem {
  background-color: #cdcccc;
  width: 50px;
  height: 50px;
  margin-top: 10px;
  text-align: center;
  line-height: 60px;
  border-radius: 2px;
  font-size: 1.2em;
  cursor: pointer;
}
.myicon {
  position: absolute;
  bottom: 0;

  border-radius: 0;
}
.el-main {
  --el-main-padding: 5px;
}
.el-menu-item {
  height: 35px;
}
</style>

