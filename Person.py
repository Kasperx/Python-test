import random
import uuid


class Person:
    #firstname: str
    #surname: str
    name: str
    age: int
    address: str
    id: int
    genre: str

#    def __new__(cls):
#        return super().__new__(cls)

    def __init__(self, id: int, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        #self.id = uuid.uuid4()

    def show(self, persons: [] = None):

        if persons is None:
            print(self.getperson(self))
        else:
            for x in persons:
                print(self.getperson(x))

    def getperson(self, person):
        return ("["
        + "id: " + str(person.id)
        + "name: " + person.name
        + ", \tage: "
        + str(person.age)
        + ", \taddresse: "
        + person.address
        + "]")