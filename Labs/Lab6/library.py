import random
import pickle as pk
genres = {1: "hobby", 2: "romance", 3: "cooking", 4: "science", 5: "adventure", 6: "puzzle"}
library_magazine_categories = [[1,2,3,4,5]]
library_magazine_quantities = [[1,2,3,4,5]]
# create magazine categories array
for i in range(3):
    arr = []
    for j in range(5):
        arr.append(random.randint(1, 6))
    library_magazine_categories.append(arr)
# create magazine quantities array
for i in range(3):
    arr = []
    for j in range(5):
        arr.append(random.randint(0, 99))
    library_magazine_quantities.append(arr)
file1 = open("categories.p", "wb")
file2 = open("quantities.p", "wb")
pk.dump(library_magazine_categories, file1)
pk.dump(library_magazine_quantities, file2)
file1.close()
file2.close()
print("Welcome to Victors Library:")
user_input = input("Are you an admin?\n(y/n):")
if user_input == 'n':
    floor_input = int(input("What floor would you like to go to (1 - 5 inclusive): "))
    room_input = int(input("What room would you like to go to (1 - 3 inclusive): "))
    print(f'floor {floor_input} room {room_input} contains {library_magazine_quantities[room_input][floor_input-1]} books on {genres.get(library_magazine_categories[room_input][floor_input-1])}')
else:
    categories_file = open("categories.p", "rb")
    quantities_file = open("quantities.p", "rb")
    stored_categories = pk.load(categories_file)
    stored_quantities = pk.load(quantities_file)
    for j in range(5):
        for i in range(3):
            print(f'floor {j+1} room {i+1} contains {stored_quantities[i+1][j]} {genres.get(stored_categories[i+1][j])} books')
    categories_file.close()
    quantities_file.close()
