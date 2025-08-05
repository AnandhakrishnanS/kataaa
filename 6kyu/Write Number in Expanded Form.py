# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"

def expanded_form(num):
    num = str(num)
    exp=[]
    ind=1
    for i in num:
        pos=len(num)-ind
        if i!="0":
            n=i
            for i in range(0,pos):
                n+="0"
            exp.append(n)
        ind+=1
    return " + ".join(exp)