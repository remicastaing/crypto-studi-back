from typing import Optional
from models import db
from models.liste import Liste
from models.tache import Tache
from datetime import date


class ListeDAO():

    def getAll(self):

        return Liste.query.all()

    def get(self, id):
        return Liste.query.get(id)

    def getTaches(self, id):
        return Tache.query.filter_by(liste=id).all()

    def create(self, nom: str):
        liste = Liste(nom=nom)
        liste.date = date.today()
        liste.completion = 0
        db.session.add(liste)
        db.session.commit()
        db.session.refresh(liste)
        return liste

    def delete(self, id):
        liste = Liste.query.get(id)
        db.session.delete(liste)
        db.session.commit()

    def update(self, id: str, nom: Optional[str]):

        liste = Liste.query.get(id)

        liste.nom = nom

        db.session.commit()
        db.session.refresh(liste)
        return liste

    # def update_completion(self, id: str, completion: Optional[int]):

    #     liste = Liste.query.get(id)

    #     liste.nom = nom

    #     db.session.commit()
    #     db.session.refresh(liste)
    #     return liste
