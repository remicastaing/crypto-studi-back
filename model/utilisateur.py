import uuid


class Utilisateur():

    def __init__(self, id, prenom, nom, email) -> None:
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.email = email
