"""

"""
from typing import List



if __name__ == '__main__':
    aa = [1,2,3,4,5]


    prev = aa[0]
    result = [prev]
    for i in range(1,len(aa)):
        aa[i] = aa[i]+prev
        prev = aa[i]
        result.append(prev)
    print(result)