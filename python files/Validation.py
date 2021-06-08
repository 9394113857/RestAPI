import phonenumbers
from phonenumbers import carrier, timezone, geocoder, data

INDIA_CODE = "+91"
Phone_Number = 3394112233  # 5394112233 Its False
my_number = phonenumbers.parse(INDIA_CODE + str(Phone_Number), "IN")
# Getting Values from the Service:-
print("===============================================")
num = phonenumbers.is_valid_number(my_number)
print("1.Checking Given Number is Active or Not:", num)

#print() // separate line