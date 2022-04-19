def chocolate(total_money,price):
    number=total_money//price
    change=total_money%price
    print(number,change)
    return number,change
total_money=200
price=7
chocolate(total_money,price)
