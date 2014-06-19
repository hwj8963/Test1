import math

        
class Prime : 

        def __init__(self) :
                self.prime_max = 1
                self.prime_list = []
                self.fac_dic = {}

        def primes(self,n) :
                if(self.prime_max < n) :
                        for i in range(self.prime_max+1,n) :
                                isPrime = True
                                for k in self.prime_list :
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



                
        
        
