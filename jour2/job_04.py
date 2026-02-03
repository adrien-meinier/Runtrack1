class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Numéro étudiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")
        print(f"Le nombre de credits de {self.__prenom} {self.__nom} est de {self.__credits} points")

student = Student("Doe", "John", 145)

student.add_credits(30)
student.add_credits(25)
student.add_credits(20)

student.studentInfo()
