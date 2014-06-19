import math

class BigInteger :
    dpn = 10
    def __init__(self,num) :
        self.num_list = []
        while num != 0 :
            self.num_list += [num % int(math.pow(10,self.dpn))]
            num = int(num/math.pow(10,self.dpn))
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
    def __add__(self,other) :
        #todo
        print(A,B)
        return 0
A = BigInteger(100000030000500007000001)
B = BigInteger(5)



