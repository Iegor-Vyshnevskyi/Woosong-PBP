# Practical Business Python
# Lecture 3: Built-In Data Structures, Functions, and Files


## 1.1. Tuple
# A tuple is a fixed-length, immutable sequence of Python objects which, once assigned, cannot be changed. 

# Example
mytuple = ("apple", "banana", "cherry")

# Example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

# Example
thistuple = ("apple",)
print(type(thistuple))

# Example
# String, int and boolean data types, and mixed data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# Example
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Example
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4[0])
print(tuple4[-1])

# Example
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4])  
# elements beginning to 2nd
print(my_tuple[:-7]) 
# elements 8th to end
print(my_tuple[7:]) 
# elements beginning to end
print(my_tuple[:]) 

# Example 
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple2_3 = tuple2 + tuple3
print(tuple2_3)

# Example 
tuple2 = (1, 5, 7, 9, 3)
tuple2_2 = tuple2 * 2
print(tuple2_2)

# Example 
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple.count('r'))
print(my_tuple.index('o'))

## 1.2. List
# Create a list
# As opposed to int, bool etc., a list is a compound data type; you can group values together:

# Example
a = "is"
b = "short"
my_list = ["this", "list", a, b]
print(my_list)
my_list = list(("this", "list", a, b)) # note the double round-brackets
print(my_list)

# Example
# The areas of the different parts of your house are stored in separate variables for now, as shown in the script.
# area variables (in square meters)
hall = 12.45
kit = 17.0
liv = 30.0
bed = 13.55
bath = 11.50
# Create list areas
areas = [hall, kit, liv, bed, bath]
# Print areas
print(areas)


# Create list with different types
# A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types including strings, floats, booleans, etc.

# Example
# area variables (in square meters)
hall = 12.45
kit = 17.0
liv = 30.0
bed = 13.55
bath = 11.50
# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
# Print areas
print(areas)


# List of lists
# Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists.

# Example
# area variables (in square meters)
hall = 12.45
kit = 17.0
liv = 30.0
bed = 13.55
bath = 11.50
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)
# Print out the type of house
print(type(house))


# Subset and conquer

# Example
x = ["x", "y", "z", "a"]
x[1]
x[-3]

# Example
# Create the areas list
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Print out first element from areas
print(areas[0])
# Print out second last element from areas
print(areas[-2])
# Print out the area of the bedroom
print(areas[7])

# subset and calculate
# After you've extracted values from a list, you can use them to perform additional calculations. 
# The strings that result are pasted together using the + operator:

# Example
x = ["x", "y", "z", "a"]
print(x[0] + x[2])

# Example
# Create the areas list
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Sum of kitchen and living area: eat_live_area
eat_live_area = areas[3] + areas[-5]
# Print the variable eat_live_area
print(eat_live_area)


# Slicing and dicing
# It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:
# Example
x = ["x", "y", "z", "a"]
x[1:3] # The elements with index 1 and 2 are included, while the element with index 3 is not.

# Example
# Create the areas list
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Use slicing to create downstairs
downstairs = areas[:4]
# Use slicing to create upstairs
upstairs = areas[4:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Slicing and dicing (2)
# Example
x = ["x", "y", "z", "a"]
x[:3]
x[3:]
x[:]

# Example
# Create the areas list
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Alternative slicing to create downstairs
downstairs = areas[:6]
# Alternative slicing to create upstairs
upstairs = areas[6:]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


# Replace list elements
# Just subset the list and assign new values to the subset. 
# You can select single elements or you can change entire list slices at once.

# Example
x = ["x", "y", "z", "a"]
x[1] = "r"
print(x)
x[2:] = ["a", "b"]
print(x)

# Example
# Create the areas list
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Correct the bedroom area
areas[-3] = 13.75
# Change "hallway" to "play zone"
areas[0] = "play zone"
print(areas)


# Extend a list
# Example
x = ["x", "y", "z", "a"]
y = x + ["b", "c"]
print(y)

# Example
# Create the areas list and make some changes
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, 
         "bedroom", 13.55, "bathroom", 11.50]
# Add game zone data to areas, new list is areas_1
areas_1 = areas + ["game zone", 10.75]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)


# Delete list elements
# We can also remove elements from your list with the del statement:

# Example
x = ["x", "y", "z", "a"]
del(x[3])
print(x)

# Example
# From 'areas_2' we delete 'game zone' data
print(areas_2)
del(areas_2[-4:-2])
print(areas_2) 


# Copy list

# Create list areas
areas = ["hallway", 12.45, "kitchen", 17.0, "living room", 30.0, "bedroom", 13.55, "bathroom", 11.50]
# Create areas_copy
areas_copy = areas[:]
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas_copy)


# Sorting
# Example
x = ["x", "y", "z", "a"]
x.sort()
print(x)

# Example
w = ["saw", "small", "He", "foxes", "six"]
w.sort(key=len)
print(w)


# 1.3. Dictionary

# Example
empty_dict = {}
d1 = {"a": "some value", "b": [1, 2, 3, 4]}
print(type(d1))

# Example
d1[7] = "an integer"
print(d1)
d1["b"]

# Example
"b" in d1

# Example
d1[5] = "some value"
print(d1)
del(d1[5])
print(d1)
d1.pop("b")
d1


# 1.4. Set

# Example
set([2, 2, 2, 1, 3, 3])
{2, 2, 2, 1, 3, 3}

# Example
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.union(b) # union
a | b # union
a.intersection(b) # intersection
a & b # intersection



## 2. Functions
# In-built functions
# The general way for calling functions and saving the result to a variable is: output = function_name(input)

# Example
# Create variables v1 and v2
v1 = [10, 20, 30, 40]
v2 = True
# Print out type of v1
print(type(v1))
# Print out length of v1
print(len(v1))
# Convert v2 to an integer: out2
out2 = int(v2)


# Help!
# Example
help(max)

# Multiple arguments
# Example
# Create lists first and second
first = [14.55, 23.0, 5.0]
second = [17.30, 4.75]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)
# Print out full_sorted
print(full_sorted)


# String Methods

# Example
# string to experiment with: place
place = "game zone"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place); print(place_up)
# Print out the number of o's in place
print(place.count("o"))


# List Methods

# Example
# Create list areas
areas = [14.55, 23.0, 5.0, 17.30, 4.75]
# Print out the index of the element 5.0
print(areas.index(5.0))
# Print out how often 5.0 appears in areas
print(areas.count( 5.0))
# Use append twice to add poolhouse and garage size
areas.append(34.25)
areas.append(19.75)
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)


# Writing a function

# Example
def my_function(x, y):
   return x + y

my_function(5, 7)


# Import package

# Example
# Definition of radius
r = 0.87
# Import the math package
import math 
# Calculate C (the circumference of the circle)
C = 2 * math.pi * r # pi is fixed number ~3.14
# Calculate A (the area of the circle)
A = math.pi * (r**2) # '**' power operator
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Selective import

# Example
# Definition of radius
r = 0.87
# Import pi function of math package
from math import pi
# Calculate C (the circumference of the circle)
C = 2 * pi * r # pi is fixed number ~3.14
# Calculate A (the area of the circle)
A = pi * (r**2) # '**' power operator
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# Different ways of importing

# Example
from scipy.linalg import inv as my_inv



# 3. Files and the Operating System 

# Example
path = "C:/My docs/VScode_traning/MPS.txt"
f = open(path, encoding="utf-8")
for line in f:
    print(line)
f.close()






