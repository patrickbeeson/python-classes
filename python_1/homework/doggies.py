#!/usr/local/bin/python3
"""
doggies.py

This program has a class called Dog whose init method takes
two parameters, name and breed. An empty list is bound to the dogs
global variable. A while loop is used to get a user's input for name and
breed, and terminates if a blank line is entered. For each name and breed
entered, an instance of the Dog class with name and breed as arguments is created.
This instance is appended to the dogs list, and printed.
"""

# create our Dog class
class Dog:
    """ A dog with a name and breed as parameters """

    def __init__(self, name, breed):
        """ Each dog has a name and breed """
        self.name = name
        self.breed = breed

    def __str__(self):
        """ Returns the dog's name and breed """
        return "{name}: {breed}".format(name=self.name, breed=self.breed)
        
if __name__ == "__main__":
    # create our empty dogs list
    dogs = []

    # start our loop
    while True:
        # get the dog's name
        ui_dogname = str(input("Enter the dog's name: "))
        
        # If our first input is blank, break the loop
        if not ui_dogname:
            print("Goodbye!")
            break
        
        # get the dog's breed
        ui_dogbreed = str(input("Enter the dog's breed: "))
        
        # create an instance of the dog object and
        # assign the input as arguments
        dog = Dog(name=ui_dogname, breed=ui_dogbreed)
        # append the instance to our list
        dogs.append(dog)
        
        print("DOGS")
        
        # loop through the list and print the name and breed
        for i,dog in enumerate(dogs):
            print("{i}. {name}:{breed}".format(i=i, name=dog.name, breed=dog.breed))
        
        print(40 * "*")
    