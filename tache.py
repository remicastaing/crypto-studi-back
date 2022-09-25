
from datetime import datetime
import json
from config import ProductionConfig, DevelopmentConfig

from models.cotation import Cotation
from models.crypto import Crypto

from core.env import is_on_heroku

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from services.coinmarketcapService import CoinMarketCapService

if not(is_on_heroku()):
    config = DevelopmentConfig
else:
    config = ProductionConfig


engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True, future=True)


CMC = CoinMarketCapService(config.CMC_API_URL, config.CMC_API_KEY)

session = Session(engine)

cryptos = session.query(Crypto).all()

cotations = CMC.getQuotes(cryptos)


session.add_all(cotations)

session.commit()


# cotation = Cotation(crypto = 'BTC', date = datetime.now(), prix = 123.4)


# session.add(cotation)

# session.commit()
