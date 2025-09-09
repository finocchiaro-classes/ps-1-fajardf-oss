#Created the first input of an integer between 10 and 100
firstnum = int(input("Submit an integer in between 10 and 100."))
#Created the second input of an integer less than 4
secondnum = int(input("Submit an integer that is less than 4."))
#Repeat back to the user the two integers that they entered.
print(f'You entered {firstnum} and {secondnum}')
#Create a variable for the sum of both numbers.
sum = firstnum + secondnum
#Print out their sum.
print(f'{firstnum} + {secondnum} = {sum}')
#Create a variable for the product of both numbers.
product = firstnum*secondnum
#Print out their product.
print(f'{firstnum} * {secondnum} = {product}')
#Create a variable to raise the first number to the power of the second.
power = firstnum**secondnum
#Print out the first number raised to the power of the second number.
print(f'{firstnum} ** {secondnum} = {power}')
#Create a variable for the remained of the division of the first number by the second number.
remainder = firstnum % secondnum
#Print out the remainder you get when you divide the first number by the second number.
print(f'{firstnum} % {secondnum} = {remainder}')

