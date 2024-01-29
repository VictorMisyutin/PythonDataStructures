	# The formula for the calculation of an Economic Order Quantity is given as:

	# 	Q  =  √ [ 2 D S  / H  ]

	# where 	Q  is the EOQ units
	# 	D  is the demand in units ( typically on an annual basis )
	# 	S  is the order cost ( per purchase order )
	# 	H  is the holding costs ( per unit, per year )
import math
D = float(input("what is the demand in units?"))
S = float(input("what is the order cost?"))
H = float(input("what is the holding cost?"))
Q = math.sqrt((2*D*S)/H)
print("The EOQ units is ", str(format( Q, "0.3f")))