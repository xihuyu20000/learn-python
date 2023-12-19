<template>
  <div style="display: flex; height: 100vh; background-color: #f2f2f2">
    <div>
      <div class="menu-item" v-for="(item, i) in menus" :key="i">
        <router-link :to="item.url">{{ item.text }}</router-link>
      </div>
    </div>

    <div class="menu-others"><router-view></router-view></div>
  </div>
</template>
<script setup>
const menus = ref([
  { text: "折线图", url: "/chart00" },
  { text: "层次聚类图", url: "/chart01" },
  { text: "径向树图", url: "/chart02" },
  { text: "关系图", url: "/chart03" },
  { text: "桑吉图", url: "/chart04" },
  { text: "饼图", url: "/chart05" },
  { text: "堆叠折线图", url: "/chart06" },
  { text: "关系图", url: "/chart07" },
]);
</script>
<style lang="scss" scoped>
.menu-item {
  width: 150px;
}
.menu-others {
  flex-grow: 1;
}
</style>
