<template>
  <el-container>
    <el-aside :width="isCollapse ? 160 : 0">
      <div class="toggle-button" @click="isCollapse = !isCollapse">|||</div>
      <el-menu :collapse="isCollapse">
        <el-menu-item :index="i" v-for="(path, name, i) in urls" :key="i">
          <router-link :to="path">{{ name }}</router-link>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main> <router-view></router-view></el-main>
  </el-container>
</template>
    
<script setup>
const isCollapse = ref(false);
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
    
<style lang="scss" scoped>
.toggle-button {
  // 添加背景颜色
  background-color: #4a5064;
  // 设置文本大小
  font-size: 10px;
  // 设置文本行高
  line-height: 24px;
  // 设置文本颜色
  color: #fff;
  // 设置文本居中
  text-align: center;
  // 设置文本间距
  letter-spacing: 0.2em;
  // 设置鼠标悬浮变小手效果
  cursor: pointer;
}
.el-menu-item {
  height: 35px;
}
</style>