
import Controller
import Person
#import Database_sqlite
import Database_mariadb

print("###\n")
controller: Controller = Controller.Controller
person: Person = controller.createPerson()
person.show()
print("###\n")
persons: [Person] = controller.createPerson(5)
person.show(persons)
print("###\n")
db: Database_mariadb = Database_mariadb
db.create_database_and_table()
#db.insert_data(persons)
