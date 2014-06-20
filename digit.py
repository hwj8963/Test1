import math

def digit(n, idx) :
    return int(n/math.pow(10,idx-1))%10

def digitsum(n) :
    sum = 0
    while n != 0 :
        sum += n%10
        n = int(n/10)
    return sum

