# Practical Business Python
# Lecture 2: Python Basics

## 1. First code example
# Example
3/9

print(3 / 9)

# Print the sum of 2 and 15
print(2 + 15)

## 1.1. Adding comments
# You can write any notes in your Python scripts. It helps to remember what you do and why you do it.
# Just remember to use the '#' comment marker and your notes won't be run as Python code.  
# See the '# Addition' comment .

# Division
print(3 / 9)

# Addition
print(2 + 15)


## 2. Python as a calculator
# Python can be used as a calculator.

# Addition, subtraction
print(3 + 8)
print(3 - 8)

# Multiplication, division, and exponentiation
print(2 * 7)
print(2 / 3)
print(2 ** 3)



## 2.1. Variable Assignment
# In Python, a variable enables you to associate a name with a specific value.
# To establish a variable called x and assign it the value 23, you employ the '=' operator, as demonstrated below:
x = 23

# Subsequently, you can employ the variable's name, x, in place of the actual value, 23.
# It's important to note that in Python, the '=' symbol is used for assignment, not for testing equality!

# Create a variable savings = 1000
savings = 1000

# Print out savings
print(savings)


## 2.2. Calculations with variables
# Rather than performing calculations with concrete values, you can utilize variables.
# Now that you've established a savings variable, let's begin the process of saving.

#Example: If you set aside $10 every month, how much money will you have saved four months down the line?

# Create a variable savings
savings = 1000

# Create a variable growth_multiplier
growth_multiplier = 1.01

# Calculate result
result = 1000*(1.01**4)

# Print out result
print(result)


## 3. Variables' types
# In the previous exercise, you worked with the integer Python data type:

# int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
# Next to numerical data types, there are three other very common data types:

# float, or floating point: a number that has both an integer and fractional part, separated by a point. 1.1, is an example of a float.
# str, or string: a type to represent text. You can use single or double quotes to build a string.
# bool, or boolean: a type to represent logical values. It can only be True or False (the capitalization is important!).

# Example:

# Create a float variable 'quarter'
quarter = 0.25

# Create a string variable 'intro'
intro = "Hello! What's up?"

# Create a boolean variable 'is_fine'
is_fine = True

# 3.1. Operations with other types
# Different types behave differently in Python.
# For instance, when you perform addition with two strings, the outcome will differ from adding two integers or two booleans.

# Example:

# Calculate year_savings using monthly_savings and num_months
monthly_savings = 10
num_months = 24
year_savings = monthly_savings * num_months

# Print the type of year_savings to see the type of the variable
print(type(year_savings))

# Assign sum of intro and intro and intro to tripleintro
intro = "Hello! What's up?"
tripleintro = intro + intro + intro

# Print out doubleintro
print(tripleintro)

# 3.2. Type conversion
# Using the '+' operator to concatenate/merge two strings can be extremely valuable for constructing custom messages.
# Imagine, for instance, that you've computed your savings and wish to present the results as a string.
# To achieve this, you'll need to convert the types of your variables explicitly. To be precise, you can use 'str()' to convert a value into a string. 
# For instance, 'str(savings)' will convert the integer savings into a string.
# Similar functions like 'int()', 'float()', and 'bool()' are available to assist you in converting Python values into various data types as needed.

# Example:

# Definition of savings and total_savings. Merging in string.
savings = 1000
total_savings = 1430
print("I had $" + str(savings) + " and now have $" + str(total_savings) + ". Great!")

# Convert pi_string into float
pi_float = 3.1415926
pi_int = int(pi_float)
print(pi_int)


