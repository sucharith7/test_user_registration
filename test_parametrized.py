import pytest
from ValidateUser import ValidateUser 

testmail=[["abc@yahoo.com","valid"],
["abc.com","invalid"],
["abc-100@yahoo.com","valid"],
[".abc@yahoo.com","invalid"],
["abc.100@yahoo.com","valid"],
["abc@gmail.c","invalid"],
["abc111@abc.com","valid"],
[".abc111@.com","invalid"],
["abc-100@abc.net","valid"],
[".abc@com.com","invalid"],
["abc.100@abc.com.au","valid"],
["abc()*@gmail.com","invalid"],
["abc@1.com","valid"],
["abc@%*.com","invalid"],
["abc@gmail.com.com","valid"],
["abc..2002@gmail.com","invalid"],
["abc+100@gmail.com","valid"],
["abc.@gmail.com","invalid"]]

@pytest.mark.parametrize("mail,expected",testmail)
def test_mail_validator(mail,expected):
	validator=ValidateUser()
	result=validator.emailId("cat.dog@cd.co.in")
	assert result == "matched"