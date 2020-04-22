import re
class ValidateUser:

	def firstName(self,Fname):
		match=re.match(r'^[A-Z]{1}[a-z]{2,}$',Fname)
		if match:
			return "matched"
		else:
			return "not matched"


	def lastName(self,Lname):
		match=re.match(r'^[A-Z]{1}[a-z]{2,}$',Lname)
		if match:
			return "matched"
		else:
			return "not matched"


	def emailId(self,Email):
		match=re.match(r'^[a-z]{3,}(|[.|+|-]?[0-9a-zA-Z]+)([@])([a-z0-9]+)([.|+|_][a-z]{2,4})(|[.][a-zA-Z]{2,3})$',Email)
		if match:
			return "matched"
		else:
			return "not matched"