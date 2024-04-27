# creating an empty dictionary
myDict = {}
# entering the number of key - value pairs
print ("How many employees would you like to log.")
count = int(input())
# populating the dictionary
for num in range(count) :
    lst = []
    print ("enter the base salary, then total sales, then commision rate")
    salary = float(input())
    lst.insert(0, salary)
    sales = float(input())
    lst.insert(1, sales)
    commision_rate = float(input())/100
    lst.insert(2, commision_rate)
    commision = float(sales*commision_rate)
    lst.insert(3, commision)
    total = salary + commision
    lst.insert(4, total)
    print ("enter the employee name")
    key = input()
    # associate a key with its value
    myDict[key] = lst

print("Employee: Commision, Total Earnings")
for employee, values in myDict.items() :
    print(f"\t{employee} : ${values[3]}, ${values[4]}")

