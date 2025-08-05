# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

def tribonacci(signature, n):
    j=0
    res=0
    if len(signature)>n:
        for i in range(0,len(signature)-n):
            signature.pop()
        return signature 
    else:
        while len(signature)<n:
            res=signature[j]+signature[j+1]+signature[j+2]
            j+=1
            signature.append(res)
        return signature