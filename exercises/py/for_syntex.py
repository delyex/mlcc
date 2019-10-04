# 普通 for 循环
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# 如果这里不用 words[:]，会进入死循环
# [:] 表示拷贝一份源数据
for w in words[:]:
    if(len(w) > 6):
        words.insert(0, w)

# for ... else
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print(num, ' 等于 ', i, ' * ', j)
            break
    else:
        print(num, ' 第一个质数')


# 同时引用两个变量
mydict = {'Key1': [1, 2, 3, 4, 5], 'Key2': [6, 7, 8, 9, 10]}
for k, v in mydict.items():
    print(k, v)
print(type(mydict))

mylist = ['A', 'B', 'C']
print(type(mylist))

mylist = [(1, 1), (2, 2), (3, 3)]
print(type(mylist))
print(mylist[0])

mylist = [[1, 1], [2, 2], [3, 3]]
print(type(mylist))
print(mylist[0])
