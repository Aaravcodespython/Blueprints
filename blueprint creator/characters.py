class NPC1():
    def __init__ (self,name,level,role):
        self.name = name
        self.level = level
        self.role = role

    def speak(self):
        print(f"Hi, my name is {self.name} and I am a {self.role}! I am also level {self.level}!")

    def level_up(self):
        self.level += 1

class NPC2():
    def __init__ (self,name,level,role):
            self.name = name
            self.level = level
            self.role = role
    
    def speak(self):
        print(f"Hi, my name is {self.name} and I am a {self.role}! I am also level {self.level}!")

    def level_up(self):
        self.level += 1

class Pet():
     def __init__ (self,name,level,role):
             self.name = name
             self.level = level
             self.role = role
     
     def speak(self):
        print(f"Hi, my name is {self.name} and I am a {self.role}! I am also level {self.level}!")
 
     def level_up(self):
        self.level += 1