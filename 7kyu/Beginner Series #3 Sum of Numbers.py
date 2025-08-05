# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    result=0
    if a==b:
        return a
    else:
        if a>b:
            for i in range(b,a+1):
                result+=i
        else :
            for i in range(a,b+1):
                result+=i
        return result