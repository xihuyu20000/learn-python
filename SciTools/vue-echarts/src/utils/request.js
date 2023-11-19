import axios from "axios";

const service = axios.create({
  baseURL: "/api", // url = base url + request url
  timeout: 6000, // request timeout
  headers: {
    "Content-Type": "application/json; charset=utf-8",
  },
});

// http request拦截器
service.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    config.headers.Authorization = "Bearer " + localStorage.getItem("token");
    return config;
  },
  function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

service.interceptors.response.use(
  function (response) {
    // 对响应数据做点什么
    return response;
  },
  function (error) {
    // 对响应错误做点什么
    if (error.response.status === 401) {
      // 统一处理 401 错误
      alert("请重新登录");
      return Promise.reject(error);
    }
    return Promise.reject(error);
  }
);

export default service;
