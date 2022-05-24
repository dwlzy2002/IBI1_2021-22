def chocolate(total_money,price):
    number=total_money//price
    change=total_money%price
    print("We can buy how many chocolate:",number,"The change left:",change)
    return number,change
#example:
total_money=200
price=7
chocolate(total_money,price)
