from db.run_sql import run_sql
import pdb

# from models.clinic import Clinic
from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository


def save(animal):
    sql = "INSERT INTO animals (pet_name, date_of_birth, specie, treatment, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.pet_name, animal.date_of_birth, animal.specie , animal.treatment, animal.vet.id]
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
        vet = vet_repository.select(row['vet_id'])
        animal = Animal( row['pet_name'], row['date_of_birth'], row['specie'], vet, row['treatment'], row['id'])
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
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['pet_name'], result['date_of_birth'], result['specie'],vet,result['treatment'], result['id'] )
    return animal


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (pet_name, vet_id, treatment, specie, date_of_birth) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.pet_name, animal.vet.id, animal.treatment, animal.completed, animal.id]
    run_sql(sql, values)

