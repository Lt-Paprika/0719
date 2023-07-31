class Person:
    def __init__(self, personid, firstName, lastName, favoriteColour, age, isWorking):
        self.id = personid
        self.firstName = firstName
        self.lastName = lastName
        self.favoriteColour = favoriteColour
        self.age = age
        self.employed = isWorking
    def print_me(self):
        print(f"My name is {self.firstName}, {self.lastName}")
        print(f"My Id is {self.id}")
        print(f"My favorite colour is {self.favoriteColour}")
        print(f"I am {self.age} years old. In 10 years i will be {self.age}")
        print(f"I am currently {self.employed}")
        print(f"My age in 10 years will be {self.age + 10}")
    def change_colour (self):
        new_colour = input ("What is your new favorite colour?")
        self.favoriteColour = new_colour
        print (f"Your new favourite colour is {self.favoriteColour}")
        
Justin = Person(599612, "Justin", "Penner", "Purple", 32, "not working")
Justin.print_me()

Change_Colour = input("Would you like to change your favorite colour? (yes/no)")
if Change_Colour == 'yes':
    Justin.change_colour()
else:
    print("Thank you.")

#rebuilt the entire repository after hard resetting it all and deleting to get rid of my repositories within repositories hahaha
