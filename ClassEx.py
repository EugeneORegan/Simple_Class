# A class called Person
class Person:
    isAdult = False

    # The following is the CONSTRUCTOR of the class.
    # In this case we set the persons age when INSTANTIATING
    # an object of that type
    def __init__(self, age):
        self.age = age

    # A function to determine whether a Person is an adult
    def isAdultOrChild(self):
        if self.age >= 18:
            self.isAdult = True
        else:
            self.isAdult = False
        return self.isAdult


# While the next piece of code is in the same file,
# it is important to note that it is NOT part of the
# person class. Typically they would be in another file,
# but keeping it here for demonstration purposes.

People = []  # A list to store all the Person objects ... Not needed, but a common practice.

# Next three lines create three different Person objects with different ages
a = Person(19)
b = Person(12)
c = Person(18)
# We then add the Person objects to the List
People.append(a)
People.append(b)
People.append(c)
adultCount = 0  # A counter variable for next part

# A for loop that goes through the list and sees how many adults in it.
for p in People:
    print(p.isAdultOrChild(), " Age is ", p.age)

    if p.isAdultOrChild():
        adultCount = adultCount + 1

# Printing how many adults
print("There are ", adultCount, " adults in the list")
