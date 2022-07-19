from typing import Optional
from uuid import UUID
from models import db
from datetime import date, datetime
from models.tache import Tache
from http import HTTPStatus
from flask_restx import abort


class TacheDAO():

    def getAll(self):
        return Tache.query.all()

    def getAllFor(self, id):
        print("Retourne liste de tâche")
        return Tache.query.filter(Tache.attribution==id).all()

    def get(self, id):
        return Tache.query.get(id)

    def create(self, liste: str, nom: str, statut: bool, attribution: str):
        tache = Tache(liste=UUID(liste), nom=nom, statut=statut, attribution=attribution)
        tache.date = datetime.now()
        db.session.add(tache)
        db.session.commit()
        db.session.refresh(tache)
        return tache

    def delete(self, id):

        tache = Tache.query.get(id)
        db.session.delete(tache)
        db.session.commit()

    def update(self, id: str, nom: Optional[str], statut: Optional[bool], attribution: Optional[str]):

        tache = Tache.query.get(id)
        print(statut)
        if nom:
            tache.nom = nom
        if statut is not None:
            tache.statut = statut
        if attribution:
            tache.attribution = attribution

        db.session.commit()
        db.session.refresh(tache)
        return tache
