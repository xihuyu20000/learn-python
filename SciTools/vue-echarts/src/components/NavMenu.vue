<script setup>
</script>
<template>
  <el-aside width="50px" class="navcontainer">
    <div class="navitem">数据</div>
    <div class="navitem">分析</div>
    <div class="navitem">图谱</div>
    <div class="navitem">报告</div>
    <div class="navitem">设置</div>
    <div class="navitem myicon">我</div>
  </el-aside>
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
</style>