import digit
import math

sum = 0 
    
for i in range(1,100000000) :
    digits = digit.digits(i)
    dfs = 0
    for d in digits :
        dfs += math.factorial(d)
    if dfs == i :
        print(i)
        sum+=i
print(sum)
