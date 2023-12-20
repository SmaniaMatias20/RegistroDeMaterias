class Materia:
    def __init__(self, name, qualification, state):
        self.id_materia = None
        self.name = name
        self.qualification = qualification
        self.state = state
    
    def __str__(self):
        return f'Materia[{self.name}, {self.qualification}, {self.state}]'