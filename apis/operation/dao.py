
from models import db
from models.operation import Operation
from datetime import date

arguments = [
               'en_vigeur',
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

class OperationDAO():

    def getAll(self):
        return Operation.query.all()

    def get(self, id):
        return Operation.query.get(id)

    def create(self, data):

        operation = Operation()
        operation.date =date.today()
        for key, value in data.items():
            if key in arguments:
                setattr(operation, key, value)

        db.session.add(operation)
        db.session.commit()
        db.session.refresh(operation)
        return operation

    def delete(self, id):

        Operation.query.get(id).delete()
        db.session.commit()

    def update(self, id, data):

        operation = Operation.query.get(id)

        operation.date_creation = date.today()

        for key, value in data.items():
            if key in arguments:
                setattr(operation, key, value)

        db.session.commit()
        db.session.refresh(operation)
        return operation
