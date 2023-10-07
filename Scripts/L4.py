# Lecture 4 script

# S1
# sudoku_list is a Python list containing a sudoku game
sudoku_list =  [[0, 0, 4, 3, 0, 0, 2, 0, 9],
               [0, 0, 5, 0, 0, 9, 0, 0, 1],
               [0, 7, 0, 0, 6, 0, 0, 4, 3],
               [0, 0, 6, 0, 0, 2, 0, 8, 7],
               [1, 9, 0, 0, 0, 7, 4, 0, 0],
               [0, 5, 0, 0, 8, 3, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 1, 0, 5],
               [0, 0, 3, 5, 0, 8, 6, 9, 0],
               [0, 4, 2, 9, 1, 0, 3, 0, 0]]
               
               
# Import NumPy
import numpy as np

# Convert sudoku_list into an array
sudoku_array = np.array(sudoku_list)

# Print the type of sudoku_array 
print(type(sudoku_array))

# S2
# Create an array of zeros which has four columns and two rows
zero_array = np.zeros((2, 4))
print(zero_array)

# Create an array of random floats which has six columns and three rows
random_array = np.random.random((3, 6))
print(random_array)

# S3
# get plt + edited/added
!pip install matplotlib
from matplotlib import pyplot as plt
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Create an array of integers from one to ten
one_to_ten = np.arange(1, 11)
one_to_ten

# Create your scatterplot
plt.scatter(one_to_ten, doubling_array)
plt.show()

# S4

# check the current working directory
import os
print(os.getcwd())
# change the current working directory
import os
print(os.getcwd())
os.chdir('[path]')
print(os.getcwd())

# edited/added
sudoku_solution = np.load('sudoku_solution.npy')
sudoku_list = np.load('sudoku_game.npy')
sudoku_game = np.array(sudoku_list)

# Create the game_and_solution 3D array
game_and_solution = np.array([sudoku_game, sudoku_solution])

# Print game_and_solution
print(game_and_solution) 

#S5
# Import NumPy
import numpy as np

# edited/added
sudoku_game = np.load('sudoku_game.npy')

# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Reshape flattened_game back to a nine by nine array
reshaped_game = flattened_game.reshape((8, 9))

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)


#S6
# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3, 2))

# Print the data type of zero_array
print(zero_array.dtype)

# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3, 2))

# Print the data type of zero_array
print(zero_array.dtype)

# Create a new array of int32 zeros with three rows and two columns
zero_int_array = np.zeros((3, 2), dtype=np.int32)

# Print the data type of zero_int_array
print(zero_int_array.dtype)

#S7
import numpy as np

# create an array of  integers
int_array = np.array([-3, -1, 0, 1])

# create an array of floating-point numbers
float_array = np.array([0.1, 0.2, 0.3])

# create an array of complex numbers
complex_array = np.array([1+2j, 2+3j, 3+4j])

# check the data type of int_array
print(int_array.dtype)  # prints int64

# check the data type of float_array
print(float_array.dtype)  # prints float64

# check the data type of complex_array
print(complex_array.dtype)  # prints complex128


#S8
import numpy as np
# A string data type
print(np.array([78.988, "NumPy", True]).dtype)
print(np.array([9, 1.12, True]).astype("<U5").dtype)

# An integer data type
print(np.array([34.62, 70.13, 9]).astype(np.int64).dtype)
print(np.array([45.67, True], dtype=np.int8).dtype)

# A float data type
print(np.array([[6, 15.7], [True, False]]).dtype)
print(np.random.random((4, 5)).dtype)

#S9
# edited/added
sudoku_game = np.load('sudoku_game.npy')

# Print the data type of sudoku_game
print(sudoku_game.dtype)

# Change the data type of sudoku_game to int8
small_sudoku_game = sudoku_game.astype(np.int8)

# Print the data type of small_sudoku_game
print(small_sudoku_game.dtype)

#S10
# edited/added
tree_census = np.load('tree_census.npy')

# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]

# Print the first five block_ids
print(block_ids[:5])

# Select the tenth block ID from block_ids
tenth_block_id = block_ids[9]
print(tenth_block_id)

# Select five block IDs from block_ids starting with the tenth ID
block_id_slice = block_ids[9:14]
print(block_id_slice)

#S11
# Create an array of the first 100 trunk diameters from tree_census
hundred_diameters = tree_census[:100, 2]
print(hundred_diameters)

# Create an array of trunk diameters with even row indices from 50 to 100 inclusive
every_other_diameter = tree_census[50:101:2, 2]
print(every_other_diameter)

#S12
# Extract trunk diameters information and sort from smallest to largest
sorted_trunk_diameters = np.sort(tree_census[:, 2])
print(sorted_trunk_diameters)

#S13
# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)

# Slice largest_tree_data to get only the block id
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)

# Create an array which contains row data on all trees with largest_tree_block_id
trees_on_largest_tree_block = tree_census[tree_census[:, 1] == largest_tree_block_id]
print(trees_on_largest_tree_block)

#S14
# Create the block_313879 array containing trees on block 313879
block_313879 = tree_census[tree_census[:, 1] == 313879]
print(block_313879)

# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:, 1] == 313879)

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879)

#S15
# Create and print a 1D array of tree and stump diameters
trunk_stump_diameters = np.where(tree_census[:, 2] == 0, tree_census[:, 3], tree_census[:, 2])
print(trunk_stump_diameters)

#S16
# edited/added
new_trees = np.array([[1211, 227386, 20, 0], [1212, 227386, 8, 0]])

# Print the shapes of tree_census and new_trees
print(tree_census.shape, new_trees.shape)

# Add rows to tree_census which contain data for the new trees
updated_tree_census = np.concatenate((tree_census, new_trees))
print(updated_tree_census)

#S16
# Print the shapes of tree_census and trunk_stump_diameters
print(trunk_stump_diameters.shape, tree_census.shape)

# Reshape trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((1000, 1))

# Concatenate reshaped_diameters to tree_census as the last column
concatenated_tree_census = np.concatenate((tree_census, reshaped_diameters), axis=1)
print(concatenated_tree_census)

#S17
# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census, 3, axis=1)

# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census[:,1] == 313879)

# Delete the rows for trees on block 313879 from tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps, private_block_indices, axis=0)

# Print the shape of tree_census_clean
print(tree_census_clean.shape)

#S18
import numpy as np

# data
security_breaches = np.array([[0,5,1],
                              [0,2,0],
                              [1,1,2],
                              [2,2,1],
                              [0,0,0]])
security_breaches

# Summing Data
security_breaches.sum()

# sum the values of all rows in each column to create column totals
security_breaches.sum(axis=0)

# Find the minimum value of each column
security_breaches.min(axis=0)

# Find the maximum value of each column
security_breaches.max(axis=0)

# Find the mean of each column
security_breaches.mean(axis=0)

# Cumulative sum
security_breaches.cumsum(axis=0) # column sum
security_breaches.cumsum(axis=1) # raw sum

#S18

array = np.array([[1, 2, 3], [4, 5, 6]])
array + 3 # adding 3 to all elements in array

array * 2 # multiplying by 2 to all elements in array

# Adding two arrays together
array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[0, 1, 0], [1, 0, 1]])
array_a + array_b

# Multiplying two arrays together
array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[0, 1, 0], [1, 0, 1]])
array_a * array_b

#S19

array = np.array(["NumPy", "is", "awesome"])
vectorized_len = np.vectorize(len)
vectorized_len(array) > 2

vectorized_upper = np.vectorize(str.upper)
vectorized_upper(array)

vectorized_lower = np.vectorize(str.lower)
vectorized_lower(array)

#S20

# loading data
with open("rgb_array.npy","rb") as f:
    logo_rgb_array = np.load(f)
logo_rgb_array

# Display the array as image 
!pip install matplotlib
import matplotlib.pyplot as plt
plt.imshow(logo_rgb_array)
plt.show()

#S21

# Display the documentation for .astype()
help(np.ndarray.astype)


#S22

# Reduce every value in logo_rgb_array by 50 percent
darker_rgb_array = logo_rgb_array * 0.5
print(darker_rgb_array)

#S23

# Save darker_rgb_int_array to an .npy file called darker_monet.npy
with open("darker_monet.npy", "wb") as f:
    np.save(f, darker_rgb_array)
    
#S24

# Flipping
array = np.array([[1.1, 1.2, 1.3],
                  [2.1, 2.2, 2.3],
                  [3.1, 3.2, 3.3],
                  [4.1, 4.2, 4.3]])
np.flip(array)
np.flip(array, axis = 0) # raws bottom -> top
np.flip(array, axis = 1) # column right -> left

#S25

array

np.transpose(array)



