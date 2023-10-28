
import Controller
import Person
import Database

print("###\n")
controller: Controller = Controller.Controller
person: Person = controller.createPerson()
person.show()
print("###\n")
persons: [Person] = controller.createPerson(5)
person.show(persons)
print("###\n")
db: Database = Database
db.create_connection(None)
db.create_database()
db.insert_data(persons)
