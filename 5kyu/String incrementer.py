# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

def increment_string(string1):
    num=""
    str1=""
    list1=list(string1)
    count=0

    for i in reversed(string1):
            try:
                s=int(i)
                num+=str(i)
                count+=1
            except ValueError:
                break
    num=num[::-1]
    str1=string1[0:len(string1)-count]
    print(str1)

    if num!="":
        leno=len(num)
        num=str(int(num)+1).zfill(leno)
        str1+=num
    else:
        str1+="1"
    return str1