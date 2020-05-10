class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        initialAge = 0

    def amIOld(self, age):
        # Do some computations in here and print out the correct statement to the console
        # print("amIold", age)
        if age <= 0:
            print("Age is not valid, setting age to 0.")
            # age = 0
        elif (age > 13 and age <=18):
            print("You are young.")
        else:
            print("You are a teenager.")
    def yearPasses(self, age):
        #Increment the age of the person in here
        self = age + 1
        print("yearPasses")

t = int(input())

for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld(age)
    for j in range(0, 3):
        p.yearPasses(age)
        # print("range2")
    p.amIOld(age)
    # print("range1")


#Age is not valid, setting age to 0. (age < 0)
#You are young. (age >= 13 and age < 18)
#You are a teenager. (age > 18)