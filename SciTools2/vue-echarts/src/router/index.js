import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", redirect: "/table" },
  {
    path: "/table",
    name: "table",
    component: () => import(`../views/table.vue`),
  },
  {
    path: "/chart",
    name: "chart",
    component: () => import(`../views/chart.vue`),
  },
  {
    path: "/schema",
    name: "schema",
    component: () => import(`../views/schema.vue`),
    children: [
      {
        path: "/FreqYearly",
        name: "FreqYearly",
        component: () => import(`../views/charts/FreqYearly.vue`),
      },
      {
        path: "/AccFreqYearly",
        name: "AccFreqYearly",
        component: () => import(`../views/charts/AccFreqYearly.vue`),
      },
      {
        path: "/AccFreqYearly2",
        name: "AccFreqYearly2",
        component: () => import(`../views/charts/AccFreqYearly2.vue`),
      },
      {
        path: "/FreqAuthors",
        name: "FreqAuthors",
        component: () => import(`../views/charts/FreqAuthors.vue`),
      },
      {
        path: "/FreqAuthors2",
        name: "FreqAuthors2",
        component: () => import(`../views/charts/FreqAuthors2.vue`),
      },
      {
        path: "/CoKws",
        name: "CoKws",
        component: () => import(`../views/charts/CoKws.vue`),
      },
      {
        path: "/CoKws2",
        name: "CoKws2",
        component: () => import(`../views/charts/CoKws2.vue`),
      },
      {
        path: "/BurstTerms",
        name: "BurstTerms",
        component: () => import(`../views/charts/BurstTerms.vue`),
      },
      {
        path: "/Pupples",
        name: "Pupples",
        component: () => import(`../views/charts/Pupples.vue`),
      },
      {
        path: "/CSChart",
        name: "CSChart",
        component: () => import(`../views/charts/CSChart.vue`),
      },
    ],
  },

  {
    path: "/graph",
    name: "graph",
    component: () => import(`../views/graph.vue`),
  },
  {
    path: "/report",
    name: "report",
    component: () => import(`../views/report.vue`),
  },
  {
    path: "/settings",
    name: "settings",
    component: () => import(`../views/settings.vue`),
  },
  {
    path: "/mine",
    name: "mine",
    component: () => import(`../views/mine.vue`),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
