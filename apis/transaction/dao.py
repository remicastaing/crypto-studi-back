from typing import Optional
from uuid import UUID
from models import db
from datetime import date, datetime
from models.transaction import Transaction
from http import HTTPStatus
from flask_restx import abort


class TransactionDAO():

    def getAll(self):
        return db.session.query(Transaction).all()

    def getAllFor(self, id):
        print("Retourne liste de tâche")
        return db.session.query(Transaction).filter(Transaction.utilisation==id).all()

    def get(self, id):
        return db.session.query(Transaction).get(id)

    def create(self, utilisateur: str, date: datetime, crypto: str, quantite: float, prix: float):
        transaction = Transaction(utilisateur=UUID(utilisateur), crypto=crypto, date = date, quantite=quantite, prix=prix)
        db.session.add(transaction)
        db.session.commit()
        db.session.refresh(transaction)
        return transaction

    def delete(self, id):

        transaction = db.session.query(Transaction).get(id)
        db.session.delete(transaction)
        db.session.commit()

    def update(self, id: str, utilisateur: Optional[str], crypto: Optional[bool], quantite: Optional[float],  prix: Optional[float]):

        transaction = db.session.query(Transaction).get(id)

        if crypto:
            transaction.crypto = crypto
        if quantite:
            transaction.quantite = quantite
        if prix:
            transaction.prix = prix

        db.session.commit()
        db.session.refresh(transaction)
        return transaction
