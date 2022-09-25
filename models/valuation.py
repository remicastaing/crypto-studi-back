from sqlalchemy import Column, Date, Numeric
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Valuation(Base):

    __tablename__ = 'valuation'

    utilisateur = Column(UUID(as_uuid=True))
    date = Column(Date, nullable=False)
    montant = Column(Numeric, nullable=False)

    def __repr__(self):
        return (
            f"<Valuation utilisteur={self.utilisateur}, date={self.date}>, montant={self.montant}"
        )
