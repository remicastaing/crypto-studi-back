from decimal import Decimal
from typing import Dict
from unicodedata import decimal
from unittest import result
from sqlalchemy import text
from models import db
from models.crypto import Crypto
from models.transaction import Transaction
from flask_restx import abort

from services.coinmarketcapService import CoinMarketCapService
from flask import current_app


sql_text = text("""
                select t.crypto, c.nom ,  sum(t.quantite) as quantite  
                from "transaction" t, crypto c 
                where t.crypto = c.symbol 
                group by t.crypto, c.nom  
                """)



class ValuationDAO():

    def get(self):

        stocks = []

        with db.engine.connect() as conn:
            result = conn.execute(sql_text)
            for row in result:
                stocks.append({'crypto': row.crypto, 'nom': row.nom, 'quantite': row.quantite})

        print(stocks)
        CMC = CoinMarketCapService(current_app.config['CMC_API_URL'], current_app.config['CMC_API_KEY'])

        cryptos = db.session.query(Crypto).all()
        cots = CMC.getQuotes(cryptos)

        cotations = {}
        change = {}
        for cot in cots:
            cotations[cot.crypto] =  cot.prix
            change[cot.crypto] =  cot.change 

        for stock in stocks:
            stock['valuation'] = stock['quantite'] * Decimal(cotations[stock['crypto']])
            stock['change'] =  Decimal(change[stock['crypto']])


        return stocks

