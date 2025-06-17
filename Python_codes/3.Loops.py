#1. Write a program to print “Bright IT Career” ten times using for loop


i=0
for i in range(10):
    print("Bright IT Career")
# 2. Write a java program to print 1 to 20 numbers using the while loop.
j=1
while j<=20:
    print(j)
    j += 1

# 3. Program to equal operator and not equal operators

x,y,z = 10, 20 , 30
if(x == 10 and z != 20):
    print("equal operator and not equal operators are working")


# 4. Write a program to print the odd and even numbers in given range.
print("\n Odd and even numbers in given range")
max_num = int(input('enter the max number: '))
even_num = ['Even numbers :']
odd_num = ['Odd numbers :']
for num in range(1,max_num):
    if(num%2 == 0):
        even_num.append(num)
    elif(num%2 == 1):
        odd_num.append(num)
print('Odd numbers',odd_num[1:])
print('Even numbers',even_num[1:])

#5. Write a program to print largest number among three numbers

x,y,z = 10,50,15
large = 0
if x >= y and x >= z:
    large = x
elif y>=z and y>=x:
    large = y
elif z>=x and z>=y:
    large = z
print("\nLargest among the numbers",x,y,z)
print(large)

'''6. Write a program to print even number between 10 and 20 using while'''
N = 10
print('\neven numbers using while loop between 10 and  20')
while N in range(20):
    N += 1
    if(N%2 == 0):
        print(N,end = " ")

'''7. Write a program to print 1 to 10 using the do-while loop statement'''

    # do-while loop doesn't exists in python


"""8. Write a program to find Armstrong number or not
"""

"""Armstrong number : a number that is equal to the sum of power_base_n of its own digits..
   for example : 153, 1^3 + 5^3 + 3^3 = 153
                1634, 1^4 + 6^4 + 3^4 + 4^4 = 1634
"""
print("\n ------------------- Armstrong number ----------------------")
a_n = input('enter a number: ')
p = len(a_n)
temp = []
for i in a_n:
    temp.append(int(i)**p)
if sum(temp)== int(a_n):
    print("Given number",a_n,"is Armstrong number :)")
else:
    print("Given number ",a_n,"is Not a Armstrong number :(")

"""9. Write a program to find the prime or not."""
print("\n----------- Prime number or Not -----------------")
i_num = int(
input('enter a number: '))
value = 0
f = []
for value in range(2,i_num):
    if(i_num % value == 0):
        f.append(value)
#print(f)
if f == []:
    print(i_num," is a prime")
else:
    print(i_num," is not prime")
    


"""10. Write a program to palindrome or not"""
print("\n----------- Palindrome or Not -----------------")
word = input('enter something: ')
reverse_word = ""
    #print(word[0:])
for j in word:
    reverse_word = j + reverse_word
    #print(reverse_word)
if (reverse_word==word):
    print("the given string '",word,"'is palindrome")
else:
    print("the given string '",word,"'is not palindrome")
    


"""11. Program to check whether a number is EVEN or ODD using switch"""

print("\n----------- GIVEN NUMBER IS EVEN or ODD using match-case -----------------")
i_num = int(input("Enter the number to check: \n"))
C = int(input("Enter '1' to check even \nEnter '2' to check odd : "))
match C:
    case 1:
              if (i_num % 2 == 0):
                  print(i_num," is even")
              else:
                  print(i_num," is not even")
    case 2:
              if (i_num % 2 != 0):
                  print(in_num," is odd")
              else:
                  print(in_num," is not odd")

"""12. Print gender (Male/Female) program according to given M/F using switch"""
print("\n----------- Print gender (Male/Female) program according to given M/F using switch -----------------")
C = input("Collecting gender information\nEnter 'M' for Male \nEnter 'F' for Female : ")
cin = ''
if C == 'M':
    cin = 1
elif C == 'F':
    cin = 2
match cin:
    case 1:
        print("The gender is \tMale")
    case 2:
        print("The gender is \tFemale")
