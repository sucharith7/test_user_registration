import pytest
from ValidateUser import ValidateUser


class Test_userValidator:

	def test_GivenFname_Whenmatch_Should_ReturnTrue(self):
		validator=ValidateUser()
		result=validator.firstName("Suchi")
		assert result == "matched"


	
