print("enter the number of coins required to make exactly $3.00")

pennies = input("Please enter the amount of pennies: ")
nickles = input("Please enter the amount of nickles: ")
dimes = input("Please enter the amount of dimes: ")
quarters = input("Please enter the amount of quarters: ")

sum = (int(pennies)) + (int(nickles)*5) + (int(dimes)*10) + (int(quarters)*25)
sum = sum/100
if(sum == 3.00):
    print("Congrats, you made exactly $3.00")
else:
    print("You did not make exactly $3.00. The total amount of money is: $" + str(sum))