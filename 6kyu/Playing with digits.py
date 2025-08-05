# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

def dig_pow(n, p):
    digit=0
    lus=list(map(int,str(n)))
    
    k=0
    for i in lus:
        digit+=i**p
        p+=1
    print(digit)
    for j in range(1,100000):
        if (j*n)==digit:
            k=j
            break
        else:
            k=-1
    return k