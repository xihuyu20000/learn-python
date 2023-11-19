from typing import List, Dict, Any


def acc_sum(bb:List[int])->List[int]:
    """
    对一个list中的元素，逐个累计
    """
    aa = bb.copy()
    prev = aa[0]
    result = [prev]
    for i in range(1,len(aa)):
        aa[i] = aa[i]+prev
        prev = aa[i]
        result.append(prev)
    return result

def init_line_option(title:str, x_category:List[str], y_series:List[Any])->Dict:
    option = {
        'title':{
            'show':True,
            'text':title
        },
        'xAxis': {
            'type': "category",
            'data': x_category,
        },
        'yAxis': {
            'type': "value",
        },
        'series': y_series,
    }
    return option