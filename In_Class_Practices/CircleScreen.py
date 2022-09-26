"""
This program uses the methods defined in the CircleScreen file
"""
# import the  file which has the functions we want to use
import CircleProgram


# define teh main method. Just use this as is.
def main():
    # Your code goes here.
    # define diameter
    theDiameter = 10.9

    # pass the diameter to the method, call the method, and store the returned value in the theArea variable
    theArea = CircleProgram.CircleArea(theDiameter)

    # print out the output
    print("The area of a circle of {0}".format(theDiameter), " is {0}".format(theArea))

    # Call the method which shows the area
    #CircleProgram.ShowCircleArea()
if __name__ == "__main__":
    main()
