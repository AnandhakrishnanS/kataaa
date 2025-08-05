# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    l=str(num)
    list1=list(l)
    list1.sort(reverse=True)
    a=""
    for i in list1:
        a+=i
    return(int(a))