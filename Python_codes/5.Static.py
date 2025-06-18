
# 1. Define a static variable and access that through a class  
class Shape:
	x = 0 # static variable
	y = 0 # static variable
	print(x)      #x=0
	
# 2. Define a static variable and access that through a instance 
Shape.x = 5          #changing x to 5
print(Shape.x)

# 3. Define a static variable and change within the instance 
instance = Shape()   #Creating instance for Shape class 
print(instance.x) 

# 4.Define a static variable and change within the class.
instance.x = 4      #Change object through instance = 4
print(instance.x) 	#gives 4
print(Shape.x) 		#gives 5
