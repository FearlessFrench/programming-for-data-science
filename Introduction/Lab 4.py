money = float(input("Enter (1-4) exchange Thai baht to (1. DollarUS 2.Yen 3.Euro 4.Other) : "))
USD = 33.83
YEN = 26.97
EUR = 36.72

if (money == 1):
    x = float(input("Enter amount Thai bath: "))
    y = x/33.83
    print(x,"bath exchange to US dollar is", y)

if (money == 2):
    x = float(input("Enter amount Thai bath: "))
    y = x/26.97
    print(x,"bath exchange to Yen is", y)

if (money == 3):
    x = float(input("Enter amount Thai bath: "))
    y = x/36.72
    print(x,"bath exchange to Euro is", y)

if (money == 4):
    x = float(input("Enter amount Thai bath: "))
    print("Please contact ID: 650510714, Name: Christopher French")
