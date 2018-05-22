#coding:utf-8


# print('输入两个数字，依次返回：m与n的和、m与n积、m的n次方、m除n的余数、m与n中较大的数')
# i = 1
# while True:
# 	m = input('请输入第一个数字：')
# 	n = input('请输入第二个数字：')
# 	if m.isdigit() and n.isdigit():
# 		break
# 	else:
# 		if i == 1:
# 			print('请输入数字。')
# 			i += 1
# 		elif i < 4:
# 			print('知道数字是啥吗？')
# 			i += 1
# 		else:
# 			print('w q n m l g b')
# 			i += 1
# m = int(m)
# n = int(n)
# list = []
# list.append(str(m+n))
# list.append(str(m*n))
# list.append(str(m**n))
# list.append(str(m%n))
# if m > n:
#     list.append(str(m))
# else:
#     list.append(str(n))
# print(" ".join(tuple(list)))


'''完美立方数
n = int(input())  # n范围内的立方数

list_cube = [0]  # 用于存储立方数的列表
for i in range(1, n + 1):
    list_cube.append(i * i * i)

for a in range(6, n + 1):
    for b in range(2, a - 1):
        if list_cube[a] < (list_cube[b] + list_cube[b + 1] + list_cube[b + 2]):
            break
        for c in range(b + 1, a):
            if list_cube[a] < (list_cube[b] + list_cube[c] + list_cube[c + 1]):
                break
            for d in range(c + 1, a):
                if list_cube[a] == (list_cube[b] + list_cube[c] + list_cube[d]):
                    print("Cube=%d,Tripe=(%d,%d,%d)" % (a, b, c, d))

'''


'''汇率转换
import re
# money = input().lower()
money = 'rmb5'
tmp = re.findall(r'usd(\d+)|rmb(\d+)',money)
print(tmp)
if len(tmp)==0 :
    print('bad')
else:
	print(tmp)
	print('win')
print(type(tmp))
t = tmp[0]
# #===去除元组里的空元素
# t = list(t)
# print(t)
# t1 = []
# for i in range(len(t)):
# 	if t[i] != '':
# 		t1.append(t[i])
# print(t1)

t = t[1]
try:
    num=float(t)
    if 'usd' in tmp:
        print('RMB%.2f'%(num*6.78))
    else:
        print('USD%.2f'%(num/6.78))
except:
    print('wrong')

'''


'''查询英文月份简写
#方法1
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
l = months.split('.')
# print(l)

n = input('请输入月份：')

if n.isdigit() and 1<= int(n) <=12:

	print(l[int(n)-1])
else:
	print('输入错误')


#方法2
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
n = input()

#（每个月份的数字-1）*4就是这个月份简写的开始索引，截取4个字符
index = (int(n)-1)*4
month = months[index: index + 4] # 切片
print(month)
'''


'''凯撒密码

# 原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# str_y = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# str_m = ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
str_y = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_m = 'DEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABC'
s = input('请输入语句：')
s = s.upper()
out_s = ''
for i in s:
	if i == ' ':
		out_s = out_s + ' '
	else:
		index = str_m.find(i)
		out_s = out_s + str_m[index+3]
print(out_s.lower())

'''


'''完美立方

for i in range(258,1000):
	a = i//100
	b = (i-a*100)//10
	c = (i-a*100-b*10)
	# e = a**3
	# f = b**3
	# g = c**3
	if a**3 + b**3 + c**3 == i:
		print(i)

import math
list = []
for i in range(100, 1000):
    x = math.floor(i / 100) # 向下取整
    y = math.floor((i - x * 100) / 10)
    z = i - math.floor(i / 10) * 10
    if i == x ** 3 + y ** 3 + z ** 3:
        list.append(str(i))
print(", ".join(tuple(list)))

'''


'''字符串运用

str_s = "All that doth flow we cannot liquid name Or else would fire and water be the same;But that is liquid which is moist and wet Fire that property can never get. Then 'tis not cold that doth the fire put out But 'tis the wet that makes it die, no doubt. "
print(len(str_s))
print(str_s.startswith('All'))
print(str_s.endswith("That's all, folksl"))
print(str_s.rfind('the') - str_s.find('the'))
print(str_s.count('the'))
print(str_s.isalnum())


s = "All that doth flow we cannot liquid name Or else would fire and water be the same;But that is liquid which is moist and wet Fire that property can never get. Then 'tis not cold that doth the fire put out But 'tis the wet that makes it die, no doubt. "
print("这首词总共有:" + str(len(s)) + "个字符串")
print("这首诗是否以All开头:",s.startswith('All'))
print("这首诗是否以That\'s all, folks!结尾:",s.endswith('That\'s all, folks!'))
print("第一次出现单词the的位置:",s.find(' the '))
print("最后一次出现单词the的位置:",s.rfind(' the '))
print("the在诗中出现的总次数:",s.count(' the '))
print("是否诗中出现的所有字符都是字母和数字:",s.isalnum())

'''


'''装饰器
import os

# print(os.getcwd())

def p(func):
	def inner():
		print('噗~~~')
		func()
	return inner

# def a():
# 	print('我放了个屁...')

#方法一
# p(a)()

#方法二
@p              # 使用 @ 功能时，被装饰函数要在 该语句之后定义
def a():
	print('我放了个屁...')
a()
'''



l = ['Hello', 'World', 18, 'Apple', None]
# l2 = [i.lower() for i in l if str(i).isalpha() and i != None]
# print(l2)
# l3 = [i.lower() for i in l if isinstance(i,str)]
# print(l3)
# print(type(l3))

# l3_g = (i.lower() for i in l if isinstance(i,str)) # 生成器
# print(type(l3_g))
# print(l3_g)
# for i in l3_g:
# 	print(i)
# 	print(type(i))



# i = 1
# while i<=9:
# 	j = 1
# 	while j<=i:
# 		# print(str(i)+'*'+str(j)+'='+str(i*j)+' ',end='')
# 		print('%s*%s=%s '%(i,j,i*j),end='')
# 		j+=1
# 	i +=1
# 	print()

for i in range(1,10):
	for j in range(1,10):
		if j<=i:
			print('%s*%s=%s ' % (i, j, i * j), end='')
	print()