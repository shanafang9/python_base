#coding:utf-8
#
# l = [1,2,3,4,5]
# print('原：',l)
#
# l.append(6)
# print('append(元素)：',l)
# l.insert(0,'a')
# print('insert(索引,元素)：',l)
# l1 = [7,6,8]
# l.extend(l1)
# print('extend(seq)：',l)
#
# l.pop(0)
# print('pop(索引)：',l) # 默认删除最后一个元素
# l.remove(1)
# print('remove(元素)：',l)
#
# l.index(3)
# print('index(元素)：',l)
#
# l1 = l.copy()
# print('copy()：',l1)
#
# l.count(2)
# print('count(元素)：',l.count(2))
#
# l.reverse()
# print('l.reverse：',l)
#
# l.sort()
# print('l.sort()：',l)
#
# l.sort(reverse=True)
# print('l.sort(reverse=True)：',l)


'''test
l=list(enumerate(['a','b','c'],start=1))
print(l)
'''


# s = [1,2,3]
# t = s
# print(id(t),id(s))
# print(t,s)
# t.reverse()
# print(id(t),id(s))
# print(t,s)
#
# S = [1,2,3]
# T = S
# print(id(T),id(S))
# print(T,S)
# # T = S[::-1]
# S = S[::-1]
# print(id(T),id(S))
# print(T,S)



import random

print(random.random())# 不需要传入参数     0<=  n  <1.0
#例：0.7394443167122585

print(random.randint(1,10))#需要传入参数   1<=  n  <1=0
#例：7

'''异常处理
try:
	num = int('python')
except ValueError as e:
	print('错了:',e)
finally:
	print('再接再厉')

'''