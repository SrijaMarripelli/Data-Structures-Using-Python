# create a 2D array
my_2d_array = [[1,2,3], [4,5,6] ,[7,8,9]]

# access an element of the 2D array
print(my_2d_array[0][0])

# update an element of the 2D array
my_2d_array[0][0] = 6
print(my_2d_array)

# append a row to the 2D array
my_2d_array.append([10, 11, 12])
print(my_2d_array)

# get the number of rows and columns in the 2D array
num_rows = len(my_2d_array)
num_cols = len(my_2d_array[0])
print(num_rows, num_cols)