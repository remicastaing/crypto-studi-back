from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Crypto(Base):

    __tablename__ = 'crypto'

    symbol = Column(String(), primary_key=True)
    nom = Column(String(), nullable=False)
    id = Column(Integer(), nullable=False)

    def __repr__(self):
        return (
            f"<Crypto symbol={self.symbol}, nom={self.nom}, id={self.id}>"
        )
