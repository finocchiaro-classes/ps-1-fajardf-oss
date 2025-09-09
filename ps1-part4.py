#The amount of points before answering the questions
points = 0
#Ask the user for the number of prior arrests
prior = int(input(f'Prior arrests: '))
    #Adding a point for users with 2 or more prior arrests
if prior >= 2:
    points += 1
#Adding another point for users with 5 or more prior arrests
if prior >= 5:
    points += 1
            
#Ask the user whether there are prior arrests for a local ordinance
local = input(f'Prior arrests for local ordinance (Y/N): ')
#Adding a point for users with prior arrests for a local ordinance
if local == "Y":
    points += 1
#Ask for the individual's age at release
release_age = int(input(f'Age at release: '))
#Adding a point for users with age at release 18 to 24
if 18 <= release_age <= 24:
    points += 1
#Subtracting a point for users with age at release of greater than or equal to 40
if release_age >= 40:
    points -= 11
#Printing the recidivism score for the user
print(f'The recidivism score is {points}')
