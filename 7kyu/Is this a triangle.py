# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

def is_triangle(a, b, c):
    check=[]
    if a+b>c:
        check.append(1)
    if b+c>a:
        check.append(1)
    if a+c>b:
        check.append(1)
    if len(check)==3:
        return True
    else:
        return False