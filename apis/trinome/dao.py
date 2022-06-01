
from models import db
from models.trinome import Trinome
from datetime import date
from models import db
from sqlalchemy import select, update

arguments = [
    'actuel',
    'date',
    'couts_carbu',
    'couts_pneu',
    'couts_entretien',
    'couts_peage',
    'salaires',
    'cotisations',
    'indemnites',
    'autres_couts',
    'hh_totales',
    'assurances',
    'taxes',
    'couts_structure',
    'nbre_vehicules',
    'nbre_jours_roulage',
    'couts_journaliers_autres',
    'couts_forces_fms',
    'couts_forces_horaires',
    'couts_forces_journaliers']


class TrinomeDAO():

    def getAll(self):
        return Trinome.query.all()

    def get(self, id):
        res = Trinome.query.get(id)
        return res

    def get_actuel(self):
        res = db.session.execute(select(Trinome).
                                 where(Trinome.actuel == True)).fetchone()

        return res[0]

    def create(self, data):

        trinome = Trinome()
        trinome.date = date.today()

        for key, value in data.items():
            if key in arguments:
                setattr(trinome, key, value)

        return self.create_trinome(trinome)

    def delete(self, id):

        Trinome.query.get(id).delete()
        db.session.commit()

    def update(self, id, data):

        trinome = Trinome()
        trinome.date = date.today()

        old_trinome = Trinome.query.get(id)

        for key, value in vars(old_trinome).items():
            if key in arguments:
                setattr(trinome, key, value)

        for key, value in data.items():
            if key in arguments:
                setattr(trinome, key, value)

        trinome.id = None

        return self.create_trinome(trinome)

    def set_actual_to_false(self):
        db.session.execute(update(Trinome).
                           where(Trinome.actuel == True).
                           values(actuel=False))

    def create_trinome(self, trinome):

        if trinome.actuel:
            self.set_actual_to_false()
        db.session.add(trinome)
        db.session.commit()
        db.session.refresh(trinome)
        return trinome
