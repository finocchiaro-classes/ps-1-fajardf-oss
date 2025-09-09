#Create a function called heartrate() that takes parameters age and goal as an integer and a string, respectively.
def heart_rate(age: int, goal: str):
    #Subtract the user's age from 220 to give their max heart rate, saved as a variable called max_HR.
    max_HR = 220 - age
    #Print out the user's max heart rate.
    print(f'Your maximum heart rate is: {max_HR}')
    #If function to separate the target heart rates from the users with different goals (S or E).
    #If the goal value is S, their target heart rate range is 80% to 100% of max_HR.
    if goal == "S":
        low = max_HR*.8
        print(f'Your target heart rate is between {low} and {max_HR}.')
   #If the goal value is E (else), their target heart rate range is 60% to 80% of max_HR.
    else:
        low2 = max_HR*.6
        bottom2 = max_HR*.8
        print(f'Your target heart rate is between {low2} and {bottom2}.')

#Ask the user their age, which you should save as a variable called user_age. See the example output below for the required wording.
user_age = int(input(f'What is your age?'))
#Ask the user if they want to improve speed (S) or endurance (E). Save the input as user_goal. See the example output below for the required wording.
user_goal = input(f'Is your goal (S) speed or (E) endurance?')
#Call the heart_rate() function you wrote above, passing in user_age and user_goal as the arguments.
heart_rate(user_age,user_goal)
