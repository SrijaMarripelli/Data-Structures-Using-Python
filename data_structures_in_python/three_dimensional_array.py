# create a 3D array
my_3d_array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]

# access an element of the 3D array
print(my_3d_array[0][0][0])

# update an element of the 3D array
my_3d_array[0][0][0] = 6
print(my_3d_array)

# append a 2D array to the 3D array
my_3d_array.append([[13,14], [15,16]])
print(my_3d_array)

# get the shape of the 3D array
shape = (len(my_3d_array), len(my_3d_array[0]), len(my_3d_array[0][0]))
print(shape)