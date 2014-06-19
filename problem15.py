import math

def combination(n,r) :
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
print(combination(40,20))

