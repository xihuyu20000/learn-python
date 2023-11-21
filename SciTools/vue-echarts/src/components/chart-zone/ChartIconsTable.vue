<template>
  <el-container style="margin: 0; padding: 0">
    <span style="margin-bottom: 5px">图表类型</span>
    <el-header style="height: 120px; margin: 0; padding: 0">
      <div class="chart-style-icon">
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格1" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格2" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格3" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格4" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格5" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格6" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格7" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格8" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格1" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格2" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格3" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格4" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格5" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格6" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格7" />
        </div>
        <div class="icon">
          <img src="../../assets/biaoge.png" alt="表格8" />
        </div>
      </div>
    </el-header>
    <el-tabs :stretch="true">
      <el-tab-pane label="样式" name="first">
        <div class="input-item">
          <span class="input-label">颜色</span
          ><vxe-input style="width: 150px" size="mini"></vxe-input>
        </div>
        <div class="input-item">
          <span class="input-label">大小</span>
          <vxe-input style="width: 150px" size="mini"></vxe-input>
        </div>
      </el-tab-pane>
      <el-tab-pane label="数据" name="second">数据</el-tab-pane>
      <el-tab-pane label="事件" name="third">事件</el-tab-pane>
    </el-tabs>
  </el-container>
</template>
    
<script setup lang='ts'>
</script>
    
<style scoped>
.chart-style-icon {
  width: 100%;

  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 1fr);
}
.chart-style-icon .icon {
}
.chart-style-icon .icon img {
  width: 25px;
  height: 25px;
}
.chart-style-icon .icon img:hover {
  background-color: red;
}

.input-item {
  margin-bottom: 5px;
}
.input-label {
  font-size: 14px;
  margin-right: 5px;
}
</style>