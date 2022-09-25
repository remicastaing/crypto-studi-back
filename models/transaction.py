from sqlite3 import Timestamp
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, String, DateTime, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaction(Base):

    __tablename__ = 'transaction'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    utilisateur = Column(UUID(as_uuid=True))
    crypto = Column(String(), nullable=False)
    quantite = Column(Numeric, nullable=False)
    date = Column(DateTime, nullable=False)
    prix = Column(Numeric, nullable=False)

    def __repr__(self):
        return (
            f"<Transaction id={self.id}, utilisateur={self.utilisateur}, crypto={self.crypto}, quantite={self.quantite}, date={self.date}>, prix={self.prix}"
        )
