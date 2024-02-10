
import math
# sample data
data_list = [280, 255, 242, 207, 201]

# determine the mean value
sums = 0
for i in range(len(data_list)) :
    sums += data_list[i]
mean = sums / len(data_list)

# for each value, find the square deviation from the mean 
difference_squared = 0
for i in range(len(data_list)) :
    difference_squared += (data_list[i] - mean) ** 2

# find the square root
difference_squared = math.sqrt(difference_squared)
print(difference_squared)
