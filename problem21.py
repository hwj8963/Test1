import prime

P = prime.Prime()

def divisor_sum(n) :
    l = P.divisors(n)
    l.remove(n)
    return sum(l)


result = 0
for i in range(2,10001) :
    ds = divisor_sum(i)
    dsds = divisor_sum(ds)
    if ds == i :
        continue
    if dsds == i :
        print(i)
        result += i
print(result)
    

