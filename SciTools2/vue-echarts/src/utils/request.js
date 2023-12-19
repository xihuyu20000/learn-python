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

/**
 * 封装get方法
 * @param url
 * @param data
 * @returns {Promise}
 */
export function get(url, params = {}) {
  // service.defaults.headers = {
  //   "Content-Type": "application/json; charset=utf-8",
  // };
  return new Promise((resolve, reject) => {
    service
      .get(url, {
        params: params,
      })
      .then((response) => {
        resolve(response.data);
      })
      .catch((err) => {
        reject(err);
      });
  });
}

/**
 * 封装post请求
 * @param url
 * @param data
 * @returns {Promise}
 */
export function post(url, data = {}) {
  // service.defaults.headers = {
  //   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  // };
  return new Promise((resolve, reject) => {
    service.post(url, data).then(
      (response) => {
        resolve(response.data);
      },
      (err) => {
        reject(err);
      }
    );
  });
}
