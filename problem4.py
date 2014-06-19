import palindrome
import prime
import itertools
import sys
from functools import reduce

P = prime.Prime()


for n in range(999*999,100*100,-1) :
    if palindrome.is_palindrome(n) :
        #print(n)
        fac = P.factorization(n)
        if fac[-1] > 1000 :
            continue
        for i in range(1,int(len(fac)/2)+1) :
            for comb in itertools.combinations(fac,i) :
                mul = reduce(lambda x,y:x*y,comb)
                remain = n/mul
                if mul>100 and mul<1000 and remain>100 and remain<1000 :
                    print(n)
                    sys.exit(0)
                
                

