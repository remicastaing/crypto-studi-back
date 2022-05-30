
from models import db
from models.operation import Operation
from datetime import date

arguments = [
               'trinome',
               'commercial',
               'date',
               'avant_kms',
               'avant_peages',
               'avant_tps',
               'aller_kms',
               'aller_peages',
               'aller_tps',
               'retour_kms',
               'retour_peages',
               'retour_tps',
               'apres_kms',
               'apres_peages',
               'apres_tps',
               'chargement_tps',
               'dechargement_tps',
               'chargement_unite',
               'chargement_qtt_totale',
               'chargement_par_tour',
               ]

class OperationDAO():

    def getAll(self):
        return Operation.query.all()

    def get(self, id):
        return Operation.query.get(id)

    def create(self, data):

        operation = Operation()

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


        for key, value in data.items():
            if key in arguments:
                setattr(operation, key, value)

        db.session.commit()
        db.session.refresh(operation)
        return operation
