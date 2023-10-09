# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)
# a=[1,2,3,4,5]
# print(a[3:0:-1])
# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])
# import random
#
# fruit=['apple', 'banana', 'papaya', 'cherry']
# random.shuffle(fruit)
# print(fruit)
#
# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
#     print("vvvvvvvvv::::", v)
#     for row in m:
#         print("row::::", row)
#         for element in row:
#             print("element::::", element)
#             if v < element:
#                 print(v)
#                 v = element
#                 print("v=element::::")
#     return v
# print(fun(data[0]))
# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i])
#     #print(arr[i].pop())
# l = [1,2,3,4,5]
# print(l.pop(4))
# def f(i, values = []):
#     print("iiii:::::", i)
#     values.append(i)
#     print ("values:::::", values)
#     return values
# f(1)
# f(2)
# f(3)
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     #print(arr[i - 1])
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
#
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# print("11111:::", fruit_list1)
# print("22222::::", fruit_list2)
# print("3333::::", fruit_list3)
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     print("ls:::::",ls)
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# print (sum)
# init_tuple = ()
# print (init_tuple.__len__())
# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print (init_tuple_a == init_tuple_b)
# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print (init_tuple_a + init_tuple_b)
# init_tuple_a = 1, 2
# init_tuple_b = (3, 4)
# # [print(sum(x)) for x in [init_tuple_a + init_tuple_b]]
# for x in [init_tuple_a + init_tuple_b]:
#     print(x)
#     print(sum(x))
# init_tuple = [(0, 1), (1, 2), (2, 3)]
# result = sum(n for _, n in init_tuple)
# print(result)
# # Initialize a list of tuples
# init_tuple = [(0, 1), (1, 2), (2, 3)]
# # Initialize a variable to store the sum
# result = 0
# # Iterate through each tuple in init_tuple
# for _, n in init_tuple:
#     # Add the second element of each tuple to the result
#     result += n
# # Print the result
# print(result)
# l = [1, 2, 3]
# print(l.__len__())
# print(l[::-1][0])
# print(('python',) * (3))
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
# print(init_tuple)
# init_tuple = ((1, 2),) * 7
# nes = ((1,2),) * 7
# print(len(nes[3:8]))
#print(len(init_tuple[3:8]))
# a = {(1,2):1,(2,3):2}
# print(a[1,3])
# a = {'a':1,'b':2,'c':3}
# print (a['a'])
# print (a['a','b'])
# fruit = {}
# def addone(index):
#     if index in fruit:
#         print("index::::", index)
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('banana')
# addone('apple')
# addone('apple')
# print(fruit)
# # print(len(fruit))
# count = sum(fruit.values())
# print(count)
# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# arr[1.0] = 1
# print(arr)
# sum = 0
# for k in arr:
#     print(k)
#     sum += arr[k]
#     #print(arr[k])
# print (sum)
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates['box']))
# print(crates['box'])
# print(crates['jars'])
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print (dict[_], end=" ")
# for i in range(1, 6):
#     for j in range(1):
#         print('*' * i, end=" ")
#     print()
# Define the number of rows
num_rows = 4
for i in range(num_rows):
    for j in range(num_rows - i - 1):
        print(" ", end=" ")
    for k in range(i + 1):
        if k == i:
            print("*", end=" ")
        else:
            print("*", end="  ")
    print()
