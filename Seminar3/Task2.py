# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

#list_1 = [i for i in range(1, int(input("Enter number: ")) + 1)]
#print(list_1)
list_1 = [1, 2, 6, 9, 10]
find_numb = int(input("Enter near number you want to find to: "))
if find_numb < 0:
    print("Sorry, try enter the positive number: ")
if find_numb not in list_1:
    b = len(list_1)
    list_1.append(find_numb) 
# print(list_1)
    list_1.sort()
    a = list_1.index(find_numb)
#   print(a)
    if a == b:
        print(list_1[a-1])
    elif a < b:
        left_numb = find_numb - list_1[a-1]
        right_numb = list_1[a+1] - find_numb
        if left_numb < right_numb:
            print(list_1[a-1])
        elif left_numb > right_numb:
            print(list_1[a+1])
        else:
            print(f"There are two nearest numbers to desired: {list_1[a-1]} and {list_1[a+1]}")
else:
    print(list_1.index(find_numb))






# min = list_1[0]
# max = list_1[0]
# for i in list_1:
#     if find_numb > 0:
#         res = find_numb - i
#         if res < min:
#             min = res
#             val = i
#             print(val)
#     elif find_numb < 0:
#         res = find_numb - i
#         if res > max:
#             max = res
#             val = i
#     else:
#         res = find_numb - i
#         if res > max:
#             max = res
#             val = i
            

    