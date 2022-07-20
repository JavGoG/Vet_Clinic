import pdb
from models.animal import Animal
from models.booking import Booking
from models.user import User
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.user_repository as user_repository
import repositories.vet_repository as vet_repository
import repositories.booking_repository as booking_repository

import datetime


animal_repository.delete_all()
user_repository.delete_all()
vet_repository.delete_all()


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

vet1 = Vet("Mark", "traumatologue")
vet2 = Vet("Mary", "anaesthesist")
vet3 = Vet("Michael", "traumatologue")
vet4 = Vet("John", "practicioner")
vet5 = Vet("Rachel", "traumatologue")
vet6 = Vet("Tim", "practicionist")

vet_repository.save(vet1)
vet_repository.save(vet2)
vet_repository.save(vet3)
vet_repository.save(vet4)
vet_repository.save(vet5)
vet_repository.save(vet6)

vet_repository.select_all()

badger_dob = datetime.date(2017, 3, 3)
lola_dob = datetime.date(2017, 1, 9)
tiger_dob = datetime.date(2017, 3, 23)
pluto_dob = datetime.date(2014, 3, 30)
daisy_dob = datetime.date(2018, 5, 3)
marcus_dob = datetime.date(2021, 6, 3)

badger = Animal("Badger", badger_dob, "dog", vet1, "Stomach")
lola = Animal("Lola", lola_dob, "dog", vet2, "Skin")
tiger = Animal("Tiger", tiger_dob, "cat", vet3, "checkin")
pluto = Animal("Pluto", pluto_dob, "bird", vet4, "checkin")
daisy = Animal("Daisy", daisy_dob, "hamster", vet5, "checkin")
marcus = Animal("Marcus", marcus_dob, "dog", vet6, "checkin")


animal_repository.select_all()

animal_repository.save(badger)
animal_repository.save(lola)
animal_repository.save(tiger)
animal_repository.save(pluto)
animal_repository.save(daisy)
animal_repository.save(marcus)

appointment1 = datetime.datetime(2021, 7, 25, 9, 0, 0, 0,)
appointment2 = datetime.datetime(2021, 7, 26, 9, 0, 0, 0,)
appointment3 = datetime.datetime(2021, 7, 27, 9, 0, 0, 0,)
appointment4 = datetime.datetime(2021, 7, 25, 10, 0, 0, 0,)
appointment5 = datetime.datetime(2021, 7, 26, 11, 0, 0, 0,)
appointment6 = datetime.datetime(2021, 7, 27, 12, 0, 0, 0,)

booking1 = Booking("Ed", "Pluto", appointment1 )
booking2 = Booking("John", "Tarzan", appointment2 )
booking3 = Booking("Hommer", "Chita", appointment3 )
booking4 = Booking("Lisa", "Chico", appointment4 )
booking5 = Booking("Bart", "Rambo", appointment5 )
booking6 = Booking("Flanders", "Jil", appointment6 )

booking_repository.select_all()

booking_repository.save(booking1)
booking_repository.save(booking2)
booking_repository.save(booking3)
booking_repository.save(booking4)
booking_repository.save(booking5)
booking_repository.save(booking6)

pdb.set_trace()