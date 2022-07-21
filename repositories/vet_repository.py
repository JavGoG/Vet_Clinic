from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name, speciality) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.speciality]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet (row['name'], row['speciality'], row['id'])
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        vet = Vet (row['name'], row['speciality'], row['id'])
    return vet


def adding_vet_to_animal(self, vet_name, animal_name):
    self.vet_name = vet_name
    self.animal_name = animal_name
    self.vet_name = vet_name


def delete_all():
    sql = "DELETE FROM vets" 
    run_sql(sql)
