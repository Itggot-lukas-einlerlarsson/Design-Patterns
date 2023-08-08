# page 219 - A Beginners Guide to Python 3 Programming
# repetition

class Person():
    """docstring for Person."""

    instance_count = 0 # static variable, part of the class, not instance
    # Used in instance creation
    # Answering enquiries about the class
    # Examples for documentation of the class
    # Perform classes
    # General support to each instance

    @classmethod
    def instance_incrementer(cls): #takes cls as parameter
        cls.instance_count += 1

    @staticmethod # same as classmethod but doesn't take any parameters
    def printle():
        print("shawarma")

    def __init__(self, name : int, age : int):
        Person.instance_incrementer()
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name + " is " + str(self.age) + " years old"

    def __del__(self):
        delattr(self, "name")
        delattr(self, "age")

    def calc_salary(self, worked_hours : int ) -> int:
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return worked_hours * rate_of_pay

    def is_teenager(self) -> bool:
        return self.age < 26

def main():
    p1 = Person("Lukako", 32)
    p2 = Person("Dexter", 12)
    print("p1 object: ", p1)
    print("p2 object: ", p2)
    px = p1
    print("id of p1", id(p1))
    print("id of p2", id(px)) # a pointer to p1
    print("id of p2", id(p2))
    p1.name = "boble"
    p2.age = 25
    print(p1.name, "is", p1.age, "years old")
    print(p2.name, "is", p2.age, "years old")
    print(p1)
    print(p2)
    print(p1.calc_salary(40))
    print("is", p2.name, "a teenager?", p2.is_teenager())
    del p1
    try:
        print(p1)
    except Exception as e:
        print("Ay karamba!")
    print("Instance count:",Person.instance_count) # del säger att det fortfarande finns två instanser?
    class_attributes(p2)
    p2.printle()

def class_attributes(p2 : Person):
    print('Class attributes')
    print(Person.__name__)
    print(Person.__module__)
    print(Person.__doc__)
    print(Person.__dict__)
    print('Object attributes')
    print(p2.__class__)
    print(p2.__dict__)


if __name__ == '__main__':
    main()
