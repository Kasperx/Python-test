
import Person
import random
from faker import Faker

class Controller:

    def __new__(cls):
        return super().__new__(cls)

    def createPerson(count: int = None):

        if count is None:
            faker = Faker('de_DE')
            name: str = faker.name()
            age: int = random.randint(0, 80)
            address: str = faker.address()
            person: Person = Person.Person(
                random.randint(50,100),
                name,
                age,
                address
            )
            return person
        else:
            cnt: int = 0
            persons: [] = []
            while(cnt < count):

                faker = Faker('de_DE')
                id: int = cnt
                name: str = faker.name()
                age: int = random.randint(0, 80)
                address: str = faker.address()
                person: Person = Person.Person(
                    id,
                    name,
                    age,
                    address
                )
                persons.append(person)
                cnt += 1
            return persons
