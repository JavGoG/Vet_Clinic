from db.run_sql import run_sql

from models.clinic import Clinic
from models.animal import Animal
import repositories.user_repository as user_repository


def save(task):
    sql = "INSERT INTO tasks (pet_type, user_id, treatment, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.pet_type, task.user.id, task.treatment, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task


def select_all():
    tasks = []

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        task = Clinic(row['pet_type'], user, row['treatment'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks



# def select(id):
#     task = None
#     sql = "SELECT * FROM tasks WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
#     # Could alternativly have..
#     # if len(results) > 0 
#     if results:
#         result = results[0]
#         user = user_repository.select(result['user_id'])
#         task = Task(result['pet_type'], user, result['treatment'], result['completed'], result['id'] )
#     return task


# def delete_all():
#     sql = "DELETE  FROM tasks"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM tasks WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(task):
#     sql = "UPDATE tasks SET (pet_type, user_id, treatment, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.pet_type, task.user.id, task.treatment, task.completed, task.id]
#     run_sql(sql, values)
