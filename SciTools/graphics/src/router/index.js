import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", redirect: "/chart00" },
  {
    path: "/chart00",
    name: "折线图",
    component: () => import(`../views/chart00.vue`),
  },
  {
    path: "/chart01",
    name: "层次聚类图/系统聚类图",
    component: () => import(`../views/chart01.vue`),
  },
  {
    path: "/chart02",
    name: "径向树图",
    component: () => import(`../views/chart02.vue`),
  },
  {
    path: "/chart03",
    name: "关系图",
    component: () => import(`../views/chart03.vue`),
  },
  {
    path: "/chart04",
    name: "桑基图",
    component: () => import(`../views/chart04.vue`),
  },
  {
    path: "/chart05",
    name: "饼图",
    component: () => import(`../views/chart05.vue`),
  },
  {
    path: "/chart06",
    name: "堆叠折线图",
    component: () => import(`../views/chart06.vue`),
  },
  {
    path: "/chart07",
    name: "关系图谱",
    component: () => import(`../views/chart07.vue`),
  },
  // {
  //   path: "/chart08",
  //   name: "chart08",
  //   component: () => import(`../views/chart08.vue`),
  // },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
