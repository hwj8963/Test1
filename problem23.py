import prime

P = prime.Prime()
def divisor_sum(n) :
    l = P.divisors(n)
    l.remove(n)
    return sum(l)


over = []

for i in range(1,28124) :
    ds = divisor_sum(i)
    if ds > i :
        over += [i]

oversum = {}
for i in over :
    for j in over :
        if i+j<28124 :
            oversum[i+j] = 1
result = []
for i in range(1,28124) :
    if not i in oversum :
        result += [i]
print(result)
