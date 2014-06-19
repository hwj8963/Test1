import math

def digit(n, idx) :
    return int(n/math.pow(10,idx-1))%10

def is_palindrome(n) :
    digit_num = 1
    while True :
        if n < math.pow(10,digit_num) :
            break
        digit_num += 1
    for i in range(1,int(digit_num/2)+1) :
        if digit(n,i) != digit(n,digit_num-i+1) :
            return False
    return True

    
