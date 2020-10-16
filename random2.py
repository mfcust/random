import random

# 1a) Copy and paste the code from the markdown file and run it multiple times. What is the code doing? What do the numbers inside the parentheses represent?





# 1b)Generate a random number between -100 and 100 and store it as variable rand_num. Write a program that prints "That number is negative!" if the random number generated
#is less than zero, "The number is zero!" if the random number generated is equal to zero, and "That's a positive number!" for all other cases. Hint: You need an if, elif
#and else statement.







# 2a)The random library uses a pseudo-random number generator to calculate a random number. This means that random.randint() isn't giving you a TRULY random number, but
#it's as close as a computer can get. The pseudo-random number generator depends on a 'seed,' or starting point to perform the calculation. If you set the seed to be
#the same, then the random number that's generated will always end up being the same. Uncomment the code below and run it a couple of times. What do you observe?
#What happens if you change the range? What happens if you change the seed?

#random.seed(10)
#x = random.randint(0,1000)





#The line of code underneath resets random so that it doesn't have a fixed seed. Don't delete this!
random.seed()

# 3a) What if I wanted to generate a random integer between two values, but it has to be a multiple of 5? We can use the function random.randrange(). We can give it
#three parameters that represent the min, max and STEP. Uncomment the code below, run it a couple of times. What does each parameter in the parentheses represent?:

#y = random.randrange(1,1000,5)
#print(y)



# 3b) Generate a random integer between -500 and 500 that is a multiple of 3:




# 3c) What if I want to generate a random FLOAT number? We can use the function random.uniform(). Use this to generate a random float between 2.5 and 10.5:





# 4)We can also use the random.choice() function to choose an item inside of a list randomly. Create a list of five foods below and name it as variable food.
#Then use the random.choice(list) function to choose a random item from the list and print it to the console:






# 5) MAD LIBS using Random!! Create 3 lists with at least 5 strings inside each. Then create 3 variables that represent a random choice from each list by using the
#random.choice() function. Next, use print functions to tell a funny story using the random string variables that you generated. An abbreviated example is commented below:

'''
list1 = ['string1','string2','string3','string4','string5']
choice1 = random.choice(list)
print('Here is some text that I will combine with my " + choice1 + " string variable by using plus signs.")
'''










# 6)First, import turtle and set t=turtle.Pen(). Next, create a variable called num that is a random integer between 0 and 2. Then use 3 conditional statements (if, elif, else)
#that have your turtle do something different depending on what value x is. The logic of your program in English would be as follows: if num is equal to 0, my turtle
#will draw something unique, else if num is equal to 1, my turtle will do something different/unique, else my turtle will do something different and unique.
#Recommendation: Change the pen color of the turtle for each condition, and have your turtle draw a different shape for each condition.








#----------------------------Bonus Questions-----------------------------------------#

# 1) Pick a random character from a string and print it to the console:







# 2)Calculate the multiplication of two random float numbers:








# 3)Create a guessing game using random.randint(). Create a random integer variable, and an input variable where the user can guess a number. Then use a while loop
#that checks the user's guess to see if it matches up with the random number generated, and then provides feedback to help the user make a better guess.
#For example, if your guess is greater than the random number, tell the user "too high, try again!" Provide similar feedback if the guess is too low. Then exit the while
#loop once the user guesses correctly, and tell the user they've won. This question requires outside research to figure out how to use a while loop.















