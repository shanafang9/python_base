#coding:utf-8

class K(object):
	c_num = 0
	def __init__(self):
		K.c_num = K.c_num + 1
	def get_class_1(self):
		print(K.c_num)
	@classmethod
	def get_class_2(cls):
		print(cls.c_num)
k1 = K()
k2 = K()
k1.get_class_1()
k1.get_class_2()