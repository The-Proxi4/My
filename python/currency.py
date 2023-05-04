yuan=float(input("What do you have left in yuan? " ))
yen=float(input("What do you have left in yen? " ))
won=float(input("What do you have left in won? " ))

yuan= yuan*0.15
yen= yen*0.0075
won= won*0.0007
usd=(yuan+yen+won)
print (usd)