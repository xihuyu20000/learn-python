# from cleaner.clean import Utils
# a = Utils.calculate_jaccard_similarity(['啊啊','不不不','大是大非'], ['啊啊','不不不','大是大非'])
# print(a)


from datasketch import MinHash, MinHashLSH
# 创建一个 MinHash 对象
# def create_minhash(data):
#     minhash = MinHash(num_perm=128)  # num_perm 是哈希函数的数量，可以根据需要调整
#     for d in data:
#         minhash.update(d.encode('utf8'))
#     return minhash
# # 创建一些示例数据（中文长句子）
# sentences = [
#     "最爱听音乐是我放松心情",
#     "听音乐是我放松心情的爱"
# ]
#
# # 创建 MinHash 对象并插入到 LSH 中
# lsh = MinHashLSH(threshold=0.5, num_perm=128)  # threshold 是相似度阈值，可以根据需要调整
#
# for idx, sentence in enumerate(sentences):
#     minhash = create_minhash(list(sentence))
#     lsh.insert(idx, minhash)
# # 查找相似的集合
# query_minhash = create_minhash(list('听音乐是我放松心情的最爱'))
# results = lsh.query(query_minhash)
# # 输出相似度分数
# for result in results:
#     minhash = create_minhash(list(sentences[result]))
#     jaccard_similarity = query_minhash.jaccard(minhash)
#     print(f"与 sentence 相似的句子 {result} 的相似度分数为: {jaccard_similarity}")
#

class Minhash:
    def create_minhash(self, data):
        minhash = MinHash(num_perm=128)  # num_perm 是哈希函数的数量，可以根据需要调整
        for d in data:
            minhash.update(d.encode('utf8'))
        return minhash
    def __init__(self, threshold):
        # 创建 MinHash 对象并插入到 LSH 中
        self.lsh = MinHashLSH(threshold=threshold, num_perm=128)  # threshold 是相似度阈值，可以根据需要调整

    def run(self, original, sentences):

        for idx, sentence in enumerate(sentences):
            minhash = self.create_minhash(list(sentence))
            self.lsh.insert(idx, minhash)
        # 查找相似的集合
        query_minhash = self.create_minhash(list(original))
        results = self.lsh.query(query_minhash)
        # 输出相似度分数
        pairs = {}
        for result in results:
            minhash = self.create_minhash(list(sentences[result]))
            jaccard_similarity = query_minhash.jaccard(minhash)
            # print(f"与 sentence 相似的句子 {result} 的相似度分数为: {jaccard_similarity}")
            pairs[result] = jaccard_similarity
        print(pairs)
        return  pairs
# 创建一些示例数据（中文长句子）
sentences = [
    '',
    "最爱听音乐是我放松心情",
    "听音乐是我放松心情的爱",
    "听音乐是我放松心情的"
]

minhash = Minhash(0.1)
minhash.run('听音乐是我放松心情的爱', sentences)