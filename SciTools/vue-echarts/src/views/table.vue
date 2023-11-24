<template>
  <div>
    <vxe-grid v-bind="gridOptions">
      <template #toolbar_buttons>
        <vxe-button>新增公式列</vxe-button>
        <vxe-button>新增汇总列</vxe-button>
        <vxe-button>新增赋值列</vxe-button>
        <vxe-button>条件标签列</vxe-button>
        <vxe-button>分组汇总</vxe-button>
        <vxe-button>过滤</vxe-button>
        <vxe-button>排序</vxe-button>
        <vxe-button>拆分行</vxe-button>
        <vxe-button>拆分列</vxe-button>
        <vxe-button>去除重复行</vxe-button>
      </template></vxe-grid
    >
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
    custom: true,
    slots: {
      buttons: "toolbar_buttons",
    },
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
  menuConfig: {
    header: {
      options: [
        [
          {
            code: "exportAll",
            name: "导出所有.csv",
            prefixIcon: "vxe-icon-download",
            visible: true,
            disabled: false,
          },
        ],
      ],
    },
    body: {
      options: [
        [
          {
            code: "copy",
            name: "复制内容",
            prefixIcon: "vxe-icon-copy",
            visible: true,
            disabled: false,
          },
          { code: "clear", name: "清除内容", visible: true, disabled: false },
          { code: "reload", name: "刷新表格", visible: true, disabled: false },
        ],
        [
          {
            code: "myPrint",
            name: "打印",
            prefixIcon: "vxe-icon-print",
            visible: true,
            disabled: false,
          },
          {
            code: "myExport",
            name: "导出.csv",
            prefixIcon: "vxe-icon-download",
            visible: true,
            disabled: false,
          },
        ],
      ],
    },
    footer: {
      options: [
        [
          {
            code: "exportAll",
            name: "导出所有.csv",
            prefixIcon: "vxe-icon-download",
            visible: true,
            disabled: false,
          },
        ],
      ],
    },
    visibleMethod({ options, column }) {
      // 示例：只有 name 列允许操作，清除按钮只能在 age 才显示
      // 显示之前处理按钮的操作权限
      const isDisabled = false;
      const isVisible = true;
      options.forEach((list) => {
        list.forEach((item) => {
          if (item.code === "copy") {
            item.disabled = isDisabled;
          }
          if (item.code === "clear") {
            item.visible = isVisible;
          }
        });
      });
      return true;
    },
  },
});
</script>
    
<style scoped>
</style>