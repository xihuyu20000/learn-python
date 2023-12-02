<template>
  <div style="width: 150px; height: 100vh">
    <el-collapse accordion v-model="activePane" @change="changeCollapse">
      <el-collapse-item
        :name="index"
        v-for="(styleList, seriealName, index) in chartStyles"
        :key="index"
      >
        <template #title> <el-icon></el-icon>{{ seriealName }} </template>
        <div class="big-box">
          <div
            class="box"
            v-for="(chart, i) in styleList"
            :key="i"
            @dblclick="choose_chart_style($event, chart)"
          >
            <img
              draggable="true"
              src="../../assets/1.jpg"
              :title="chart.title"
            />
            <span
              class="title"
              :style="{
                color:
                  mainStore.get_current_chartstyle_index === chart.cno
                    ? 'red'
                    : '',
              }"
              >{{ chart.name }}</span
            >
          </div>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>
    
<script setup>
import { useMainStore } from "../../store";
import { VXETable } from "vxe-table";
import { onMounted } from "vue";
// 数据存储对象
const mainStore = useMainStore();

// 选中图表类型
const chartStyles = ref({
  折线图: [
    {
      cno: 1001,
      name: "基础折线图",
      pic: "../../../../assets/1.jpg",
      type: "line",
      title: "图片说明",
      color: "",
    },
    {
      cno: 1002,
      name: "基础面积图",
      pic: "@/assets/1.jpg",
      type: "line",
      title: "图片说明",
      color: "",
    },
    {
      cno: 1003,
      name: "折叠图堆叠",
      pic: "@/assets/1.jpg",
      type: "line",
      title: "图片说明",
      color: "",
    },
    {
      cno: 1004,
      name: "堆叠面积图",
      pic: "@/assets/1.jpg",
      type: "line",
      title: "图片说明",
      color: "",
    },
  ],
  柱状图: [
    {
      cno: 2001,
      name: "基础折线图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 2002,
      name: "基础面积图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 2003,
      name: "折叠图堆叠",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 2004,
      name: "堆叠面积图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
  ],
  饼图: [
    {
      cno: 3001,
      name: "基础折线图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 3002,
      name: "基础面积图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 3003,
      name: "折叠图堆叠",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
    {
      cno: 3003,
      name: "堆叠面积图",
      pic: "../../assets/1.jpg",
      type: "line",
      title: "图片说明",
    },
  ],
  面积图: [],
  环饼图: [],
  散点图: [],
  雷达图: [],
  雷达图: [],
  树形图: [],
  关系图: [],
});
// 选中图表面板
const activePane = ref("0");
// 改变图表面板
function changeCollapse(index) {
  activePane.value = index;
  mainStore.save_active_chart_collapse_item(index);
}
// 改变图表类型
function choose_chart_style(event, chart) {
  mainStore.save_current_chartstyle_index(chart.cno);
  //改变选中图片的背景色
  for (let k in chartStyles.value) {
    let charts = chartStyles.value[k];
    charts.forEach((item) => {
      item.color = "";
    });
  }
  chart.color = "red";
  VXETable.modal.message({
    content: "选中图表——" + chart.name,
    status: "success",
  });
}

onMounted(() => {
  // 激活面板
  activePane.value = mainStore.get_active_chart_collapse_item;
});
</script>
    
<style lang="scss" >
.el-collapse-item__header {
  height: 25px;
  background-color: #faebeb;
  font-size: 1em;
}
.el-collapse-item__content {
  padding-bottom: 0px;
}
.big-box {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  flex-wrap: wrap;
  .box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 60px;
    .title {
      font-size: 0.7em;
    }

    img {
      width: 30px;
      height: 30px;
      vertical-align: text-bottom;
    }
    img:hover {
      cursor: pointer;
    }
  }
}
</style>