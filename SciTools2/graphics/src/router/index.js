import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", redirect: "/chart2" },
  {
    path: "/chart0",
    name: "折线图",
    component: () => import(`../views/chart0.vue`),
  },
  {
    path: "/chart1",
    name: "层次聚类图/系统聚类图",
    component: () => import(`../views/chart1.vue`),
  },
  {
    path: "/chart2",
    name: "径向树图",
    component: () => import(`../views/chart2.vue`),
  },
  {
    path: "/chart3",
    name: "关系图",
    component: () => import(`../views/chart3.vue`),
  },
  {
    path: "/chart4",
    name: "桑基图",
    component: () => import(`../views/chart4.vue`),
  },
  {
    path: "/chart5",
    name: "饼图",
    component: () => import(`../views/chart5.vue`),
  },
  {
    path: "/chart6",
    name: "堆叠折线图",
    component: () => import(`../views/chart6.vue`),
  },
  {
    path: "/chart7",
    name: "关系图",
    component: () => import(`../views/chart7.vue`),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
