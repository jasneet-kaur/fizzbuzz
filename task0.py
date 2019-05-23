import string 
str1= "Fizz"
str2="Buzz"
str3="FizzBuzz"


for number in range(100):
	if number%3==0:
		number=str1
	elif number%5==0:
		number=str2
	elif number%3==0 and number%5==0:
		number=str3
	print(number)


