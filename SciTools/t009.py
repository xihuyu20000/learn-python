from simhash import Simhash

def calculate_similarity(sentence1, sentence2):
    # 创建Simhash对象
    hash1 = Simhash(sentence1)
    hash2 = Simhash(sentence2)

    # 计算汉明距离
    distance = hash1.distance(hash2)

    # 设置阈值，可以根据需要调整
    threshold = 3

    # 判断相似度
    similarity = 1 - distance / threshold if distance <= threshold else 0
    return similarity

# 示例
sentence1 = "This is a sample sentence for testing."
sentence2 = "This is a sample sentence for evaluation."

similarity = calculate_similarity(sentence1, sentence2)
print(f"句子相似度：{similarity}")
