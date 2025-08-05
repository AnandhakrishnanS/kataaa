# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000, but fixed tests go higher.

def divisors(n):
    if n==1:
        return 1
    else:
        lis=[n,1]
        for i in range(2,n):
            if n%i==0:
                lis.append(i)
        return len(lis)