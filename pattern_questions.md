# **Pattern Problems**
## 1. Square Star pattern
``` python
#square pattern
def square_pattern(a):
	for i in range(a):
		print("*" * a)

input_size = input("Enter a number : ")
#print(type(input_size))
square_pattern(int(input_size)) #change data type from string to Integer

```
## 2. Inverted Pyramid Star Pattern
``` python
''' INverted  pyramid pattern
*|*|*|*|*|*|*|
 |*|*|*|*|*|
   |*|*|*|
     |*|
	
///////////////////////'''
def inverted_square_pyramid(n_rows):
	space  = 0										#to add identation from second line
	for row in range(n_rows):
		print(" " * space,"*"* (2*n_rows-1))  		#first row 4lines therefore 7stars (2*4-1)
		space = space + 1 							#to add identation from seond line
		n_rows = n_rows - 1 						# to decrease the no.of stars from second line
		
		
no_of_lines = input("enter the height of triangle: ")	 #enter number of lines to print
inverted_square_pyramid(int(no_of_lines))				 #changed DT String >> int
```

## 3. Pyramid Star pattern
``` python
PYRAMID STAR PATTERN
			|*|
		  |*|*|*|
		|*|*|*|*|*|
	  |*|*|*|*|*|*|*|
----------------------------'''
def pyramid_pattern(n_rows):
	space = n_rows - 1 							# space decreases for every iteration		
	for row in range(n_rows):					# loop executes n_row times
		print(" " * space,"*"  * (2*row -1)) 	# consider row number for printing star
		space = space-1							# space decreases for every iteration
		
no_of_lines = input("enter the height of triangle: ")
pyramid_pattern(int(no_of_lines)) #changed DT String >> int
```
## 4. Diamond star pattern
``` python
""" DIAMOND SQUARE PATTERN
    *
   ***
  *****
 *******
  *****
   ***
    *
"""

def diamond_square(size_n):			
	space = 0											#for second part space
	for row in range(1,(2*size_n)):						#iterates 2n-1 times
		if(row <size_n):								#for first 3 lines if block
			print(" " * (size_n-row)+"*" * (2*row-1))	#space is related to row number ,star is also related as 2*row-1
		else:
			print(" " * space+"*"*(2 * size_n - 1))		#space is seperate variable increase line by line, star is related to size_n square (2*n-1)
			size_n = size_n-1							#no.of stars need to be decreased
			space  = space + 1							#space is increase for each iteration 
			
			
			
length_of_square  = input("Enter the length of square: ")
diamond_square(int(length_of_square))
		
```
## 5. Hallow Square star pattern
``` python
"""Hollow square  pattern
	*******
	*     *
	*     *
	*     *
	*     *
	*     *
	*******
"""
def hollow_square(size_n):
	space = size_n - 2
	for row in range(1,size_n+1):			#row iterates for  1 to size_n
		if(row  == 1 or row == size_n):		#for 1st and last row size_n star prints
			print("*" * size_n)				
		else:								#middle rows were filled with space
			print("*"+" " * space+"*")   	#concatinating the space and star
			
			
length = input("Enter length of the square: ")
hollow_square(int(length))
```
## 6. Butterfly pattern
``` python
"""  BUTTERFFLY PATTERN
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
--------------------------------------"""

def butterfly(size_n):
	space = 1
	for row in range(1,2*size_n):
		if(row <= size_n):
			print("*"*row+" "*((2*size_n)-(2*row))+"*"*row)
		else:
			print("*"*(size_n-1)+" "*2*space+"*"*(size_n-1))
			space= space+1
			size_n = size_n-1
			
butterfly_nsize = input("Enter Butterfly size:  ")
butterfly(int(butterfly_nsize))
```
## 7. Downward Right angle triangle pattern
``` python
"""Downward right angle triangle"
*|*|*|*|*|*|*   row 1 ---     7star
*   	  *     row 2 4spaces 2star   n-3
*       *       row 3 3spaces 2star   n-4
*     *			row 4 2spaces 2star   n-5
*   *			row 5 1spaces 2star   n-6
* *				row n-1 0spaces 2star n-7
*				row n  1star   
------------------"""

def downward_R_triangle(height):
	space = height-3
	for row in range(1,height):
		if(row==1):
			print("*"*height)
		if(row==height-1):
			print("*")
		else:
			print("*"+" "*space+"*")
			space = space-1
			
height_of_triangle = input("Enter the size of triangle: ")
downward_R_triangle(int(height_of_triangle))
```
## 8. Hallow Diamond star
``` python
""" Hallow diamond star
				spaces	innerspace star    row
    *			3		 0			1		1
   *_*			2		 1			2		2
  *___*			1		 3			2		3
 *_____*		0		 5			2		4
  *___*			1		 3			2		5
   *_*			2		 1			2		6
    *			3		 0			1		7
------------------------------------"""
def hallow_diamond_star(size_n):
	squarelength = size_n
	space = 1
	space_2 = 1
	for row in range(1,2*size_n):
		
		if(row == 1 or row == (2*squarelength-1)):             #row=1,2*len-1 only 1 star
			print(" "*(squarelength-1)+"*")
		elif(row <= size_n):
			print(" "*(size_n-row)+"*"+" "*((2*space)-1)+"*")  #row < 4 space =size_n-row
			space = space + 1
		else:
			space =size_n-2
			print(" " * space_2+"*"+" "*((2*space)-1)+"*")
			size_n = size_n-1 
			space = space-1
			space_2 = space_2 +1

length = input("Enter the length of the square: ")
hallow_diamond_star(int(length))
```
## 9. Cross star pattern
``` python
"""cross star pattern
    *
    *
*|*|*|*|*
    *
    *
"""

def cross_star(lines):
	for line in range(2*lines-1):
		if(line != lines-1):
			print(" " * (lines-1)+"*"+" " * (lines-1))
		else:
 			print("*" * ((2*lines) -1))

a = input("enter the number: ")
cross_star(int(a))
```
## 10. Hallow pyramid star pattern
``` python
""" hallow pyramid star pattern
    *
   * *
  *   *
 *******
 --------------""" 
def hallow_pyramid_star(height):
	i_space = 1
	for row in range(1,height+1):
		if(row == 1):
			print(" "*(height-row)+"*")
		elif(row < height):
			print(" " *(height-row)+"*"+" "*((2*i_space)-1)+"*")
			i_space = i_space + 1
		else:
			print("*"*(2*height-1))

length = input("Enter the length of the square: ")
hallow_pyramid_star(int(length))
```
