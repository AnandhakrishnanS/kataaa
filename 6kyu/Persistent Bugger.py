# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    l1=list(map(int,str(n)))
    print(l1)
    count=0
    while len(l1)!=1:
        s=1
        for i in l1:
            s*=i
        l1=list(map(int,str(s)))
        count+=1
        print(l1)
    return count