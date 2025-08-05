# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.

def solution(array_a, array_b):
    sol=0
    indi=0
    for i in array_a:
        h=array_a[indi]-array_b[indi]
        sol+=h**2
        indi+=1
    return sol/len(array_a)