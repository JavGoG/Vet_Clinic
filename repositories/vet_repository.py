from db.run_sql import run_sql
from models.user import User
from models.clinic import Clinic

def adding_vet_to_animal(self, vet_name, animal_name, user_name):
    self.vet_name = vet_name
    self.animal_name = animal_name
    self.user_name = user_name
