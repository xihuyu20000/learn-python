import collections

import strenum

ActionItem = collections.namedtuple('ActionItem', ['id', 'en', 'cn'])
class Actions:



    parse_cnki = ActionItem('parse_cnki', 'parse cnki', '解析知网')
    parse_weipu = ActionItem('parse_weipu', 'parse weipu', '解析维普')
    parse_wanfang = ActionItem('parse_wanfang', 'parse wanfang', '解析万方')
    parse_csv = ActionItem('parse_csv', 'parse csv', '解析CSV')
    parse_excel = ActionItem('parse_excel', 'parse excel', '解析excel')
    parse_pickle = ActionItem('parse_pickle', 'parse pickle', '解析pickle')
    parse_cnki_patent = ActionItem('parse cnki patent', 'parse_cnki_patent', '解析知网专利')
    parse_wos = ActionItem('parse_woshi', 'parse wos', '解析wos')

    remove_rows = ActionItem('remove_rows', 'remove rows', '删除行')
    remove_cols = ActionItem('remove_cols', 'remove cols', '删除列')


    replace_value = ActionItem('replace_value', 'replace value', '替换值')
    rename_cols = ActionItem('rename_cols', 'rename cols', '重命名')
    modify_value = ActionItem('modify_value', 'modify value', '修改值')
    copy_column = ActionItem('copy_column', 'copy column', '复制列')
    combine_synonym = ActionItem('combine_synonym', 'combine synonym', '合并同义词')
