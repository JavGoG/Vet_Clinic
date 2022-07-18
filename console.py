import pdb
from models.animal import Animal
from models.clinic import Clinic
from models.user import User

import repositories.animal_repository as animal_repository
import repositories.user_repository as user_repository
import datetime
# animal_repository.delete_all()
# user_repository.delete_all()




user1 = User("Jack Jarvis", "Badger", "078964325")
user2 = User("Jean Davis", "Lola", "078954377")
user3 = User("Thomas", "Tiger", "078954338")
user4 = User("Robert", "Pluto", "078954374")
user5 = User("David", "Daisy", "078954322")
user6 = User("Christine", "Marcus", "078954311")

user_repository.select_all()

user_repository.save(user1)
user_repository.save(user2)
user_repository.save(user3)
user_repository.save(user4)
user_repository.save(user5)
user_repository.save(user6)


badger_dob = datetime.date(2017, 3, 3)
lola_dob = datetime.date(2017, 1, 9)
tiger_dob = datetime.date(2017, 3, 23)
pluto_dob = datetime.date(2014, 3, 30)
daisy_dob = datetime.date(2018, 5, 3)
marcus_dob = datetime.date(2021, 6, 3)

badger = Animal("Badger", badger_dob, "dog", user1, "Stomach")
lola = Animal("Lola", lola_dob, "dog", user2, "Skin")
tiger = Animal("Tiger", tiger_dob, "cat", user3, "checkin")
pluto = Animal("Pluto", pluto_dob, "bird", user4, "checkin")
daisy = Animal("Daisy", daisy_dob, "hamster", user5, "checkin")
marcus = Animal("Marcus", marcus_dob, "dog", user6, "checkin")

animal_repository.select_all()

animal_repository.save(badger)
animal_repository.save(lola)
animal_repository.save(tiger)
animal_repository.save(pluto)
animal_repository.save(daisy)
animal_repository.save(marcus)

# clinic_1 = Clinic("Plant seeds", user1, 30)
# clinic_repository.save(clinic_1)

# clinic_2 = Clinic("Go for a run", user1, 30, True)
# clinic_repository.save(clinic_2)


pdb.set_trace()