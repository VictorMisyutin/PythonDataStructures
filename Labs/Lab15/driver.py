rooms = {
    "lobby" : {
        "room-number": 100,
        "use": "waiting",
        "sq-ft": 75
    },
    "exam room one" : {
        "room-number": 101,
        "use": "examination",
        "sq-ft": 125
    },
    "exam room two" : {
        "room-number": 102,
        "use": "examination",
        "sq-ft": 125
    },
    "exam room three" : {
        "room-number": 103,
        "use": "examination",
        "sq-ft": 125
    },
    "exam room four" : {
        "room-number": 104,
        "use": "examination",
        "sq-ft": 125
    },
    "cafeteria" : {
        "room-number": 200,
        "use": "eating",
        "sq-ft": 175
    },
    "womens restroom": {
        "room-number": 201,
        "use": "bathroom",
        "sq-ft": 25
    },
    "mens restroom": {
        "room-number": 202,
        "use": "bathroom",
        "sq-ft": 25
    },
    "disco room": {
        "room-number": 300,
        "use": "parties",
        "sq-ft": 175
    }
}

print("Please select one of these options:")
print("1. View all room names")
print("2. View more detail of a room")
print("3. Add a room")
print("4. Exit the program")
response = int(input("\nEnter a number 1-4: "))
while response < 0 or response > 4:
    print("1. View all room names")
    print("2. View more detail of a room")
    print("3. Add a room")
    print("4. Exit the program")
    response = int(input("\nEnter a number 1-4: "))
    print()
while response != 4:
    print()
    if response == 1:
        for room in rooms :
            print(f"{room}")
    elif response == 2:
        roomSearch = input("What room would you like more detail on: ")
        roomSearch = roomSearch.lower()
        try:
            for item in rooms[roomSearch]:
                print(f"{item}: {rooms[roomSearch][item]}")
        except:
            print(f"room {roomSearch} was not found.")
    else:
        try:
            roomName = input("what is the room name: ")
            roomName = roomName.lower()
            rooms[roomName] = {}
            roomNumber = int(input("what is the room number: "))
            roomUse = input("what is the room use: ")
            roomSqFt = int(input("what is the room square footage: "))
            try:
                rooms[roomName]["room-number"] = roomNumber
                rooms[roomName]["use"] = roomUse
                rooms[roomName]["sq-ft"] = roomSqFt
            except:
                print("error")
        except:
            print("invalid input")

    print("\n1. View all room names")
    print("2. View more detail of a room")
    print("3. Add a room")
    print("4. Exit the program")
    response = int(input("\nEnter a number 1-4: "))
    while response < 0 or response > 4:
        print("1. View all room names")
        print("2. View more detail of a room")
        print("3. Add a room")
        print("4. Exit the program")
        response = int(input("\nEnter a number 1-4: "))
        print()