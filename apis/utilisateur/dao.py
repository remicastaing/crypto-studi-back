from core.DAO import DAO

from models import db
from models.utilisateur import Utilisateur


class UtilisateurDAO(DAO):

    def getAll(self):
        return Utilisateur.query.all()

    def get(self, id):
        return Utilisateur.query.get(id)

    def create_utilisateur(self, prenom: str, nom: str, email: str):

        utilisateur = Utilisateur(prenom = prenom, nom = nom, email = email)
        db.session.add(utilisateur)
        db.session.commit()
        db.session.refresh(utilisateur)
        return utilisateur

