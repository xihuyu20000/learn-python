<template>
  <div>
    <vxe-grid v-bind="gridOptions"></vxe-grid>
  </div>
</template>
    
<script setup>
import { detail_table } from "../api/data";

const gridOptions = reactive({
  border: true,
  stripe: true,
  showFooter: true,
  autorResize: true,
  showOverflow: true,
  exportConfig: {},
  columnConfig: {
    resizable: true,
  },
  toolbarConfig: {
    export: true,
    custom: true,
    slots: {},
  },
  columns: [
    { type: "seq", width: 60 },
    { field: "abs", title: "abs", sortable: true },
    {
      field: "authors",
      title: "authors",
      sortable: true,
    },
    {
      field: "doctype",
      title: "doctype",

      sortable: true,
    },
    { field: "kws", title: "kws", sortable: true },
    { field: "orgs", title: "orgs", sortable: true },
    {
      field: "pubyear",
      title: "pubyear",
      sortable: true,
    },
    {
      field: "source",
      title: "source",
      sortable: true,
    },
    {
      field: "title",
      title: "title",
      sortable: true,
    },
  ],
  proxyConfig: {
    ajax: {
      query: ({ page, sort, filters }) => {
        return detail_table().then((resp) => {
          return resp.data;
        });
      },
    },
  },
});
</script>
    
<style scoped>
</style>