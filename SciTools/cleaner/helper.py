import secrets
import uuid
from typing import List, Set, Dict

import jieba
import pandas as pd
from datasketch import MinHashLSH, MinHash
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from zhon.hanzi import punctuation

class Utils:
    @staticmethod
    def resort_columns(old_names:List[str], new_names:List[str]):
        """
        新插入的列，位于原有列的后面。
        新的列名，是原列名后面加上了“-new”。其他格式不支持
        """
        for new1 in new_names:
            old_names.remove(new1)

        for new1 in new_names:
            i = old_names.index(new1[:new1.rfind('-')])
            old_names.insert(i + 1, new1)

        return old_names

    @staticmethod
    def calculate_cosine_similarity(text1: str, text2: str):
        """
        夹角余弦
        """
        vectorizer = CountVectorizer()
        corpus = [text1, text2]
        vectors = vectorizer.fit_transform(corpus)
        similarity = cosine_similarity(vectors)
        return similarity[0][1]


    @staticmethod
    def calculate_jaccard_similarity(threshold, l1, sentences) ->Dict[int, float]:
        """
        threshold 在 [0.0, 1.0]
        """
        set1 = set(l1)
        result = {}
        for index, l2 in enumerate(sentences):
            set2 = set(l2)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            if union == 0:
                return 0
            if union:
                val = intersection / union
                if val >= threshold:
                    result[index] = val
        return result

    @staticmethod
    def generate_random_color():
        """
        生成任意颜色
        """
        red = secrets.randbelow(256)
        green = secrets.randbelow(256)
        blue = secrets.randbelow(256)
        # return red, green, blue

        red = str(hex(red))[-2:].replace('x', '0').upper()
        green = str(hex(green))[-2:].replace('x', '0').upper()
        blue = str(hex(blue))[-2:].replace('x', '0').upper()
        return '#'+red+green+blue

    @staticmethod
    def has_Chinese_or_punctuation(ws):
        return Utils.has_Chinese(ws) or Utils.has_punctuation(ws)

    @staticmethod
    def has_Chinese(ws):
        return any([True if '\u4e00' <= w <= '\u9fff' else False for w in jieba.lcut(ws)])

    @staticmethod
    def has_punctuation(ws):
        # 中文符号
        return any([True if w in punctuation else False for w in jieba.lcut(ws)])



    array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"
             ]
    @staticmethod

    def uuid8():
        id = str(uuid.uuid4()).replace("-", '')  # 注意这里需要用uuid4
        buffer = []
        for i in range(0, 8):
            start = i * 4
            end = i * 4 + 4
            val = int(id[start:end], 16)
            buffer.append(Utils.array[val % 62])
        return "".join(buffer)
class Minhash:
    """
    大数据量，太慢了，需要优化
    """
    def create_minhash(self, data):
        minhash = MinHash(num_perm=128)  # num_perm 是哈希函数的数量，可以根据需要调整
        for d in data:
            minhash.update(d.encode('utf8'))
        return minhash

    def run(self, threshold, original, sentences):
        # 创建 MinHash 对象并插入到 LSH 中
        self.lsh = MinHashLSH(threshold=threshold, num_perm=128)  # threshold 是相似度阈值，可以根据需要调整

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
        # print(pairs)
        return  pairs


class Parser:
    """
    导出txt时，文件末尾多2个空行
    """
    CORE_ITEMS = ('RT'  # 文献类型
                  , 'A1'  # 作者
                  , 'AD'  # 工作单位
                  , 'T1'  # 题名
                  , 'JF'  # 来源
                  , 'YR'  # 出版年
                  , 'FD'  # 出版日期
                  , 'K1'  # 关键词
                  , 'AB'  # 摘要
                  )

    @staticmethod
    def parse_cnki(filenames) -> DataFrame:
        """
        解析cnki的refworks格式的数据
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:

                values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '',
                          'FD': '',
                          'K1': '',
                          'AB': ''}
                for linone, line in enumerate(f.readlines()):
                    # 前2个字母是具体的key
                    name = line[:2].strip()
                    if name in Parser.CORE_ITEMS:
                        values[name] = line[2:].strip()

                    # 空行，表示上一条结束，新的一条开始
                    if len(line.strip()) == 0:
                        if values and len(values['RT']) > 0:
                            ds.append(values)
                        # 每次初始化数据

                        values = {'RT': '', 'A1': '', 'AD': '', 'T1': '', 'JF': '', 'YR': '', 'FD': '',
                                  'K1': '',
                                  'AB': ''}

        df = pd.DataFrame(ds, dtype='object')
        return df
    @staticmethod
    def parse_wos(filenames):
        """
        解析wos的数据
        ER记录结束
        """
        ds = []
        if isinstance(filenames, str):
            filenames = [filenames]
        # 字段说明参考https://www.jianshu.com/p/964f3e44e431

        for filename in filenames:
            with open(filename, encoding='utf-8') as f:
                flags = ['PT','AU','AF','BA','BF','CA','GP','BE','TI','SO','SE','BS','LA','DT','CT','CY','CL'
                    ,'SP','AB','C1','C3','RP','EM','RI','OI','CR','NR','TC','Z9','U1','U2','PU','PI','PA'
                    ,'BN','PY','BP','EP','DI','PG','WC','WE','SC','GA','UT','OA','DA','DE','SN','J9','JI','VL','AR','ID','EI'
                    ,'PD','IS','FU','FX','PM','SU','SI','EA','HO','D2','PN'
                    ,'ER','EF']
                lines = [line.rstrip() for line in f.readlines() if line.rstrip()]

                flag = ''
                record = {}
                for line in lines[2:]:
                    start = line[:2]
                    if start in flags:
                        flag = start
                        # 是否记录结束
                        if flag == 'ER':
                            if record:
                                ds.append(record)
                            record = {}
                            continue
                        # 文件结束
                        elif flag =='EF':
                            if record:
                                ds.append(record)
                            break
                        # 新的字段开始
                        record[flag] = [line[2:]]
                    elif start.strip()=='':
                        # 还是属于上一个字段的内容
                        record[flag].append(line[3:])
                    else:
                        raise Exception('出现新的字段类型 '+flag)
        print(len(ds))


if __name__ == '__main__':
    Parser.parse_wos('../files/WOS-NLP-1000.txt')