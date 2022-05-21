from typing import Optional
from models import db
from models.utilisateur import Utilisateur
from http import HTTPStatus
from flask_restx import abort


class UtilisateurDAO():

    def getAll(self):
        return Utilisateur.query.all()

    def get(self, id):
        return Utilisateur.query.get(id)

    def create(self, prenom: str, nom: str, email: str):
        # if Utilisateur.query.filter(Utilisateur.email == email):
        #     abort(HTTPStatus.CONFLICT, f"{email} est déjà enregistré", status="fail")
        utilisateur = Utilisateur(prenom=prenom, nom=nom, email=email)
        db.session.add(utilisateur)
        db.session.commit()
        db.session.refresh(utilisateur)
        return utilisateur

    def delete(self, id):

        Utilisateur.query.get(id).delete()
        db.session.commit()

    def update(self, id: str, prenom: Optional[str], nom: Optional[str], email: Optional[str]):

        utilisateur = Utilisateur.query.get(id)
        if prenom:
            utilisateur.prenom = prenom
        if nom:
            utilisateur.nom = nom
        if email:
            utilisateur.email = email

        db.session.commit()
        db.session.refresh(utilisateur)
        return utilisateur
