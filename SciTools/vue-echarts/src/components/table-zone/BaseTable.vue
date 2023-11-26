<template>
  <div style="width: 100%; height: 100%; display: flex">
    <uploaded></uploaded>
    <div style="flex: 1">
      <vxe-grid v-bind="gridOptions" height="auto" ref="edTable">
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
          <vxe-button @click="saveRows">保存</vxe-button>
        </template>
      </vxe-grid>
    </div>
  </div>
</template>
    
<script setup>
import Sortable from "sortablejs";
import { onMounted, nextTick, getCurrentInstance } from "vue";
import { detail_table } from "../../api/data";
const edTable = ref(null);

// 统计每一列的空行数量
const countNull = (list, field) => {
  let count = 0;
  list.forEach((item) => {
    if (!item[field] || item[field].replace(/(^\s*)|(\s*$)/g, "").length <= 0) {
      count += 1;
    }
  });
  return count;
};
// 拖拽列
// 列拖拽
let oldList = [],
  newList = [];
const columnDrop = () => {
  const $table = edTable.value;
  nextTick(() => {
    let sortable2 = Sortable.create(
      $table.$el.querySelector(
        ".body--wrapper>.vxe-table--header .vxe-header--row"
      ),
      {
        handle: ".vxe-header--column",
        onEnd: ({ item, newIndex, oldIndex }) => {
          const { fullColumn, tableColumn } = $table.getTableColumn();
          const targetThElem = item;
          const wrapperElem = targetThElem.parentNode;
          const newColumn = fullColumn[newIndex];
          if (newColumn.fixed) {
            const oldThElem = wrapperElem.children[oldIndex];
            // 错误的移动
            if (newIndex > oldIndex) {
              wrapperElem.insertBefore(targetThElem, oldThElem);
            } else {
              wrapperElem.insertBefore(
                targetThElem,
                oldThElem ? oldThElem.nextElementSibling : oldThElem
              );
            }
            VXETable.modal.message({
              content: "固定列不允许拖动，即将还原操作！",
              status: "error",
            });
            return;
          }
          // 获取列索引 columnIndex > fullColumn
          const oldColumnIndex = $table.getColumnIndex(tableColumn[oldIndex]);
          const newColumnIndex = $table.getColumnIndex(tableColumn[newIndex]);
          // 移动到目标列
          const currRow = fullColumn.splice(oldColumnIndex, 1)[0];
          fullColumn.splice(newColumnIndex, 0, currRow);
          $table.loadColumn(fullColumn);
        },
      }
    );
  });
};
/** 保存 */
const saveRows = () => {
  console.log(edTable.value.getRecordset());
};
const gridOptions = reactive({
  border: true,
  stripe: true,
  showFooter: true,
  autorResize: true,
  showOverflow: true,

  editConfig: {
    trigger: "dblclick",
    mode: "cell",
  },
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
    {
      field: "abs",
      title: "abs",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "authors",
      title: "authors",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "doctype",
      title: "doctype",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "kws",
      title: "kws",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "orgs",
      title: "orgs",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "pubyear",
      title: "pubyear",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "source",
      title: "source",
      sortable: true,
      editRender: { name: "input" },
    },
    {
      field: "title",
      title: "title",
      sortable: true,
      editRender: { name: "input" },
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
          {
            code: "deleteColumn",
            name: "删除列",
            prefixIcon: "vxe-icon-custom-column",
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
          {
            code: "reload",
            name: "刷新表格",
            visible: true,
            disabled: false,
          },
        ],
      ],
    },
  },
  cellStyle: ({ row, rowIndex, column, columnIndex }) => {
    if (columnIndex > 0) {
      if (
        !column.property ||
        row[column.property].replace(/(^\s*)|(\s*$)/g, "").length <= 0
      ) {
        return {
          background: "#fafafa",
        };
      }
    }
  },
  footerCellStyle: () => {
    return {
      "background-color": "#f1f1f1",
    };
  },
  footerMethod: ({ columns, data }) => {
    return [
      columns.map((column, columnIndex) => {
        if (columnIndex === 0) {
          return "空值";
        }
        return countNull(data, column.field);
      }),
    ];
  },
  filters: () => {
    return [];
  },
});

onMounted(() => {
  columnDrop();
});
</script>
    

<style scoped lang="scss">
</style>