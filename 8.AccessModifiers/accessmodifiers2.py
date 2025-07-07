import Access_modifiers as acc
class parent:
	def __init__(self):
		self.a = 20
		self.b = 30
		self._code = self.a*self.b
		
	def access_other(self):
		cls = acc.Myclass()
		cls.access_private_members()
		
class T_child(parent):
	
	def __init__(self):
		m = acc.Parent()
		self.x = 10
		print(m._protected_field)
		m._protected_method()
		
print("\n")
c = T_child()


print("\n")

task = parent()
task.access_other()
