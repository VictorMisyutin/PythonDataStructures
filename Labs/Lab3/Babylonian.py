# Babylonian Method
# Programmer: Victor Misyutin
import math
TOLERANCE = 0.001

def Babylonian(number) :
    x = number
    # (1) choose y = 1 as an initial estimate of square root(x)
    y = 1
    # (2) if x > 2 , let y = x / 2
    if (x > 2):
        y = x/2
    count = 1
    while (True) :
        # (3) let y = the average of y and x / y
        y =  (y + (x/y))/2
        if (abs((y*y) - x) < TOLERANCE ):
            # (5) return y , as the square root of x
            return y
        # (4) if y ^ 2 is not close enough to x , then repeatstep (3)
        print(count, y)
        count = count + 1
print ("Programmer: Victor Misyutin")
print ("CSC 242 Python Data Structures")
print ("----- The Babylonian Method -----\n")

radicand = float(input("please enter a positive real number "))
radical = Babylonian(radicand)
print ("the square root of", radicand, "is", radical)

print ("\nValue using math library: ", math.sqrt(radicand))