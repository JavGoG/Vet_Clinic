from db.run_sql import run_sql
import pdb

# from models.clinic import Clinic
from models.animal import Animal
from models.user import User
import repositories.user_repository as user_repository


def save(animal):
    sql = "INSERT INTO animals (pet_name, date_of_birth, specie,  treatment, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.pet_name, animal.date_of_birth, animal.specie , animal.treatment, animal.user.id]
    results = run_sql(sql, values)
    # pdb.set_trace()
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        animal = Animal(user, row['pet_name'], row['date_of_birth'], row['specie'], row['treatment'], row['id'])
        animals.append(animal)
    return animals



def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        animal = animal(result['pet_name'], user, result['treatment'], result['specie'], result['id'] )
    return animal


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (pet_name, user_id, treatment, specie, date_of_birth) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.pet_name, animal.user.id, animal.treatment, animal.completed, animal.id]
    run_sql(sql, values)
