from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 示例文本数据
documents = [
    "zhang san 1",
    "san zhang 11"
]

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 将文本数据转化为TF-IDF向量
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# 计算文档之间的余弦相似性
similarity_matrix = cosine_similarity(tfidf_matrix)

# 打印相似性矩阵
print("Similarity Matrix:")
print(similarity_matrix)

# 查找最相似的文档
most_similar = similarity_matrix.argsort()[:, -2]

# 打印最相似的文档
for i, doc_index in enumerate(most_similar):
    print(f"Document {i} is most similar to Document {doc_index} (Similarity Score: {similarity_matrix[i][doc_index]:.2f})")