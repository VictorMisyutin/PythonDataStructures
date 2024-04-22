import random
# the list of team members
team = ["Daisy", "Edward", "Kay", "Mirna", "Sidney", "Tina", "Zachary"]
taskSet = set(["A", "D", "E", "M", "O", "P", "Q", "R", "S", "T", "U", "V"])

# define the member's qualifications
daisy = set(["D", "M", "T", "U"])
edward = set(["D", "E", "M", "R", "V"])
kay = set(["E" , "M" , "S" , "V" , "U"])
mirna = set(["A" , "E", "O" , "P" , "S"])
sidney = set(["Q" , "R" , "V"])
tina = set(["A" , "M ", "O" , "P" , "S"])
zachary = set(["P" , "Q" , "O" , "T" , "U"])

# [ Set Intersection ]
# Determine the common attributes / preferences of team members
# Daisy and Edward. ( Refer to the starter code for this operation. )
print("Daisy and Edward Common Attributes:")
print(daisy.intersection(edward))
# [ An Empty Set ]
# Determine the common attributes / preferences of team members
# Mirna and Sidney.
print("\nMirna and Sidney Common Attributes:")
print(mirna.intersection(sidney))
# [ Set Union ]
# Determine the set of all the combined unique attributes in the profiles
# of members Daisy and Edward. ( Refer to the starter code for this
# operation. )
print("\nunique attributes of Daisy and Edward")
daisy.union(edward)

# [ Single Attribute Subset ]
# Form a team ( subset ) of all the members that are proficient in the "
# Design " attribute. ( Refer to the updated starter code for this
# operation. )
designMembers = []
team = ["Daisy", "Edward", "Kay", "Mirna", "Sidney", "Tina", "Zachary"]
if ("D" in daisy) :
    designMembers.append(team[0])
if ("D" in edward) :
    designMembers.append(team[1])
if ("D" in kay) :
    designMembers.append(team[2])
if ("D" in mirna) :
    designMembers.append(team[3])
if ("D" in sidney) :
    designMembers.append(team[4])
if ("D" in tina) :
    designMembers.append(team[5])
if ("D" in zachary) :
    designMembers.append(team[6])
print("All team members that are proficient in the design attribute")
print(designMembers)

# [ Set Complement ]
# Construct a Universal set which contains all the unique attribute
# categories that were previously outlined, i.e. A , D , E , M , etc. Then,
# form a subset, from this Universal set, of what you construe as being a
# grouping of attributes that would primarily focus on pure management
# tasks, i.e., not programming, nor software, etc. traits. Then form a set
# complement of your subset. ( Refer to the program code within the
# For Further Exploration step of this assignment. )

managerial = set(["M","O"])
print("\nSet of only managerial tasks: ")
print(managerial)

print("\nCompliment of managerial set")
print(taskSet.difference(managerial))

# [ Set Difference ]
# From the Universal set of all team members, construct two random
# subsets of team members. Then, form a set difference of your two subsets.
# ( Refer to the program code within the Information about This
# Project section of this assignment. )

# number of team members per set
newSet1 = set([])
newSet2 = set([])
for i in range(5):
    newSet1.add(random.choice(team))
    newSet2.add(random.choice(team))
print("\nfirst random set:")
print(newSet1)
print("second random set:")
print(newSet2)
print("\nfirst set difference of second random set:")
print(newSet1.difference(newSet2))

