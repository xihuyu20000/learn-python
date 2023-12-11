import collections
import itertools
import os
import re
import secrets
import uuid
from typing import List, Dict
import dbm
import jieba
from log import logger
import numpy as np
import pandas as pd
import wmi
from blinker import signal
from strenum import StrEnum
from zhon.hanzi import punctuation


class ssignal:
    stack_change = signal('stack_change')
    info = signal('info')
    error = signal('error')
    finish = signal('finish')
    set_clean_dataset = signal('set_clean_dataset')


class Cfg:
    workspace = os.path.abspath(os.curdir)
    datafiles = os.path.join(workspace, 'datafiles')
    dicts = os.path.join(workspace, 'dicts')


    table_header_bgcolor = 'lightblue'
    seperator = 'seperator'
    csv_seperator = 'csv_seperator'
    stopwords_file = '停用词表.txt'
    synonyms_file = '合并词表.txt'
    def __init__(self):
        self.db = os.path.join(os.path.abspath(os.curdir), 'sci.db')
        if not os.path.exists(self.db):
            with dbm.open(self.db, 'c') as f:
                f['table_header_bgcolor'] = 'lightblue'
                f['seperator'] = ';'
                f['csv_seperator'] = ','
                f['stopwords_file'] = os.path.join(os.path.abspath(Cfg.dicts), '停用词表')
                f['synonyms_file'] = os.path.join(os.path.abspath(Cfg.dicts), '同义词表')

    def set(self, k, v):
        file = dbm.open(self.db, 'c')
        file[k] = bytes(v, encoding='utf-8')
        file.close()

    def get(self, k):
        file = dbm.open(self.db, 'c')
        v = file[k]
        file.close()
        return str(v,'utf-8')




class FileFormat(StrEnum):
    CNKI = 'CNKI'
    WOS = 'WOS'
    CSV = 'CSV'
    EXCEL = 'EXCEL'
    PICKLE = 'PICKLE'
    PARQUET = 'PARQUET'


# -*- codeding = uft-8 -*-


class Md5:
    @staticmethod
    def int2bin(n, count=24):
        return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])

    class MD5Algo(object):
        # 初始化密文
        def __init__(self, message):
            self.message = message
            self.ciphertext = ""

            self.A = 0x67452301
            self.B = 0xEFCDAB89
            self.C = 0x98BADCFE
            self.D = 0x10325476
            self.init_A = 0x67452301
            self.init_B = 0xEFCDAB89
            self.init_C = 0x98BADCFE
            self.init_D = 0x10325476
            '''
            self.A = 0x01234567
            self.B = 0x89ABCDEF
            self.C = 0xFEDCBA98
            self.D = 0x76543210
             '''
            # 设置常数表T
            self.T = [0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE, 0xF57C0FAF, 0x4787C62A, 0xA8304613, 0xFD469501,
                      0x698098D8, 0x8B44F7AF, 0xFFFF5BB1, 0x895CD7BE, 0x6B901122, 0xFD987193, 0xA679438E, 0x49B40821,
                      0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA, 0xD62F105D, 0x02441453, 0xD8A1E681, 0xE7D3FBC8,
                      0x21E1CDE6, 0xC33707D6, 0xF4D50D87, 0x455A14ED, 0xA9E3E905, 0xFCEFA3F8, 0x676F02D9, 0x8D2A4C8A,
                      0xFFFA3942, 0x8771F681, 0x6D9D6122, 0xFDE5380C, 0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70,
                      0x289B7EC6, 0xEAA127FA, 0xD4EF3085, 0x04881D05, 0xD9D4D039, 0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665,
                      0xF4292244, 0x432AFF97, 0xAB9423A7, 0xFC93A039, 0x655B59C3, 0x8F0CCC92, 0xFFEFF47D, 0x85845DD1,
                      0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1, 0xF7537E82, 0xBD3AF235, 0x2AD7D2BB, 0xEB86D391]
            # 循环左移位数
            self.s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                      5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                      4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                      6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
            self.m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                      1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12,
                      5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2,
                      0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9]

        # 附加填充位
        def fill_text(self):
            for i in range(len(self.message)):
                c = Md5.int2bin(ord(self.message[i]), 8)
                self.ciphertext += c

            if (len(self.ciphertext) % 512 != 448):
                if ((len(self.ciphertext) + 1) % 512 != 448):
                    self.ciphertext += '1'
                while (len(self.ciphertext) % 512 != 448):
                    self.ciphertext += '0'

            length = len(self.message) * 8
            if (length <= 255):
                length = Md5.int2bin(length, 8)
            else:
                length = Md5.int2bin(length, 16)
                temp = length[8:12] + length[12:16] + length[0:4] + length[4:8]
                length = temp

            self.ciphertext += length
            while (len(self.ciphertext) % 512 != 0):
                self.ciphertext += '0'

        # 分组处理（迭代压缩）
        def circuit_shift(self, x, amount):
            x &= 0xFFFFFFFF
            return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

        def change_pos(self):
            a = self.A
            b = self.B
            c = self.C
            d = self.D
            self.A = d
            self.B = a
            self.C = b
            self.D = c

        def FF(self, mj, s, ti):
            mj = int(mj, 2)
            temp = self.F(self.B, self.C, self.D) + self.A + mj + ti
            temp = self.circuit_shift(temp, s)
            self.A = (self.B + temp) % pow(2, 32)
            self.change_pos()

        def GG(self, mj, s, ti):
            mj = int(mj, 2)
            temp = self.G(self.B, self.C, self.D) + self.A + mj + ti
            temp = self.circuit_shift(temp, s)
            self.A = (self.B + temp) % pow(2, 32)
            self.change_pos()

        def HH(self, mj, s, ti):
            mj = int(mj, 2)
            temp = self.H(self.B, self.C, self.D) + self.A + mj + ti
            temp = self.circuit_shift(temp, s)
            self.A = (self.B + temp) % pow(2, 32)
            self.change_pos()

        def II(self, mj, s, ti):
            mj = int(mj, 2)
            temp = self.I(self.B, self.C, self.D) + self.A + mj + ti
            temp = self.circuit_shift(temp, s)
            self.A = (self.B + temp) % pow(2, 32)
            self.change_pos()

        def F(self, X, Y, Z):
            return (X & Y) | ((~X) & Z)

        def G(self, X, Y, Z):
            return (X & Z) | (Y & (~Z))

        def H(self, X, Y, Z):
            return X ^ Y ^ Z

        def I(self, X, Y, Z):
            return Y ^ (X | (~Z))

        def group_processing(self):
            M = []
            for i in range(0, len(self.ciphertext), 512):
                # 获取当前分组
                current_group = self.ciphertext[i:i + 512]

                # 处理当前分组...
                # ...

                # 更新 init_A、init_B、init_C、init_D
                self.init_A = self.A
                self.init_B = self.B
                self.init_C = self.C
                self.init_D = self.D

                for j in range(0, 512, 32):
                    num = ""
                    # 获取每一段的标准十六进制形式
                    for k in range(0, len(current_group[j:j + 32]), 4):
                        temp = current_group[j:j + 32][k:k + 4]
                        temp = hex(int(temp, 2))
                        num += temp[2]
                    # 对十六进制进行小端排序
                    num_tmp = ""
                    for k in range(8, 0, -2):
                        temp = num[k - 2:k]
                        num_tmp += temp

                    num = ""
                    for k in range(len(num_tmp)):
                        num += Md5.int2bin(int(num_tmp[k], 16), 4)
                    M.append(num)
            # print(M)

            for j in range(0, 16, 4):
                self.FF(M[self.m[j]], self.s[j], self.T[j])
                self.FF(M[self.m[j + 1]], self.s[j + 1], self.T[j + 1])
                self.FF(M[self.m[j + 2]], self.s[j + 2], self.T[j + 2])
                self.FF(M[self.m[j + 3]], self.s[j + 3], self.T[j + 3])

            for j in range(0, 16, 4):
                self.GG(M[self.m[16 + j]], self.s[16 + j], self.T[16 + j])
                self.GG(M[self.m[16 + j + 1]], self.s[16 + j + 1], self.T[16 + j + 1])
                self.GG(M[self.m[16 + j + 2]], self.s[16 + j + 2], self.T[16 + j + 2])
                self.GG(M[self.m[16 + j + 3]], self.s[16 + j + 3], self.T[16 + j + 3])

            for j in range(0, 16, 4):
                self.HH(M[self.m[32 + j]], self.s[32 + j], self.T[32 + j])
                self.HH(M[self.m[32 + j + 1]], self.s[32 + j + 1], self.T[32 + j + 1])
                self.HH(M[self.m[32 + j + 2]], self.s[32 + j + 2], self.T[32 + j + 2])
                self.HH(M[self.m[32 + j + 3]], self.s[32 + j + 3], self.T[32 + j + 3])

            for j in range(0, 16, 4):
                self.II(M[self.m[48 + j]], self.s[48 + j], self.T[48 + j])
                self.II(M[self.m[48 + j + 1]], self.s[48 + j + 1], self.T[48 + j + 1])
                self.II(M[self.m[48 + j + 2]], self.s[48 + j + 2], self.T[48 + j + 2])
                self.II(M[self.m[48 + j + 3]], self.s[48 + j + 3], self.T[48 + j + 3])

            self.A = (self.A + self.init_A) % pow(2, 32)
            self.B = (self.B + self.init_B) % pow(2, 32)
            self.C = (self.C + self.init_C) % pow(2, 32)
            self.D = (self.D + self.init_D) % pow(2, 32)

            """
            print("A:{}".format(hex(self.A)))
            print("B:{}".format(hex(self.B)))
            print("C:{}".format(hex(self.C)))
            print("D:{}".format(hex(self.D)))
            """

            answer = ""
            for register in [self.A, self.B, self.C, self.D]:
                if len(hex(register)) != 10:
                    str1 = list(hex(register))
                    str1.insert(2, '0')
                    str2 = ''.join(str1)
                    register = str2[2:]
                else:
                    register = hex(register)[2:]
                for i in range(8, 0, -2):
                    answer += str(register[i - 2:i])

            return answer

    @staticmethod
    def get(msg):

        MD5 = Md5.MD5Algo(msg)
        MD5.fill_text()
        result = MD5.group_processing()
        return result


class Utils:
    @staticmethod
    def resort_columns(old_names: List[str], new_names: List[str]):
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
    def calculate_jaccard_similarity(threshold, l1, sentences) -> Dict[int, float]:
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
        return '#' + red + green + blue
    @staticmethod
    def replace(line, words_dict):
        """
        假设line是'aa;bb;cc;dd'，words_dict是{'aa':1,'cc':2}，返回值是1;bb;2;dd
        :param line:
        :param words_dict:
        :return:
        """
        keys = words_dict.keys()
        words = [str(words_dict[w]) if w in keys else w for w in line.split(Cfg.seperator)]
        return Cfg.seperator.join(words)

    @staticmethod
    def get_from_limit(i: int, arr: List[str], limit: int):
        if limit <= len(arr):
            return arr[i]
        else:
            if i < len(arr):
                return arr[i]
            else:
                return ''

    @staticmethod
    def split_string_by_length(string, length):
        """
        按照数量，拆分字符串
        """
        pattern = f".{{1,{length}}}"
        result = re.findall(pattern, string)
        return result
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
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v",
             "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V",
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


class MachineCode:
    def __init__(self):
        """
        机器码，还有授权文件，还有验证
        """
        self.m_wmi = wmi.WMI()
        self.licence_path = os.path.join(os.path.expanduser('~'), '.licence.abc')

    def __cpu(self):
        cpu_info = self.m_wmi.Win32_Processor()
        if len(cpu_info) > 0:
            return cpu_info[0].ProcessorId
        return ''

    def __mac(self):
        for network in self.m_wmi.Win32_NetworkAdapterConfiguration():
            mac_address = network.MacAddress
            if mac_address != None:
                return mac_address
        return ''

    def __mainboard(self):
        board_info = self.m_wmi.Win32_BaseBoard()
        if len(board_info) > 0:
            return board_info[0].SerialNumber.strip().strip('.')
        return ''

    def get_code(self):
        """
        获得机器码
        """
        combine_str = self.__mac() + self.__cpu() + self.__mainboard()
        combine_byte = combine_str.encode("utf-8")
        return Md5.get(combine_byte).upper()

    def read_licence(self):
        """
        获取授权文件内容
        """

        if os.path.exists(self.licence_path):
            with open(self.licence_path, 'r', encoding='utf-8') as f:
                return ''.join(f.readlines())
        return ''

    def write_licence(self, text):
        """
        写入授权文件
        """
        with open(self.licence_path, 'w', encoding='utf-8') as f:
            f.write(text)


class PandasUtil:
    @staticmethod
    def cocon_matrix(df, col_name, threhold=0, diagonal_values=False):
        """
        共现矩阵
        :param df:
        :param col_name:
        :param threhold:
        :return:
        """
        df2 = df[col_name].str.split(Cfg.seperator)
        # 根据对角线是否有值，决定使用哪个函数
        sfunc = itertools.combinations_with_replacement if diagonal_values else itertools.combinations

        df2 = df2.apply(lambda x: [Cfg.seperator.join(sorted(item)) for item in sfunc(x, 2)])

        total_pairs = collections.defaultdict(int)

        for row in df2:
            for pair in row:
                total_pairs[pair] += 1

        total_pairs = {k: v for k, v in total_pairs.items() if v > threhold}

        total_words = set()
        for k, v in total_pairs.items():
            total_words.update(k.split(Cfg.seperator))

        result = pd.DataFrame(index=list(total_words), columns=list(total_words), dtype=np.uint8)
        for k, v in total_pairs.items():
            ss = k.split(Cfg.seperator)
            i, j = ss[0], ss[1]
            result.loc[i, j] = v
            result.loc[j, i] = v
        result.fillna(0, inplace=True)
        result.reset_index(inplace=False, drop=False)

        return result

    @staticmethod
    def heter_matrix(df, col_name1, col_name2, threshold=0):
        df.fillna('', inplace=True)
        df1 = df[col_name1].str.split(Cfg.seperator)
        df2 = df[col_name2].str.split(Cfg.seperator)

        pair_dict = collections.defaultdict(int)
        for i in range(len(df1)):
            for arr in itertools.product(df1[i], df2[i]):
                pair_dict[Cfg.seperator.join(arr)] += 1

        columns = set()
        index = set()
        for item, v in pair_dict.items():
            arr = str(item).split(Cfg.seperator)
            index.add(arr[0])
            columns.add(arr[1])

        result = pd.DataFrame(columns=list(columns), index=list(index), dtype=np.uint8)

        for item, v in pair_dict.items():
            arr = str(item).split(Cfg.seperator)
            result.loc[arr[0], arr[1]] = v
        result = result.fillna(0).astype(np.uint8)

        # 删除行
        condition = (result < threshold).all(axis=1)
        result = result[~condition]
        # 删除列
        columns_to_remove = result.columns[(result < threshold).all()]
        result = result.drop(columns=columns_to_remove)

        return result
