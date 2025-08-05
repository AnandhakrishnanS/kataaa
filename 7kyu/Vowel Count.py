# count vowel
def get_count(sentence):
    vow=["a","e","i","o","u"]
    count=0
    for i in sentence:
        if i in vow:
            count+=1
    return count