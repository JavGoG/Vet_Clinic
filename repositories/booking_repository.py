from db.run_sql import run_sql
from models.booking import Booking
from models.user import User

def save(booking):
    sql = "INSERT INTO bookings (user_name, pet_name, date_time) VALUES (%s, %s, %s) RETURNING *"
    values = [booking.user_name, booking.pet_name, booking.date_time]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        booking = Booking (row['user_name'], row['pet_name'], row['date_time'], row['id'])
        bookings.append(booking)
    return bookings
