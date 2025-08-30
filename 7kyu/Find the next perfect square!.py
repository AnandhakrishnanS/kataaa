
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-

def find_next_square(sq):
    import math
    num=math.sqrt(sq)
    s=str(num)
    num_list=s.split(".")
    if num_list[1]=="0":
        return (math.isqrt(sq)+1)*(math.isqrt(sq)+1)
    else:
        return -1

