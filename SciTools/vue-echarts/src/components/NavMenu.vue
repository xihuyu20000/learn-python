<script setup>
</script>
<template>
  <el-aside width="50px" class="container">
    <div class="item">数据</div>
    <div class="item">分析</div>
    <div class="item">图谱</div>
    <div class="item">报告</div>
    <div class="item">设置</div>
    <div class="item myicon">我</div>
  </el-aside>
</template>
    

    
<style scoped>
.container {
  width: 50px;
  height: 100vh;
  background-color: DodgerBlue;
  display: flex;
  flex-direction: column;
}

.item {
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
</style>