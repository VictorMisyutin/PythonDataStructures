import sqlite3

def display_cities_sorted_by_population(cursor, order='ASC'):
    cursor.execute(f'SELECT * FROM Cities ORDER BY Population {order}')
    cities = cursor.fetchall()
    print("Cities sorted by population:")
    print("City\tPopulation")
    for city in cities:
        print(city[1], city[2])

def display_cities_sorted_by_name(cursor):
    cursor.execute('SELECT * FROM Cities ORDER BY CityName')
    cities = cursor.fetchall()
    print("Cities sorted by name:")
    print("City\tPopulation")
    for city in cities:
        print(city[1], city[2])

def display_total_population(cursor):
    cursor.execute('SELECT SUM(Population) FROM Cities')
    total_population = cursor.fetchone()[0]
    print(f"Total population of all cities: {total_population}")

def display_average_population(cursor):
    cursor.execute('SELECT AVG(Population) FROM Cities')
    average_population = cursor.fetchone()[0]
    print(f"Average population of all cities: {average_population}")

def display_city_with_highest_population(cursor):
    cursor.execute('SELECT * FROM Cities ORDER BY Population DESC LIMIT 1')
    city = cursor.fetchone()
    print(f"City with the highest population: {city[1]} ({city[2]})")

def display_city_with_lowest_population(cursor):
    cursor.execute('SELECT * FROM Cities ORDER BY Population ASC LIMIT 1')
    city = cursor.fetchone()
    print(f"City with the lowest population: {city[1]} ({city[2]})")

def main():
    # Connect to the database.
    connection = sqlite3.connect('cities.db')
    cursor= connection.cursor()

    while True:
        print("\nSelect an operation:")
        print("1. Display a list of cities sorted by population, in ascending order")
        print("2. Display a list of cities sorted by population, in descending order")
        print("3. Display a list of cities sorted by name")
        print("4. Display the total population of all the cities")
        print("5. Display the average population of all the cities")
        print("6. Display the city with the highest population")
        print("7. Display the city with the lowest population")
        print("8. Exit")

        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            display_cities_sorted_by_population(cursor, 'ASC')
        elif choice == '2':
            display_cities_sorted_by_population(cursor, 'DESC')
        elif choice == '3':
            display_cities_sorted_by_name(cursor)
        elif choice == '4':
            display_total_population(cursor)
        elif choice == '5':
            display_average_population(cursor)
        elif choice == '6':
            display_city_with_highest_population(cursor)
        elif choice == '7':
            display_city_with_lowest_population(cursor)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    # Close the connection.
    cursor.connection.close()

if __name__ == '__main__':
    main()