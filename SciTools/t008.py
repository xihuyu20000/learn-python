from cleaner.helper import Utils

result = Utils.calculate_jaccard_similarity(0.001, {'崔彩贤', '伊雅楠', '远佳怡', '李玲玲', '沈霖', '王忠港'}, [set(), {'崔彩贤', '伊雅楠', '远佳怡', '沈霖', '王忠港'}, {'叶靓俏', '赵文武', '尹彩春'}, {'郑泽宇'}, {'肖镇江', '章胜平', '冯靖', '宋志刚'}, {'李元文', '任雪雯', '李纬', '邓宇童', '胡博', '肖飞', '蔡玲玲'}, {'吴群', '彭山桂', '杨一鸣', '王健'}])

print(result)