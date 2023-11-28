<template>
  <el-container>
    <el-aside width="200px"> </el-aside>
    <el-aside width="200px">
      <chart-icons-table></chart-icons-table>
    </el-aside>
    <el-container>
      <el-header style="margin: 0; padding: 0">
        <drop-down-data></drop-down-data>
      </el-header>
      <el-main style="padding: 0"><div id="cytospacechart"></div></el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { onMounted } from "vue";

import cytoscape from "cytoscape";

const props = defineProps({
  option: Object,
});
let myChart = null;
onMounted(() => {
  myChart = cytoscape({
    container: document.getElementById("cytospacechart"), // container to render in

    elements: [
      {
        data: { id: "a" },
      },
      {
        data: { id: "b" },
      },
      {
        data: { id: "ab", source: "a", target: "b" },
      },
    ],

    style: [
      {
        selector: "node",
        style: {
          "background-color": "#666",
          label: "data(id)",
        },
      },

      {
        selector: "edge",
        style: {
          width: 3,
          "line-color": "#ccc",
          "target-arrow-color": "#ccc",
          "target-arrow-shape": "triangle",
          "curve-style": "unbundled-bezier",
        },
      },
    ],

    layout: {
      name: "grid",
      rows: 1,
    },
  });
});
</script>
<style scoped>
#cytospacechart {
  width: 100%;
  height: 600px;
  display: block;
  background: #d5d5d5;
}
</style>
