# -*- coding:UTF-8 -*-
#! /usr/bin/python3
# 字符串 内建函数
String_a = 'iPhone'
String_b = 'Apple'
# 首字母大写
print('=====首字母大写=====\n注意调用方法：')
print(String_a,'->',str.capitalize(String_a))
print(String_b,'->',String_b.capitalize()) # 注意调用方法
print('=====字符填充=====')
print('填充字符，默认填充空格：',String_a.center(20))# 填充字符
print('左对齐填充',String_b.ljust(20,'-'))# 左对齐填充
print('右对齐填充',String_b.rjust(20,'-'))# 右对齐填充
print('右对齐，前补零：',String_b.zfill(20)) # 返回长度为 width 的字符串，原字符串右对齐，前面填充0
print('=====计算出现次数=====')
print('注意调用方法：\np出现：',String_b.count('p'),'次')# 计算某字符串出现次数
print('p出现：',str.count(String_b,'p'),'次')

# bytes.decode(encoding="utf-8", errors="strict")
# encode(encoding='UTF-8',errors='strict')

String_C = 'a b c d c'
print(String_C.expandtabs(tabsize=8)) # 用制表符扩充???
print('=====查找值的索引=====')
print('查找b的索引，可规定查找区间，存在返回其索引，不存在返回-1：',String_C.find('b',0,5)) # 返回索引,不存在返回-1
print('查找c的索引，可规定查找区间，存在返回其索引，不存在会报错：',String_C.index('c',3,5)) # 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
print('类似于find()函数，从右边开始查找.',String_C.rfind('b',0,5)) # 类似于 find()函数，不过是从右边开始查找.
print('类似于index()函数，从右边开始查找.',String_C.rindex('c'),'\n\b=====判断函数=====') # 类似于 index()，不过是从右边开始..

del String_C;String_c = '1z2y3x4w5v6u'
print('判断是否为仅包含字母和数的非空字符串',String_c.isalnum()) # 判断是否为仅包含字母和数的非空字符串
print('判断是否为仅包含字母的非空字符串',String_c.isalpha()) # 判断是否为仅包含字母的非空字符串
print('如果字符串只包含数字则返回 True 否则返回 False',String_c.isdigit()) # 如果字符串只包含数字则返回 True 否则返回 False.
print('检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false',String_c.isdecimal()) # 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
print('字符串若包含至少一个区分大小写的字符，且所有这些字符都是小写，则返回True',String_c.islower()) # 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回 True
print('字符串若包含至少一个区分大小写的字符，且所有这些字符都是大写，则返回True','AAA'.isupper()) # 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是大写，则返回 True
print('如果字符串中只包含数字字符，则返回 True，否则返回 False',String_c.isnumeric()) # 如果字符串中只包含数字字符，则返回 True，否则返回 False
print('如果字符串中只包含空白，则返回 True，否则返回 False.'," ".isspace()) # 如果字符串中只包含空白，则返回 True，否则返回 False.

String_C = 'today is a perfect good day'
print(String_C.title())
print((String_C.title()).istitle()) # 如果字符串是标题化的(见 title())则返回 True，否则返回 False

print(String_a.join(String_b)) # 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# 返回字符串长度
print(String_b.__len__())
print(len(String_b))
print('aWafAFS2CALjaka'.lower()) # 转换字符串中所有大写字符为小写.
print('aWafAFS2CALjaka'.upper()) # 转换字符串中所有小写字符为大写.
print('aWafAFS2CALjaka'.swapcase()) # 转换字符串中所有大小写互换.
print('=====首末字符删除=====')
print('aaaaaasaaaaaa'.lstrip('a')) # 截掉字符串左边的空格或指定字符.
print('aaaaaasaaaaaa'.rstrip('a')) # 删除字符串字符串末尾的空格或指定字符.
print('aaaaaasaaaaaa'.strip('a')) # 在字符串上执行 lstrip()和 rstrip()
print('=====最大最小字母=====')
print(max(String_b)) # 返回字符串 str 中最大的字母。
print(min(String_b)) # 返回字符串 str 中最小的字母。
print('AA12AA23AA3fjlAA12flA'.replace('AA','???',3)) # 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
print('AA12AA23AA3fjlAA12flA'.split('AA',2)) # 次数可用num=string.count(str))，以 str 为分隔符截取字符串，num指定截取个数
print(String_c.startswith('1',0,5)) # 检查字符串是否是以 输入参数 开头，是则返回 True，否则返回 False。beg和end指定范围内检查。
