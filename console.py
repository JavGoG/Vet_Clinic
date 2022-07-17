import pdb
from models.animal import Animal
from models.clinic import Clinic
from models.user import User

import repositories.clinic_repository as clinic_repository
import repositories.user_repository as user_repository
import datetime
# clinic_repository.delete_all()
# user_repository.delete_all()


badger_dob = datetime.date(2017, 3, 3)
lola_dob = datetime.date(2017, 1, 9)
tiger_dob = datetime.date(2017, 3, 23)
pluto_dob = datetime.date(2014, 3, 30)
daisy_dob = datetime.date(2018, 5, 3)
marcus_dob = datetime.date(2021, 6, 3)

badger = Animal("Badger", badger_dob, "dog", "Jack Jarvis", "Stomach")
lola = Animal("Lola", lola_dob, "dog", "Jack Jarvis", "Skin")
tiger = Animal("Tiger", tiger_dob, "cat", "Jack Jarvis", "checkin")
pluto = Animal("Pluto", pluto_dob, "bird", "Jack Jarvis", "checkin")
daisy = Animal("Daisy", daisy_dob, "hamster", "Jack Jarvis", "checkin")
marcus = Animal("Marcus", marcus_dob, "dog", "Jack Jarvis", "checkin")

user1 = User("Jack Jarvis", "Badger", "078964325")
user2 = User("Jean Davis", "Lola", "078954377")
user3 = User("Thomas", "Tiger", "078954338")
user4 = User("Robert", "Pluto", "078954374")
user5 = User("David", "Daisy", "078954322")
user6 = User("Christine", "Marcus", "078954311")

user_repository.save(user1)
user_repository.save(user2)
user_repository.save(user3)
user_repository.save(user4)
user_repository.save(user5)
user_repository.save(user6)

user_repository.select_all()

# clinic_1 = Clinic("Plant seeds", user1, 30)
# clinic_repository.save(clinic_1)

# clinic_2 = Clinic("Go for a run", user1, 30, True)
# clinic_repository.save(clinic_2)


pdb.set_trace()