<template>
  <!-- 标题 -->
  <div style="margin-bottom: 10px">
    <vxe-switch
      v-model="newoption.showingTitle"
      size="mini"
      @change="changeShowingTile"
    ></vxe-switch
    >标题
    <div v-show="newoption.showingTitle">
      <vxe-textarea
        v-model="newoption.titleText"
        placeholder=""
        size="mini"
      ></vxe-textarea>
      <div style="display: flex">
        <span>大小</span
        ><vxe-input
          v-model="newoption.titleFontSize"
          type="number"
          min="8"
          max="80"
          placeholder="字体大小"
          style="width: 100px"
          size="mini"
        ></vxe-input>
      </div>
      <div style="display: flex">
        <span>颜色</span>
        <el-color-picker
          v-model="newoption.titleColor"
          show-alpha
          :predefine="predefineColors"
          size="small"
        />
      </div>
    </div>
  </div>

  <!-- 图例 -->
  <div style="margin-bottom: 10px">
    <vxe-switch
      v-model="newoption.showingLegend"
      size="mini"
      @change="changeShowingLegend"
    ></vxe-switch
    >图例
    <div v-show="newoption.showingLegend">aasdfadf</div>
  </div>
</template>
    
<script setup>
import { useMainStore } from "@/store";
import { onMounted } from "vue";
// 数据存储对象
const mainStore = useMainStore();
// 配置对象
const newoption = ref({
  // 是否显示标题
  showingTitle: true,
  // 标题内容
  titleText: "",
  // 标题字体大小
  titleFontSize: 16,
  // 标题颜色
  titleColor: "",
  // 是否显示图例
  showingLegend: true,
});

// 改变
function changeShowingTile() {
  newoption.showingTitle = !newoption.showingTitle;
}
function changeShowingLegend() {
  newoption.showingLegend = !newoption.showingLegend;
}
const predefineColors = ref([
  "#ff4500",
  "#ff8c00",
  "#ffd700",
  "#90ee90",
  "#00ced1",
  "#1e90ff",
  "#c71585",
  "rgba(255, 69, 0, 0.68)",
  "rgb(255, 120, 0)",
  "hsv(51, 100, 98)",
  "hsva(120, 40, 94, 0.5)",
  "hsl(181, 100%, 37%)",
  "hsla(209, 100%, 56%, 0.73)",
  "#c7158577",
]);

watch(
  () => newoption,
  () => {
    let oldoption = mainStore.get_current_chart_option;
    // 是否显示标题
    oldoption.title.show = newoption.value.showingTitle;
    // 标题的内容
    oldoption.title.text = newoption.value.titleText;
    // 标题的字体大小
    oldoption.title.textStyle.fontSize = newoption.value.titleFontSize;
    // 标题的颜色
    oldoption.title.textStyle.color = newoption.value.titleColor;
    // 是否显示图例
    // oldoption.legend.show = newoption.value.showingLegend;
    // 保存当前图表配置
    mainStore.save_current_chart_option(oldoption);
  },
  {
    deep: true,
    immediate: true,
  }
);

onMounted(() => {
  let oldoption = mainStore.get_current_chart_option;
  console.log("加载默认配置", oldoption.title.show, oldoption.title.text);
  newoption.value.showingTitle = oldoption.title.show;
  newoption.value.titleText = oldoption.title.text;
  // newoption.value.titleFontSize = oldoption.title.textStyle.fontSize;
});
</script>
    
<style lang="scss" scoped>
</style>
