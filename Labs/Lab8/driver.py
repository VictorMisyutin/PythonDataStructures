from MovieScript import MovieScript

spy_keywords = ["enemy", "gadgets", "mission", "spy", "agent", "espionage", "undercover", "intelligence", "covert"]
characters = ["Bames Jond", "Atniss Keverdeen", "Wohn Jick", "Parry Hotter", "Suke Liewalker"]

# create a new movie script object
ms = MovieScript()

# the movie text and sequences
ms.addScene("opening teaser sequence", 6, [characters[0]])
ms.addScene("main titles with theme song", 3, [])
ms.addScene("the plot unfolds", 15, [characters[0],characters[2],characters[3]])
ms.addScene("meeting with the superiors", 8, [characters[0], characters[4]])
ms.addScene("the gadgets are issued", 6, [characters[0], characters[2], characters[3]])
ms.addScene("the mission begins", 12,[characters[0], characters[2], characters[3]])
ms.addScene("a romance ensues", 8, [characters[0], characters[1]])
ms.addScene("thwarted but persistent", 12,[characters[0], characters[2], characters[3]])
ms.addScene("physical confrontation with the enemy", 20, [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("subplot: the superiors are revealed to be the enemy", 7, [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("subplot: The issued gadgets are faulty", 2, [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("subplot: Enemy tries to get away in an armored vehicle", 4, [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("subplot: The protaganists side swipe the car and aprehend the enemy", 6    , [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("the enemy is defeated", 6, [characters[0], characters[2], characters[3], characters[4]])
ms.addScene("the loose ends unfold", 17, [characters[0], characters[1], characters[2], characters[3]])
ms.addScene("on to the next mission", 3,[characters[0], characters[2], characters[3]])
ms.addScene("subplot: cut back to the enemy which is planning their revenge", 2, [characters[4]])

# convert the sequence list to a dictionary
for x in range(len(ms)) :
    print (u"\u2022", ms.getScriptIndex(x), ", duration:", ms.getDurationIndex(x), ", Actors: ", ms.getActorsIndex(x), end = "\n")
print ("\n")


# Search for predefined spy_keywords
print("Searching for predefined spy keywords:")
spy_keywords_found = []
for word in spy_keywords:
    found = False
    print("Searching for: " + word)
    for i in range(len(ms)):
        if word.lower() in ms.getScript()[i].lower() :
            spy_keywords_found.append(word)
            print(f"Keyword '{word}' found in scene sequence number:", i)
            found = True
    if not found:
        print(f"\"{word}\" not found")
    print()    

keyword_found = False
print ("please enter a keyword to search the movie sequences")
keyword = input().strip()
for i in range(len(ms)) :
    if (keyword in ms.getScript()[i]) :
        keyword_found = True
        print ("[keyword(s) found]")
        print ("in scene sequence number ", i + 1)
        print ("\"", ms.getScript()[i], "\"")
        print ("\n")
