# coding:utf-8

s1 = {1,2,3,4,5}
s2 = {3,4,5,6}

print(s1-s2) # 差集 # s1 中有而 s2 中没有的 元素
# {1, 2}

print(s1|s2) # 并集 # s1 中有与 s2 中有的 元素(集合 set 无法保存重复元素)
# {1, 2, 3, 4, 5, 6}

print(s1&s2) # 交集 # s1 中有且 s2 中也有的 元素
# {3, 4, 5}

print(s1^s2) # 不同是存在s1和s2 的元素 #
# {1, 2, 6}
