# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    com=0
    n=0
    flag=False
    for i in range(0,3):
        if arr.count(arr[i])>1:
            com=arr[i]
            break
        else:
            n=arr[i]
            flag=True
    if flag==False:
        for i in arr:
            if i!=com:
                n=i
                break
            
    return n