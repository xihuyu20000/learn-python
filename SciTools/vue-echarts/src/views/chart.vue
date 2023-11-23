<template>
  <el-container>
    <el-aside width="160px">
      <el-menu>
        <el-menu-item :index="i" v-for="(path, name, i) in urls" :key="i">
          <router-link :to="path">{{ name }}</router-link>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main> <router-view></router-view></el-main>
  </el-container>
</template>
    
<script setup>
const urls = ref({
  历年发文量: "/FreqYearly",
  历年累计发文量: "/AccFreqYearly",
  混合累计发文量: "/AccFreqYearly2",
  作者发文量: "/FreqAuthors",
  作者发文量2: "/FreqAuthors2",
  关键词共现: "/CoKws",
  关键词共现2: "/CoKws2",
  父子: "/Parent",
});
</script>
    
<style scoped>
.el-menu-item {
  height: 35px;
}
</style>