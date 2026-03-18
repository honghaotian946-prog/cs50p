amount_due = 50

while amount_due > 0:
    print(f"Amount_due:{amount_due}")
    coin = int(input("Insert Coin:"))
    if coin in [5,10,25]:
        amount_due -= coin

change_owed = -amount_due
print(f"Change owed:{change_owed}")