print ("Program: Target GPA")
print ("Programmer: Victor Misyutin")
print ("-------------------------")
# ---------------------------------------------------
# variables declared and initialized
msg1 = ""; msg2 = ""
totalHours = 0; creditsEarned = 0; creditsCurrent = 0
currentGPA = 0; targetGPA = 0
targetGradePoints = 0; requiredGPA = 0
# ... declare and assign any additional variables here ...
# ---------------------------------------------------
print ("----- INPUTING Data -----")
msg1 = "GPA credit hours already completed ( Credits Earned ) "
creditsEarned = int(input("enter " + msg1))
msg2 = "GPA credit hours in progress or planned "
creditsCurrent = int(input("enter " + msg2))
msg3 = "Current GPA ( Cumulative ) "
currentGPA = float(input("enter " + msg3))
msg4 = "What is your desired GPA "
targetGPA = float(input("enter " + msg4))
# ---------------------------------------------------
print ("----- PROCESSING Data -----")
totalHours = creditsEarned + creditsCurrent
targetGradePoints = targetGPA * totalHours
targetGradePoints -= creditsEarned * currentGPA
requiredGPA = targetGradePoints/creditsCurrent
# ... complete the processing section of this program ...
# ---------------------------------------------------
print ("----- OUTPUTTING Data -----")
# ... complete the output section of this program ...
print("To attain your desired GPA of " + str(targetGPA) + " you must recieve a GPA of " + 
      str(format( requiredGPA, "0.2f")) + " in your remaining " + str(creditsCurrent) + " credits.")
