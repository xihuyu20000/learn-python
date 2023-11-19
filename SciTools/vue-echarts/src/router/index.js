import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", redirect: "/tt" },
  {
    path: "/tt",
    name: "tt",
    component: () => import(`../views/table.vue`),
  },
  {
    path: "/FreqYearly",
    name: "FreqYearly",
    component: () => import(`../views/FreqYearly.vue`),
  },
  {
    path: "/AccFreqYearly",
    name: "AccFreqYearly",
    component: () => import(`../views/AccFreqYearly.vue`),
  },
  {
    path: "/AccFreqYearly2",
    name: "AccFreqYearly2",
    component: () => import(`../views/AccFreqYearly2.vue`),
  },
  {
    path: "/FreqAuthors",
    name: "FreqAuthors",
    component: () => import(`../views/FreqAuthors.vue`),
  },
  {
    path: "/FreqAuthors2",
    name: "FreqAuthors2",
    component: () => import(`../views/FreqAuthors2.vue`),
  },
  {
    path: "/CoKws",
    name: "CoKws",
    component: () => import(`../views/CoKws.vue`),
  },
  {
    path: "/CoKws2",
    name: "CoKws2",
    component: () => import(`../views/CoKws2.vue`),
  },
  {
    path: "/CoKws3",
    name: "CoKws3",
    component: () => import(`../views/CoKws3.vue`),
  },
  {
    path: "/Parent",
    name: "Parent",
    component: () => import(`../views/Parent.vue`),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
