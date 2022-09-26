"""
Examples for for loops in python
"""
import maskpass
import matplotlib

#


# Here is a game, it asks user for a word, then keeps asking the user for the provided word in reverse, it will only
# stop if the user provides the correct reversed word. before you run this part, go to Run-> Edit Configurations ->
# Under Execution, enable Emulate terminal in output console Ask user for input
passwordInput = maskpass.askpass(prompt="Hello user, give me a password:", mask="*")
guess = False
while guess is False:
    passwordGuess = input("Ok, what is the reversed password? I will keep asking until you provide the correct answer: ")
    if (''.join(reversed(passwordGuess))) == passwordInput:
        guess = True
        print("You got it!")





# # print a given string 10 times
#
# # Here we are saying, as long as n is the range of 10 (less than 10)
# for n in range(1000):
#     # print this the value of the counter n, and then the word howdy
#     print ("{0}".format(n),"Howdy")
# print("end of the first for loop.")
#
#
# # define a list of things, such as names of cats
# cats = ["Fluffkinz","Whisper","Quincy","Stinky","Duchess"]
#
# # here we are saying, as long as therre is a variable named cat in the list of cats
# for cat in cats:
#     # print the cat name
#     print(cat)
# print("End of the cats for loop")
#
# # Another great use of for loops is to read data from external sources, such as text file.
# # This prints out all lines, the open functionality stops when it reaches the end of the file.
#
# give the locatoin of the file. The ./ part means this is local to the project
dataFileLocation= "./data.txt"

# # open the file in r mode, meaning reading mode
# with open(dataFileLocation,'r') as text:
#     #printout the line
#     print(text.readlines())
# print("End of the first reading file mechanism ")
# Another "cleaner" method to read line by line

# This open the file and saves its content in a variable named allText
# allText = open(dataFileLocation,'r')
#
# # This iterates through the allText, and then prints out data, one line at a time.
# for line in allText:
#     print(line)


