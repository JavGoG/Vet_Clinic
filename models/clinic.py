class Clinic:

    def __init__(self, description, user, duration, completed = False,  id = None, ):
        self.description = description
        self.user = user
        self.duration = duration
        self.completed = completed
        self.id = id
    
    def adding_vet_to_animal(self, vet, animal, time):
        self.vet = vet
        self.animal = animal
        self.time = time

