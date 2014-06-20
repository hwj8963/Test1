import math
import copy
import digit
class BigInteger :
    dpn = 10
    dn = int(math.pow(10,dpn))
    def __init__(self,num) :
        if isinstance(num,BigInteger) :
            self.num_list = copy.copy(num.num_list)
        else :
            self.num_list = []
            while num != 0 :
                self.num_list += [num % self.dn]
                num = int(num/self.dn)
    def __str__(self) :
        s = ""
        first = True
        for num in self.num_list[::-1] :
            if first :
                s+=str(num)
                first = False
                continue
            s+=" "
            for digit in range(self.dpn-1,0,-1) :
                if int(num /math.pow(10,digit)) != 0 :
                    break
                s+="0"
            
            s+=str(num)
        return s
    def __eq__(self,other) :
        if len(self.num_list) != len(other.num_list) :
            return False
        for i in range(len(self.num_list)) :
            if(self.num_list[i] != other.num_list[i]) :
                return False
        return True
    #def __ne__(self,other) :
    #    return not self.__eq__(other);
    def __lt__(self,other) :
        if len(self.num_list) < len(other.num_list) :
           return True
        elif len(self.num_list) > len(other.num_list) :
            return False
        else :
            for i in range(len(self.num_list)-1,-1,-1) :
                if self.num_list[i] < other.num_list[i] :
                    return True
                elif self.num_list[i] > other.num_list[i] :
                    return False
            return False
    def __le__(self,other) :
        return self==other or self<other
    def __add__(self,other) :
        if isinstance(other,BigInteger) :
            if self > other :
                big = BigInteger(self)
                small = BigInteger(other)
            else :
                 big = BigInteger(other)
                 small = BigInteger(other)

            for i in range(len(small.num_list)) :
                big.num_list[i] += small.num_list[i]
            big.normalize()
            return big
        else :
            ret = BigInteger(self)
            ret.num_list[0] += other
            ret.normalize()
            return ret
    def __mul__(self,other) :
        if isinstance(other,int) :
            new = BigInteger(self)
            for i in range(len(new.num_list)) :
                new.num_list[i] *= other
            new.normalize()
            return new
                
    def normalize(self) :
        carry = 0
        for i in range(len(self.num_list)) :
            n = self.num_list[i]
            n += carry
            carry = int(n/self.dn)
            n = n%self.dn
            self.num_list[i] = n
        while carry > 0 :
            self.num_list += [carry%self.dn]
            carry = int(carry/self.dn)
    def digitsum(self) :
        sum = 0
        for n in self.num_list :
            sum += digit.digitsum(n)
        return sum
        
A = BigInteger(2763475829034975)
B = BigInteger(1624987593949234382)
C = BigInteger(2763475829034975)
print(A.digitsum())


