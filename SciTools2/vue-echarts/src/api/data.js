import { get, post } from "../utils/request";

// 合并数据文件
export function combine_datafiles(data) {
  return post("/combine_datafiles", data);
}
// 显示所有数据文件
export function list_datafiles() {
  return get("/list_datafiles");
}

// 查询配置信息
export function get_config_datadir() {
  return get("/get_config_datadir");
}
// 保存配置信息
export function save_config(data) {
  return post("/save_config", data);
}
// 表格
export function detail_table(style, index) {
  return get("/detail_table/" + style + "/" + index);
}

// 历年发文量
export function freq_yearly() {
  return get("/freq_yearly");
}

// 累计历年发文量
export function acc_freq_yearly() {
  return get("/acc_freq_yearly");
}
// 混合累计历年发文量
export function acc_freq_yearly2() {
  return get("/acc_freq_yearly2");
}

// 作者发文量
export function freq_authors() {
  return get("/freq_authors");
}

// 共现关键词
export function co_kws() {
  return get("/co_kws");
}
