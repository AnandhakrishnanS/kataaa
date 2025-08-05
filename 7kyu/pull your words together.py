# Every time that it tries to say a sentence, instead of formatting it in normal English orthography, it just outputs a list of words.

# Robbie has pulled multiple all-nighters to get this project finished, and he needs some beauty sleep. So, he wants you to write the last part of his code, a sentencify function, which takes the output that the machine gives, and formats it into proper English orthography.

# Your function should:

# Capitalise the first letter of the first word.
# Add a period (.) to the end of the sentence.
# Join the words into a complete string, with spaces.
# Do no other manipulation on the words.

def sentencify(words):
    sent=""
    for i in words:
        if words.index(i)==0:
            if i[0].isupper()==True:
                i.upper()
                sent+=i
            else:
                i=i.capitalize()
                sent+=i
            
            
        else:
            sent+=" "
            sent+=i
    sent+='.'
    return sent