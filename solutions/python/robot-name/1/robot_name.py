import random
from string import ascii_uppercase, digits

    
class Robot:
    NAMES_USED = []
    
    def generate_name(self):
        name = ''
        for _ in range(2):
            name += random.choice(list(ascii_uppercase))
        for _ in range(3):
            name += random.choice(list(digits))
        if name in Robot.NAMES_USED:
            return self.generate_name()
        else:
            Robot.NAMES_USED.append(name)
        return name
    
    def __init__(self):
        self.name = self.generate_name()
    def reset(self):
        self.name = self.generate_name()
        