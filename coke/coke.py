
amount = 0


while amount < 50:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount= amount + coin
        if amount <= 50:
            print(f"Amount Due: {50 - amount}")
    else:
        print(f"Amount Due: {50 - amount}")


if amount >= 50:
        change = amount - 50
        print(f"Change Owed: {change}")



