def coin_comb(coin_list,price) :
    if len(coin_list) == 1 :
        if price%coin_list[0] == 0 :
            return 1
        else :
            return 0
    else :
        coin = coin_list[0]
        sum = 0
        for n in range(int(price/coin)+1) :
            sum += coin_comb(coin_list[1:],price - coin * n)
        return sum
print(coin_comb([200,100,50,20,10,5,2,1],200))

