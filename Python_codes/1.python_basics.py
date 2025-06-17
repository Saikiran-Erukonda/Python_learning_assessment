#1. Python Basics
'''1. Write a program to print your name'''
print("E Saikiran")

'''2. Write a program for a Single line comment and multi-line comments
'''

#this is a single line comment starts with symbol <hashtag> '#'

''' This is a multi ine commment starts and ends with three single apostrophe
    or we can use """ at beginning and ending
'''

'''3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.'''
# In python we don't need to define the variable datatype, python itself identifies the data_type of variable.
x = 6
y = True
name = 'Meow'
z = 0.52
h = complex(560.5,2)

print("Type of x",type(x))         #int
print("Type of y",type(y))         #bool
print("Type of name",type(name))   #char
print("Type of z",type(z))         #float
print("Type of h",type(h))         #complex

'''4. Define the local and Global variables with the same name and print both variables and
understand the scope of the variables'''

g = 5
def f():
    print("\nThe global Variable")
    print("The value of g: ", g)
l = 5
def l():
    l=10
    print("\nThe local Variable")
    print("the value of l: ",l,"\nThe value assigned inside is diplayed")
    
#call the function to execute print statements inside functions
f()
l()