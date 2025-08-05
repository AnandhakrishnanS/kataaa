# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    list1 = []
    list2 = []
    for i in range(len(text)):
        list1.append(text[i])
    print(list1)
    for j in range(len(ending)):
        list2.append(ending[j])
    print(list2)
    count=1
    flag=False
    for k in range(len(list2) - 1, -1, -1):

        if list2[k] == list1[len(list1) - count]:
            flag = True
            count += 1
        else:
            flag = False
            break
    if flag==True:
        return True
    else:
        return False

solution('abc', 'bc')