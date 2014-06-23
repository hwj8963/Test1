import math
p1 = 1.0
p2 = 1.0
i = 3
p = 2
while i<5000 :
    p = p1+p2
    print(i,p)
    p1 = p2
    p2 = p
    i += 1
