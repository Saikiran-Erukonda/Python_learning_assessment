# 1. Different ways creating a string

a = "a"  #directly assigning
b = input("Enter something..:  ")  #by inputing
print(a, type(a))
print(b, type(b))

#2. Concatenating two strings using + operator 
print("\n Using concatenating Operator")
First_name = "Saikiran"
last_name = "_Erukonda"
Full_name = First_name + last_name
print("The Full name: ",Full_name)

#3. Finding the length of the string
print(Full_name,"\n The length of string Full_name", len(Full_name))


#4. Extract a string using Substring
print(Full_name[0:8])

#5. Searching in strings using index()
print(Full_name.index("n",0,17)) #returns 1st position were  

#6. Matching a String Against a Regular Expression With matches() 

Full_name = "Saikiran_Erukonda"
import re
re.fullmatch("sa",Full_name)                 #returns None
print(re.fullmatch("Saikiran",Full_name))  #returns None
print(re.fullmatch("Saikiran_Erukonda",Full_name)) 
''' Output :     <re.Match object; span=(0, 17), match='Saikiran_Erukonda'>'''

# 7. Comparing strings
string_1 = "India" 
string_2 = "India is our country     "
print(string_1== string_2)

#8. startsWith(), endsWith() and compareTo() 
print(string_1.startswith("I"))
print(string_1.endswith("a"))  #These comparisons are lexicographical, just like Java’s compareTo(), based on Unicode values.
print(string_1 < string_2)    #These comparisons are lexicographical, just like Java’s compareTo(), based on Unicode values.

print(string_1 > string_2) 

#9. Trimming strings with strip() 

print(string_2.strip())

#10. Replacing characters in strings with replace()
string = string_2.replace("our","my")
print(string)

# 11. Splitting strings with split()
print(list(string.strip().split(" ")))  #removes extraspaces at ends and splits ..00000000000000000000000000000.0............................00000000000000000

# 12. Converting integer objects to Strings 
num = 215
num_1 = str(num)
print(num_1)
print(type(num_1))

# 13. Converting to uppercase and lowercase 
state = "TELANGANA"
city = "hyderabad"
print(state.lower()) #converts to lowercase
print(city.upper()) #converts to uppercase
