import math
import itertools
from functools import reduce

class Prime2 :
        def primes(self,n) :
                list = range(2,n+1)
                i = 0
                while list[i] < math.sqrt(n) :
                        print(list[i])
                        list = [m for m in list if m<=list[i] or m%list[i] != 0]
                        i += 1
                return list
        
        




        
class Prime : 

        def __init__(self) :
                self.prime_max = 1
                self.prime_list = []
                self.fac_dic = {}
        def prime_nth(self,n) :
                while len(self.prime_list) < n :
                        now = self.prime_max+1
                        isPrime = True
                        for k in self.prime_list :
                                if k > math.sqrt(now) :
                                        break
                                if now%k == 0 :
                                        isPrime = False
                                        break
                        if isPrime :
                                self.prime_list += [now]
                        self.prime_max += 1
                return self.prime_list[n-1]       
                
        def primes(self,n) :
                if(self.prime_max < n) :
                        for i in range(self.prime_max+1,n) :
                                isPrime = True
                                for k in self.prime_list :
                                        if k > math.sqrt(i) :
                                                break
                                        if i%k == 0 :
                                                isPrime = False
                                                break
                                if isPrime :
                                        self.prime_list += [i]
                        self.prime_max = n
                        return self.prime_list
                else :
                        num = 0
                        for i in self.prime_list :
                                if(i>n) :
                                        break
                                num += 1
                        return self.prime_list[0:num]
        def factorization_dic(self,n) :
                fac = self.factorization(n)
                fac_dic = {}
                for p in fac :
                        if p in fac_dic :
                                fac_dic[p] += 1
                        else :
                                fac_dic[p] = 1
                return fac_dic
        def divisor_num(self,n) :
                fac_dic = self.factorization_dic(n)
                num = 1
                for p in fac_dic :
                        num *= fac_dic[p]+1
                return num                
        def factorization(self,n) :
                if n == 1 :
                        return []
                elif n in self.fac_dic :
                        return self.fac_dic[n]
                elif n in self.prime_list :
                        self.fac_dic[n] = [n]
                        return [n]
                else :
                        for p in self.prime_list :
                                if n%p == 0 :
                                        fac_rest = self.factorization(int(n/p))
                                        fac = [p] + fac_rest
                                        self.fac_dic[n] = fac
                                        return fac
                        for i in range(self.prime_max+1,int(math.sqrt(n))+1) :
                                isPrime = True
                                for k in self.prime_list :
                                        if k > math.sqrt(i) :
                                                break
                                        if i%k == 0 :
                                                isPrime = False
                                                break
                                self.prime_max = i
                                if isPrime :
                                        self.prime_list += [i]
                                        if n%i == 0 :
                                                fac_rest = self.factorization(int(n/i))
                                                fac = [i] + fac_rest
                                                self.fac_dic[n] = fac
                                                return fac
                                
                        self.fac_dic[n] = [n]
                        return [n]           



                
        
        
