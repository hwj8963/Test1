

n = 1001

s = 1
m = 1
for i in range(1,int((n+1)/2)) :
    for j in range(4) :
        m += i*2
        s += m
print(s)
    
