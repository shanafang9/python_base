# coding:utf-8

'''isalnum()
s0 = '$#123abc'
s1 = '123abc'
print(s0,s0.isalnum()) # 所有字符都是 数字 或 字母
print(s1,s1.isalnum())
'''

'''isalpha()
s2 = 'abc'
print(s2,s2.isalpha()) # 所有字符都是 字母
'''

'''isdigit()
s3 = '123'
print(s3,s3.isdigit()) # 所有字符都是 数字
'''

'''islower()
s4 = '123ab'
s5 = 'ab'
print(s4,s4.islower()) # 所有 字母 都是小写
print(s5,s5.islower())
'''

'''isupper()
s6 = '123AB'
s7 = 'AB'
print(s6,s6.isupper()) # 所有 字母 都是大写
print(s7,s7.isupper())
'''

'''istitle()
s8 = 'W123er'
s9 = 'Wrt'
print(s8,s8.istitle()) # 所有 单词 都是 首字母大写
print(s9,s9.istitle())
'''

'''isspace()
s10 = ''
s11 = '   '
s12 = '12 3'
print(s10,s10.isspace()) # 所有字符都是 空字符
print(s11,s11.isspace())
print(s12,s12.isspace())
'''

'''填充'''
s = 'win'
# print(s.center(5))
#  win
# print(s.center(6,'*'))
# *win**

# print(s.ljust(5,"*"))
# win**
# print(s.rjust(5,'*'))
# **win

# print(s.zfill(5))  # 将字符串填充到指定长度， 用 '0' zero填充
# 00win


'''去除'''
# s1 = '   op   '
# s2 = '***ihn&&&'
# s3 = '\n*\nih\n'
# print(s1.strip())
# # op
# print(s2.strip('&'))
# # ***ihn
# print(s2.strip('*&'))
# # ihn
# print('lstrip()',s3.lstrip().__repr__())
# print('lstrip()',s3.lstrip())
#
# print('rstrip()',s3.rstrip().__repr__())
# print('rstrip()',s3.rstrip())


'''查找'''
s = 'hello python'
# print(s.count(' '))  # 统计元素出现次数
# 1
# print(s.find('l')) # 按元素 有则返回索引;否则报错 (-1)
# 2
# print(s.rfind('l'))
# 3
# print(s.index('o'))
# 4
# print(s.rindex('o'))
# 10




'''format'''

# print('{0}{1}{0}'.format('hello','world','python'))
# helloworldhello
# print('my name is {name}'.format(name = 'jack'))
# my name is jack

# print('{:>10}'.format('python')) # {':' + '填充符' + '对齐方式' + '指定输出字符长度'}
# '    python'
# print('{:0<10}'.format('python'))
# 'python0000'
print('{:*^9}'.format('python'))
# '**python**'
# '*python**'