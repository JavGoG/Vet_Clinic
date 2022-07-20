class Booking:
    def __init__(self, user_name, pet_name, date_time, id=None):
        self.date_time = date_time
        self.pet_name = pet_name
        self.user_name = user_name
        self.id = id
    