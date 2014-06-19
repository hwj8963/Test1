hail_step_num = {}


def hail_step(n) :
    if n == 1 :
        return 1
    elif n in hail_step_num :
        return hail_step_num[n]
    else :
        if n%2 == 0 :
            step = hail_step(n/2) + 1
            hail_step_num[n] = step
            return step
        else :
            step = hail_step(3*n+1) + 1
            hail_step_num[n] = step
            return step    

max_num = 1
max_step = 1
for i in range(1,1000000) :
    if hail_step(i) > max_step :
        max_step = hail_step(i)
        max_num = i
print(max_num,max_step)
    


