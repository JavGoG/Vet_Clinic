from db.run_sql import run_sql
from models.user import User


def save(user):
    sql = "INSERT INTO users (name, pet_name, phone) VALUES (%s, %s, %s) RETURNING *"
    values = [user.name, user.pet_name, user.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User (row['name'], row['pet_name'], row['phone'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        user = User(result['name'], result['pet_name'], result['id'] )
    return user


def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET (name, phone, pet_name) = (%s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

# def tasks(user):
#     tasks = []

#     sql = "SELECT * FROM tasks WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for row in results:
#         task = Task(row['description'], row['user_id'], row['duration'], row['completed'], row['id'] )
#         tasks.append(task)
#     return tasks
