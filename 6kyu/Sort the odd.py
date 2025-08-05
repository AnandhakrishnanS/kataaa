# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    olis=[]
    for i in source_array:
        if i%2!=0:
            olis.append(i)
    olis.sort()
    print(olis)
    count=0
    indexer=0
    for j in source_array:
        if j%2!=0:
            source_array.pop(indexer)
            source_array.insert(indexer,olis[count])
            print(source_array, count)
            count+=1
        indexer+=1

    return source_array