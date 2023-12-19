<template>
  <div
    style="display: flex; width: 100%; height: 100%; background-color: #f2f2f2"
  >
    <el-container>
      <el-aside width="200px">
        <el-row>
          <el-col>
            <el-menu>
              <el-menu-item v-for="(item, i) in menus" :key="i">
                <router-link :to="item.url">{{ item.text }}</router-link>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-main
        ><div style="flex-grow: 1"><router-view></router-view></div
      ></el-main>
    </el-container>
  </div>
</template>
<script setup>
const menus = ref([
  { text: "折线图", url: "/chart0" },
  { text: "层次聚类图", url: "/chart1" },
  { text: "径向树图", url: "/chart2" },
  { text: "关系图", url: "/chart3" },
  { text: "桑吉图", url: "/chart4" },
  { text: "饼图", url: "/chart5" },
  { text: "堆叠折线图", url: "/chart6" },
  { text: "关系图", url: "/chart7" },
]);
</script>
<style lang="scss" scoped>
</style>
