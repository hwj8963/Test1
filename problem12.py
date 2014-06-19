import prime

P = prime.Prime()
fac_dic = P.factorization_dic(2000)

tri_num = 0
for i in range(1,50000) :
    tri_num += i
    div_num = P.divisor_num(tri_num)
    if div_num >= 500 :
        print(tri_num,div_num)
        break
