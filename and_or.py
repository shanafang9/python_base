# coding:utf-8

'''
纯 and 语句中，如果一个表达式不为假，那么返回最后一个；如果有一个假那么返回假
纯 or 语句中，只要有一个表达式不为假，那么返回这个表达式的值；只有所有都是假才返回假

（False or 1）  输出1

(1 or False)    输出1

（True or 1）输出前者

(1 or True)   输出前者

（True and 1) 输出后者

(1 and True)    输出后者

（False and 1）输出False

(1 and False)  输出False

'''

'''or'''
# print(False or 1)
# print(1 or False)
# print(True or 1)
# print(1 or True)

'''and'''
# print(False and 1)
# print(1 and False)
# print(True and 1)
# print(1 and True)


'''
不加括号时  and 优先级大于 or

'''

# print(1 or 5 and 4)
# and 优先级较高 ; and 两边为真 返回 右侧 '4'
# 再判断 or ; 1 or 4 两边为真   返回 左侧 '1'

# print((1 or 5) and 4)
# 优先运算括号内 ; or 两边为真 返回 右侧 '1'
# 再判断 and ; 1 and 4 两边为真 返回 左侧 '4'


'''
规律:

# and
只要左边的表达式为真，整个判断的值为 右侧 表达式的值;否则，返回左边表达式的值

# or
只要两边表达式为真，那么整个表达式的值为 左侧 表达式的值
如果 一真一假，返回值为 真值表达式的值
如果 两边都是假，返回 右侧的值

'''

# print(False or 0)
# print(0 or True)
# print(0 and True)
# print(bool(0))
# print(False or 4)


print( 0 or 0 or 4 or 6 or 9)



