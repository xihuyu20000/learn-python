export function deepMerge(target, source) {
  // 判断类型
  const isObject = (obj) => obj && typeof obj === "object";

  // 如果目标或源不是对象，则直接返回源
  if (!isObject(target) || !isObject(source)) {
    return source;
  }

  // 遍历源对象的属性
  for (const key in source) {
    if (source.hasOwnProperty(key)) {
      // 如果目标对象中没有这个属性，直接复制
      if (!target.hasOwnProperty(key)) {
        target[key] = source[key];
      } else {
        // 如果目标对象中有这个属性，递归调用深度合并
        target[key] = deepMerge(target[key], source[key]);
      }
    }
  }

  return target;
}
