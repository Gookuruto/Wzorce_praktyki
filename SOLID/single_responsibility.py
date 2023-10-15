"""
Single Responsibility Principle
“…You had one job” — Loki to Skurge in Thor: Ragnarok
A class should have only one job.
If a class has more than one responsibility, it becomes coupled.
A change to one responsibility results to modification of the other responsibility.
"""

# class Animal:
#     def __init__(self, name: str):
#         self.name = name
#
#     def get_name(self) -> str:
#         pass
#
#     def save(self, animal: Animal):
#         pass
#

"""
The Animal class violates the SRP.
How does it violate SRP?
SRP states that classes should have one responsibility, here, we can draw out two responsibilities: animal database management and animal properties management. 
The constructor and get_name manage the Animal properties while the save manages the Animal storage on a database.
How will this design cause issues in the future?
If the application changes in a way that it affects database management functions. The classes that make use of Animal properties will have to be touched and recompiled to compensate for the new changes.
You see this system smells of rigidity, it’s like a domino effect, touch one card it affects all other cards in line.
To make this conform to SRP, we create another class that will handle the sole responsibility of storing an animal to a database:
"""


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        pass

    def get_age(self):
        return self.age

    def __repr__(self):
        return f"Animal: name: {self.name} age: {self.age}"


class AnimalDB:
    def __init__(self):
        self.database_path = "animals.csv"

    def get_animal(self, number: int) -> Animal:
        with open(self.database_path, "r") as db:
            line = db.read().split()[number]
            return Animal(line.split(",")[0], line.split(",")[1])

    def save(self, animal: Animal):
        with open(self.database_path, "a") as db:
            db.write(f"\n{animal.name},{animal.age}")


"""
When designing our classes, we should aim to put related features together, 
so whenever they tend to change they change for the same reason. 
And we should try to separate features if they will change for different reasons. - Steve Fenton"""

db = AnimalDB()

pies = db.get_animal(1)

print(pies)
print(pies.name)

db.save(Animal("Elephant", 50))
