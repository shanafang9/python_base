# coidng:utf-8

'''
# dict
zip()、{}.fromkeys()、keys()、values()、get()、setdefault()、uodate()、

'''


# print(dir(dict))


'''zip()'''
# d = list(zip((1,2,3),(4,5,6),('s','b')))
# [(1, 4, 's'), (2, 5, 'b')]
# d = list(zip((1,2,3),(4,5,6),('a','b','c')))
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

# d = dict(zip((1,2,3),(4,5)))
# print(d)
# {1: 4, 2: 5}


'''{}.fromkeys()'''
# d = {1:1}
# l1 = [1,2,3]
# l2 = [4,5,6]
# d = {}.fromkeys(l1)
# {1: None, 2: None, 3: None}
# d = d.fromkeys(l1,l2)
# print(d)
# {1: [4, 5, 6], 2: [4, 5, 6], 3: [4, 5, 6]}


'''keys()&values()'''
# d = {1:'a', 2:'b', 3:'c'}
# a = d.keys()
# dict_keys([1, 2, 3])
# b = d.values()
# dict_values(['a', 'b', 'c'])


'''pop()&popitem()'''
# d = {1:'a', 2:'b', 3:'c'}
# print(d.pop(1)) # 指定 key 删除
# a
# {2: 'b', 3: 'c'}
# print(d.popitem()) # 随机删除 删除
# (3, 'c')
# {1: 'a', 2: 'b'}


'''get()'''
# d = {1:'a', 2:'b', 3:'c'}
# print(d.get(1)) # 按 key 查找 若key存在返回 value 否则返回 None(返回值可指定字符串)
# a
# print(d.get(4))
# None
# print(d.get(4,'hello'))
# hello


'''setdefault()'''
# d = {1:'a', 2:'b', 3:'c'}
# print(d.setdefault(1))
# a
# print(d.setdefault(1,'hh'))
# a
# {1: 'a', 2: 'b', 3: 'c'}
# print(d.setdefault(4))
# None
# {1: 'a', 2: 'b', 3: 'c', 4: None}
# print(d.setdefault(5,'df'))
# df
# {1: 'a', 2: 'b', 3: 'c', 4: None, 5: 'df'}


'''update()'''
# d1 = {1:'a'}
# d2 = {2:'j'}
# d3 = {}
# d1.update(d2)
# {1: 'a', 2: 'j'}
# d3.update(d1)
# {1: 'a', 2: 'j'}


'''items()'''
# d = {1:'a', 3:'b', 2:'c'}
# print(d.items())
# dict_items([(1, 'a'), (3, 'b'), (2, 'c')])


'''clear()'''
# d = {1:'a', 2:'b', 3:'c'}
# {1: 'a', 2: 'b', 3: 'c'}
# d.clear()
# {}


'''copy()'''
# d = {1:'a', 2:'b', 3:[1,2]}
# d1 = d.copy() # 浅拷贝
# print(d1)
# d[3].append(3)
# print(d1)


'''has_key() # python2'''
# print(dir(dict))




# print(dict([1,2])) 报错
# print(dict((1,2)))
print(dict(([1,2],)))
print(dict(([1,2],[3,4])))
print(dict(zip([1,2],[3,4])))


d = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
print(len(d))

d = {}
print(len(d))