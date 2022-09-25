from datetime import datetime
from typing import List
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from core.env import is_on_heroku
from models.crypto import Crypto
from models.cotation import Cotation
import json

class CoinMarketCapService():


    def __init__(self, url, key):
        self.url = url
        self.key = key


    def getQuotes(self, cryptos: List[Crypto]): 

        url = 'https://' + self.url + '/v2/cryptocurrency/quotes/latest'



        parameters = {
            'id': ','.join(map(lambda crypto: str(crypto.id), cryptos)) ,
            'convert': 'EUR'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.key,
        }

        session = Session()
        session.headers.update(headers)

        res=[]
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            
            for crypto in cryptos:
                price = data["data"][str(crypto.id)]['quote']['EUR']['price']
                change = data["data"][str(crypto.id)]['quote']['EUR']['percent_change_24h']
                res.append(Cotation(crypto = crypto.symbol, date = datetime.now(), prix = price, change = change))
            
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        return res
