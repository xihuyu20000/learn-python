import request from "../utils/request";
// 表格
export function detail_table() {
  return request.get("/detail_table");
}

// 历年发文量
export function freq_yearly() {
  return request.get("/freq_yearly");
}

// 累计历年发文量
export function acc_freq_yearly() {
  return request.get("/acc_freq_yearly");
}
// 混合累计历年发文量
export function acc_freq_yearly2() {
  return request.get("/acc_freq_yearly2");
}

// 作者发文量
export function freq_authors() {
  return request.get("/freq_authors");
}

// 共现关键词
export function co_kws() {
  return request.get("/co_kws");
}
