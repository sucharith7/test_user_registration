import re
class ValidateUser:

	def firstName(self,Fname):
		match=re.match(r'^[A-Z]{1}[a-z]{2,}$',Fname)
		if match:
			return "matched"
		else:
			return "not matched"