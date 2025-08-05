# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    new=text.lower()
    a_dic={chr(96+i):i for i in range(1,27)}
    res=[]
    for i in new:
        if i in a_dic:
            res.append(a_dic[i])
    res=[str(x) for x in res]
    return " ".join(res)