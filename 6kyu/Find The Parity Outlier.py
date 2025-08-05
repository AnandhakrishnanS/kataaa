# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    check = "odd"
    flag = ""
    list1 = []
    re = 0
    for i in range(0, 3):
        if integers[i] % 2 == 0:
            list1.append(integers[i])
    print(list1)
    if len(list1) >= 2:
        check = "even"
    for i in integers:
        if i % 2 == 0:
            flag = "even"
            if check != flag:
                re = i
                break
        if i % 2 != 0:
            print(i)
            flag = "odd"
            if check != flag:
                re = i
                break
    return re