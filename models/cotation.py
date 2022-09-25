from sqlalchemy import Column, String, Date, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Cotation(Base):

    __tablename__ = 'cotation'

    crypto = Column(String(), primary_key=True)
    date = Column(Date, primary_key=True)
    prix = Column(Numeric, nullable=False)
    change = Column(Numeric, nullable=True)

    def __repr__(self):
        return (
            f"<Cotation crypto={self.crypto}, date={self.date}, prix={self.prix}, change={self.change}>"
        )
