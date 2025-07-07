""" Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method. """

class Myclass:
	def  __init__(self):
		self.__private_field = "I am private"
		
	def __private_method(self):
		print("This is a private method.")
		
	def access_private_members(self):
		print(self.__private_field)
		self.__private_method()
		
#Checking private accessible or not

obj = Myclass()
#obj.__private_method
"""  OUTPUT
  obj.__private_method  
 AttributeError: 'Myclass' object has no attribute '__private_method' 
"""
obj.access_private_members()
""" OUTPUT
I am private
This is a private method.
"""

# print(obj.__private_field)
"""
    print(obj.__private_field)
          ^^^^^^^^^^^^^^^^^^^
AttributeError: 'Myclass' object has no attribute '__private_field'
"""

''' Create a sub class and try to access the private fields and methods from sub class. '''
class Parent:
    def __init__(self):
        self.__private_field = "Secret Code"
        self._protected_field = "I am protected"

    def __private_method(self):
        print("This is a private method in Parent")

    def reveal(self):
        return self.__private_field
        
    def _protected_method(self):
        print("This is protected method")


class Child(Parent):
    def access_private_in_child(self):
        try:
            # Attempting to access private members directly
            print(self.__private_field)        # 🚫 Will raise AttributeError
            self.__private_method()            # 🚫 Will raise AttributeError
        except AttributeError as e:
            print(f"Access denied: {e}")

        # ✅ But you *can* access indirectly via Parent's public method
        print("Using Parent's method:", self.reveal())

        # ✅ Or, access using name mangling (not recommended in practice)
        print("Using name mangling:", self._Parent__private_field)
        self._Parent__private_method()

class Sibling: #Another class  Sibling in same module accessing _protected members
	def __init__(self):
		p = Parent()
		print(p._protected_field)
		p._protected_method()
	
# 🔰 Main execution block

obj = Child()
obj.access_private_in_child()

s = Sibling()




