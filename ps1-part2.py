#Create a function called number_fun that takes two integers as parameters.
def number_fun(a: int,b: int):
    #Repeat back to the user the two integers that they entered.
    print(f'You entered {a} and {b}')
    #Create a variable to calculate the sum of both parameters.
    sum = a + b
    #Print out their sum.
    print(f'{a} + {b} = {sum}')
    #Create a variable to calculate the product of both parameters.
    product = a*b
    #Print out their product.
    print(f'{a} * {b} = {product}')
    #Create a variable to calculate the first number raised to the second number.
    power = a**b
    #Print out the first number raised to the power of the second number.
    print(f'{a} ** {b} = {power}')
    #Create a variable to calculate the remainder of dividing the first by the second number.
    remainder = a % b
    #Print out the remainder you get when you divide the first number by the second number.
    print(f'{a} % {b} = {remainder}')

#Ask the user for an integer between 10 and 100. Save that to a variable called firstnum.
firstnum = int(input(f'Enter an integer in between 10 and 100.'))
#Ask the user for a second integer that is less than 4. Save that to a variable called secondnum.
secondnum = int(input(f'Enter an integer that is less than 4.'))
#Call the number_fun() function, passing in firstnum and secondnum as the arguments.
number_fun(firstnum,secondnum)

