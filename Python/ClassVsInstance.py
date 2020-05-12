class Person:
    def __init__(self, initialAge):
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age >= 18:
            print("You are old.")
        elif self.age >= 13:
            print("You are a teenager.")
        else:  # age < 13
            print("You are young.")

    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

#
#
# for i in range(0, t):
#     age = int(input())
#     p = Person(age)
#     p.amIOld(age)
#     for j in range(0, 3):
#         p.yearPasses(age)
#         # print("range2")
#     p.amIOld(age)
#     # print("range1")


#Age is not valid, setting age to 0. (age < 0)
#You are young. (age >= 13 and age < 18)
#You are a teenager. (age > 18)