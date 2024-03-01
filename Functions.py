# def my_function():
#   print("Hello from a function")

# calling function 
# my_function()

# Argument Passing
# def my_function(name):
#   print(name + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# This function expects 2 arguments, and gets 2 arguments:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")


# This function expects 2 arguments, but gets only 1 , it is not possible and get ERROR:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# I call function without passing an argument it will take default argument "Norway" automatically
# my_function()  
# my_function("Brazil")


# Passing a List as an Argument

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# To let a function return a value, use the return statement:

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# Function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the "pass statement" to avoid getting an error.

# def myfunction():
#   pass

