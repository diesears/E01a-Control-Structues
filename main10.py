#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #making the greetings text appear
colors = ['red','orange','yellow','green','blue','violet','purple'] #outlines the possible responses
play_again = '' #enabling the play again feature for more responses 
best_count = sys.maxsize     #no limit on how many times to play       # the biggest number
while (play_again != 'n' and play_again != 'no'): #establishing possible negative answers to playing again 
    match_color = random.choice(colors) #allows the computer to insert a random answer from the given choices 
    count = 0 #establishes where the computer should start counting the attempts
    color = '' #sets the area for a response 
    while (color != match_color): #establishes the condtion that the response must match the correct answer 
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #this allows answers in upper and lower case and with spaces before or after 
        count += 1 #establishes that after this attempt the total attempts will be 1
        if (color == match_color): #the condition for which to print correct 
            print('Correct!') # what will be printed with a correst response 
        else: #establishing the other possible answers 
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #what will be printed for an incorrect response an a counter to count how many total responses 
    print('\nYou guessed it in {0} tries!'.format(count)) #printing to inform the reader how many tries it took them to guess correctly 
    if (count < best_count): #establishing a specific condition for the computer to react to, when its the readers best guess
        print('This was your best guess so far!') # displaying the fact that this was their closest guess
        best_count = count #changing this new best score to reflect the overall best score 
    play_again = input("\nWould you like to play again? ").lower().strip() #displaying the question if the reader wants to play again with a chance for input
print('Thanks for playing!') #shows the final line that thanks the reader for playing 