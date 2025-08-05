# Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

def scramble(strng, array):
    srt=''
    
    comb=list(zip(list(strng),array))
    sort_com=sorted(comb,key=lambda n:n[1])
    lett=[x for x,_ in sort_com]
    for i in lett:
        srt+=i
    return srt