# define the shape of the n-dimensional array
dimensions = [int(dim) for dim in input("Enter the dimensions of the array: ").split()]

# create the n-dimensional array using the nested lists
def create_n_dimensional_array(dimensions):
    if len(dimensions) == 1:
        return [0] * dimensions[0]
    else:
        return [create_n_dimensional_array(dimensions[1:]) for _ in range(dimensions[0])]
    
my_n_dimensional_array = create_n_dimensional_array(dimensions)

# access an element of the n-dimensional array
indices = [int(idx) for idx in input("Enter the indices of the element to access: ").split()]
element = my_n_dimensional_array
for idx in indices[:-1]:
    element = element[idx]
print(element)

# update an element of the n-dimensional array
value = int(input("Enter the new value of the element: "))
element = my_n_dimensional_array
for idx in indices[:-1]:
    element = element[idx]
if isinstance(element, list):
    element[indices[-1]] = value
else:
    raise ValueError("Invalid index")
print(my_n_dimensional_array)

# get the shape of the n-dimensional array
def get_shape(array):
    shape = []
    while type(array) == list:
        shape.append(len(array))
        array = array[0]
    return tuple(shape)

shape = get_shape(my_n_dimensional_array)
print(shape)