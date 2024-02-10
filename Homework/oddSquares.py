# define a list 
oddSquares = [] 
# populate the list
for x in range(1, 11) : 
    if (x % 2 == 1) : 
        oddSquares.append(x**2) 
# display the list contents
print (oddSquares)
print (len(oddSquares))