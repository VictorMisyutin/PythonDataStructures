import random
import csv
# the Writer's Grid
grid = []

try :
    data = []
    with open("words.csv", "r", encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            tempArr = []
            for word in row:
                tempArr.append(word)
            data.append(tempArr)
except:
    print("file not found")

all_words = [word for row in data for word in row]
samples = random.sample(all_words, 6)

print ("[ the script ]")
print("")
print ("I started the day by looking for the", samples.pop(), end = ".")
print ()
print ("I planned later to walk to the", samples.pop(), end = ".")
print ()
print ("Surprisingly, I found the", samples.pop(), "was empty", end= ".")
print ()
print ("I wondered if a", samples.pop(), "would appear", end = ".")
print ()
print ("My aunt must have left my cellular telephone with the", samples.pop(), end = ".")
print ()
print ("Yesterday, I forgot to take the", samples.pop(), "to the meeting", end = ".")
print ("\n\n")

total_entropy = 0
print ("\n")
print ("please enter an integer that will describe the entropy analysis (0 to 5)")
for i in range(6):
    print(f"for grid line {i+1}: ", end=" ")
    entropy = int(input())
    total_entropy += entropy
    print (f"estimated entropy for grid line {i+1}:", entropy)
    print()
print ("\ntotal entropy :", total_entropy)
print ("\n\n")
