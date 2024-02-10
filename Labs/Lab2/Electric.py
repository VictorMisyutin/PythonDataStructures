# Selection Program Control
print ("Programmer: Victor Misyutin")
print ("CSC 242 Python Data Structures")
print ("Lab 2: Electrical Kilowatt Usage")
print ("-------------------------")
# ---------------------------------------------------
custID = 0
custName = ""
# ---------------------------------------------------
def getCustomerData() :
    global custID, custName, custAddress, KWH, pastDue
    custName = input("please enter the Customer Name: ")
    custID = int(input("please enter the Customer Number:"))
    custAddress = input("please enter the Customer Address:")
    KWH = int(input("please enter the Kilowatt - Hour Used:"))
    pastDue = float(input("please enter the amount past due:$"))

# ---------------------------------------------------
def calculateElecticBill() :
    amt = 0
    # place if - elif - else block here
    if KWH < 125:
        amt = 0.1* KWH
    elif KWH > 125 and KWH < 320:
        amt = 12.50 + (0.09 * (KWH-125))
    elif KWH > 320 and KWH < 500:
        amt = 30.60 + (0.08 * (KWH-320))
    else:
        amt = 42.60 + (0.06 * (KWH-500))

    if amt > 300:
        amt = amt + (amt*0.12)
    amt = amt + pastDue + (0.025*pastDue)
    return amt
# ---------------------------------------------------
print ()
# call the functions
getCustomerData()
amt = calculateElecticBill()
# ---------------------------------------------------
# display the Electricity Bill Summary
print ("\nElectricity Bill\n")
print ("\n****************\n")
print ("Customer ID Number\t", custID)
print ("Customer Name\t", custName)
print ("Customer Address\t", custAddress)
print ("Killowatt per hour Used\t", KWH)
print ("Amount Past Due\t", pastDue)
print ("Total Amount Due\t", str(format(amt, "0.2f")))
