<script setup>
</script>
<template>
  <el-aside width="200px">
    <el-menu>
      <el-menu-item index="0">
        <el-icon><setting /></el-icon>
        <router-link to="/tt">表格</router-link>
      </el-menu-item>
      <el-menu-item index="1">
        <el-icon><setting /></el-icon>
        <router-link to="/FreqYearly">历年发文量</router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <el-icon><setting /></el-icon>
        <router-link to="/AccFreqYearly">历年累计发文量</router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <el-icon><setting /></el-icon>
        <router-link to="/AccFreqYearly2">混合累计发文量</router-link>
      </el-menu-item>
      <el-menu-item index="4">
        <el-icon><setting /></el-icon>
        <router-link to="/FreqAuthors">作者发文量</router-link>
      </el-menu-item>
      <el-menu-item index="5">
        <el-icon><setting /></el-icon>
        <router-link to="/FreqAuthors2">作者发文量2</router-link>
      </el-menu-item>
      <el-menu-item index="6">
        <el-icon><setting /></el-icon>
        <router-link to="/CoKws">关键词共现</router-link>
      </el-menu-item>
      <el-menu-item index="7">
        <el-icon><setting /></el-icon>
        <router-link to="/CoKws2">关键词共现2</router-link>
      </el-menu-item>

      <el-menu-item index="4">
        <el-icon><setting /></el-icon>
        <router-link to="/Parent">父子传值</router-link>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>
    

    
<style scoped>
.el-menu-item {
  height: 30px;
}
</style>