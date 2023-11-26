<template>
  <el-upload
    v-model:file-list="fileList"
    class="upload-demo"
    action="/api/upload"
    multiple
    style="margin: 0 auto"
  >
    <el-button type="primary">上传数据文件</el-button>
    <template #tip>
      <div class="el-upload__tip"></div>
    </template>
  </el-upload>
</template>
<script  setup>
import { ref } from "vue";

const fileList = ref([]);
</script>
