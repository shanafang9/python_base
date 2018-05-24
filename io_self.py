#文件操作

'''基础'''
# path = '../os_test_2.txt'
# f = open(path,'r')
# s = f.read()
# print(s)
# f.close()


'''编码&解码'''
# path = '../os_test_2.txt'
# with open(path,'wb') as f1:
#     str = 'good'
#     f1.write(str.encode('utf-8'))
# with open(path,'rb') as f2:
#     data = f2.read()
#     print(data)
#     print(type(data))
#     print(data.decode('utf-8'))


import io
'''指定行 进行文件操作'''
path = '../os_test_2.txt'
with open(path,'r') as old_f:
    with open(path,'r+') as new_f:
        while True:
            seek_point = old_f.tell()
            if 'name' in old_f.readline().strip().split('*'):
                break
        new_f.seek(seek_point, 0)
        next_line = old_f.readline()
        while next_line:
            new_f.write(next_line)
            next_line = old_f.readline()
        new_f.truncate()



