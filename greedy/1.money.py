def countCoin(p_money):
    moneys = [500,100,50,10]
    coin_count = 0
    t_money = p_money
    for money in moneys:
        res = divmod(t_money, money)
        coin_count += res[0]
        t_money = res[1]
    return coin_count


print(countCoin(1260))