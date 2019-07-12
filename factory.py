class Person(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self,name):
        print("hello I'm man " + name)


class FeMale(Person):
    def __init__(self,name):
        print("hello I'm woman " + name)

class Factory(object):
    def makePerson(self,name,gender):
        if gender == "M":
            return Male(name)
        elif gender=="F":
            return FeMale(name)

if __name__ == '__main__':
    factory = Factory()
    person1 = factory.makePerson("liming","M")
    Person2 = factory.makePerson("xiaohong","F")

