<script setup>
import * as echarts from "echarts";
provide("echarts", echarts);
</script>

<template>
  <div class="common-layout">
    <el-container>
      <nav-menu></nav-menu>
      <el-container>
        <el-aside width="150px">
          <el-menu>
            <el-menu-item index="0">
              <router-link to="/tt">表格</router-link>
            </el-menu-item>
            <el-menu-item index="1">
              <router-link to="/FreqYearly">历年发文量</router-link>
            </el-menu-item>
            <el-menu-item index="2">
              <router-link to="/AccFreqYearly">历年累计发文量</router-link>
            </el-menu-item>
            <el-menu-item index="3">
              <router-link to="/AccFreqYearly2">混合累计发文量</router-link>
            </el-menu-item>
            <el-menu-item index="4">
              <router-link to="/FreqAuthors">作者发文量</router-link>
            </el-menu-item>
            <el-menu-item index="5">
              <router-link to="/FreqAuthors2">作者发文量2</router-link>
            </el-menu-item>
            <el-menu-item index="6">
              <router-link to="/CoKws">关键词共现</router-link>
            </el-menu-item>
            <el-menu-item index="7">
              <router-link to="/CoKws2">关键词共现2</router-link>
            </el-menu-item>

            <el-menu-item index="4">
              <router-link to="/Parent">父子传值</router-link>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main> <router-view></router-view></el-main>
      </el-container>
    </el-container>
  </div>
</template>


<style scoped>
.el-main {
  --el-main-padding: 5px;
}
.el-menu-item {
  height: 35px;
}
</style>

