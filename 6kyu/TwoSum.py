# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

def two_sum(numbers, target):
    x=0
    y=0
    for i in numbers:
        j=target-i
        print(j)
        x=numbers.index(i)
        numbers[x]=0.1
        if j in numbers:
            y=numbers.index(j)
            break
        x+=1
    return (x,y)