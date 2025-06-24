#1. A is a super class. B is a sub class of A. C is a sub class of B. 

#2. Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C 
class C:
    def __init__(self, a, b):
        self.in1 = a
        self.in2 = b
    def and_gate(self):
        return self.in1 and self.in2
    def or_gate(self):
        return self.in1 or self.in2
    def describe(self):
        return "This is class C"


class B(C):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.in3 = c
    def and_gate(self):
        return self.in1 and self.in2 and self.in3
    def or_gate(self):
        return self.in1 or self.in2 or self.in3
    def describe(self):
        return "This is class B"


class A(B):
    def __init__(self, a, b, c, d, s1, s0):
        super().__init__(a, b, c)
        self.in4 = d
        self.s0 = s0
        self.s1 = s1
    def mux(self):
        # Implementing a 4-to-1 multiplexer
        selector = (self.s1 << 1) | self.s0  
        print(selector)
"""
1.  self.s1 << 1:
This performs a left bitwise shift on s1, moving it one place to the left in binary.
For example:
- If s1 = 1, then 1 << 1 becomes 10 in binary → which is 2 in decimal.
- If s1 = 0, then 0 << 1 stays 0.

2. self.s0:
This is a bitwise OR operation. It takes the result of (s1 << 1) and combines it with s0.
So it merges the two selector bits into a two-bit number.
"""
        # Convert s1, s0 to integer (00 to 11)
        inputs = [self.in1, self.in2, self.in3, self.in4]
        print(inputs)
        return inputs[selector]   
    def describe(self):
        return "This is class A"
		
""" Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance. """

# Call an overridden method with super class reference to B and C class’s objects
print("2-input AND gate")
obj = C(1,1)	
andgate = obj.and_gate()
print("Output of AND gate  of 1 , 1 : ",andgate)
print(obj.describe())

print("\n3-input OR gate ")
obj2 = B(0,1,1)
orgate = obj2.or_gate()
print(obj2.describe())
print("Output of Or gate 0 1 1  : ",orgate)

print("\n4:1 Mux , first 4 inputs and last two selection bits")
obj3 = A(1,0,1,1,0,1)
mux = obj3.mux()
print("O/p of mux: ", mux)
print(obj3.describe())

"""
Python does not override instance variables at runtime in the way methods are overridden. So even if all three classes have a variable like self.in1, the one defined in the most derived class (like A) doesn’t override C’s version—it simply redefines it in that context.
In other words:
- If you call a method from a base class that accesses self.in1, it will use the value bound in that instance, not a "redefined" version in a subclass.
- There's no polymorphic resolution of data members, only of methods.
"""
