# the list of team members
team = ["Daisy", "Edward", "Kay", "Mirna", "Sidney", "Tina", "Zachary"]
print (team)
# define the member's qualifications
# Daisy D , M , T , U
# Edward D , E , M , R , V
# Kay E , M , S , V , U
# Mirna A , E, O , P , S
# Sidney Q , R , V
# Tina A , M , O , P , S
# Zachary P , Q , O , T , U

member1 = set(["D", "M", "T", "U"])
member2 = set(["D", "E", "M", "R", "V"])
member3 = set(["E" , "M" , "S" , "V" , "U"])
member4 = set(["A" , "E", "O" , "P" , "S"])
member5 = set(["Q" , "R" , "V"])
member6 = set(["A" , "M ", "O" , "P" , "S"])
member7 = set(["P" , "Q" , "O" , "T" , "U"])

# perform a set operation ( union )
setUnion1 = member1.union(member2)
setUnion1 = sorted(setUnion1)
print ("\n")
print ("set operation:", team[0], "union", team[1], setUnion1)
# perform a set operation ( intersection )
setIntersect1 = member1.intersection(member2)
setIntersect1 = sorted(setIntersect1)
print ("\n")
print ("set operation:", team[0], "intersect", team[1], setIntersect1)
print ("\n")
listD = []
condition = True
while (condition) :
    if ("D" in member1) :
        listD.append(team[0])
    if ("D" in member2) :
        listD.append(team[1])
        condition = False
sorted(listD)
print (listD)
commonSet_D = set([])
commonSet_D.update(listD)
sorted(commonSet_D)
print (commonSet_D)

# [ Set Intersection ]
# Determine the common attributes / preferences of team members
# Daisy and Edward. ( Refer to the starter code for this operation. )

# [ An Empty Set ]
# Determine the common attributes / preferences of team members
# Mirna and Sidney.

# [ Set Union ]
# Determine the set of all the combined unique attributes in the profiles
# of members Daisy and Edward. ( Refer to the starter code for this
# operation. )