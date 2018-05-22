# coding:utf-8

# for i in range(1,5):
# 	for j in range(1,5):
# 		print(j,end=' ')
# 	print()

# for i in range(1,5):
# 	for j in range(1,5):
# 		if i ==1 or i == 4 or j == 1 or j == 4:
# 			print(i, end=' ')
# 		else:
# 			print(' ', end=' ')
# 	print()


# n = 4
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if i ==1 or i == n or j == 1 or j == n:
# 			print(i, end=' ')
# 		else:
# 			print(' ', end=' ')
# 	print()



# n = 4
# for i in range(1,n+1):
# 	for j in range(1,n):
# 		print(' ',end='')
# 	for k in range(1,i+1):
# 		print(i, end='')
# 	print()



# n = 4
# for i in range(1,n+1):
# 	for j in range(1,n-i+1):
# 		print(' ',end='')
# 	for k in range(1,2*i):
# 		print(i, end='')
# 	print()


# n = 4
# for i in range(1,n+1):
# 	for j in range(1,n-i+1):
# 		print(' ',end='')
# 	for k in range(1,2*i):
# 		if k == 1 or k == 2*i-1:
# 			print(k, end='')
# 		elif i == n:
# 			print(i,end='')
# 		else:
# 			print(' ',end='')
# 	print()

import os

# print(os.getcwd())





''' #输出质数#

for i in range(2,101):
	flag = True
	for j in range(2,i):
		if i%j == 0 :
			flag = False
			break
	if flag == True:
		print(i)

'''

