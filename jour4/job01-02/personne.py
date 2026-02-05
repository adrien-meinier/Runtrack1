class Personne:
    def __init__(self, age=14):
        self.age = age  

    def afficherAge(self):
        print(self.age)  

    def bonjour(self):
        print("Hello") 

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age 



