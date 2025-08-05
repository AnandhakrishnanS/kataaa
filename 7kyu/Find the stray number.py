# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

def stray(arr):
    com=0
    x=arr.count(arr[0])
    y=arr.count(arr[1])
    if x>y:
        com=arr[0]
    elif y>x:
        com=arr[1]
    else:
        com=arr[0]
    ret=0
    for i in arr:
        if i!=com:
            ret=i
            break
    return ret