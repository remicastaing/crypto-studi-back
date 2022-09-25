
from datetime import date, datetime, timedelta
import decimal
import functools
from sqlalchemy import text
from models import db
from models.crypto import Crypto
from flask_restx import abort


sql_text_cumul = text("""
                select stock.date,  stock.sum as cumul from cotation c, (
                    select date_trunc('day',t1.date) as date, t1.achat, SUM(t2.achat) as sum
                    from (SELECT  0 as achat, * from generate_series(
                        '2022-08-01', CURRENT_DATE,
                        INTERVAL '1 day'
                    ) as date
                    union
                    select  t.prix as achat, t."date"  from "transaction" t ) t1
                    inner join (SELECT  0  as achat, * from generate_series(
                        '2022-08-01',CURRENT_DATE,
                        INTERVAL '1 day'
                    ) as date
                    union
                    select  t.prix as achat, t."date"  from "transaction" t ) t2 on t1.date >= t2.date
                    group by t1.date, t1.achat
                    order by t1.date) as stock
                where stock.date = c.date
                """)


sql_text_cumul_by_crypto = text("""
                                select stock.date,  c.crypto, c.prix as cotation, stock.sum as quantite, stock.sum * c.prix as valuation, stock.investissement as achat, stock.sum * c.prix - stock.investissement as gain
                                from cotation c, (
                                select date_trunc('day',t1.date) as date, t1.quantite, SUM(t2.quantite) as sum, SUM(t2.achat)as investissement
                                from (SELECT :CRYPTO as crypto, 0 as quantite, 0 as prix, 0 as achat, * from generate_series(
                                    '2022-08-01', CURRENT_DATE,
                                    INTERVAL '1 day'
                                ) as date
                                union
                                select t.crypto , t.quantite, t.prix as prx, t.prix as achat, t."date"  from "transaction" t where t.crypto = :CRYPTO) t1
                                inner join (SELECT :CRYPTO as crypto, 0 as quantite, 0 as cotation, 0 as achat, * from generate_series(
                                    '2022-08-01',CURRENT_DATE,
                                    INTERVAL '1 day'
                                ) as date
                                union
                                select t.crypto , t.quantite, t.prix as prix, t.prix as achat, t."date"  from "transaction" t where t.crypto = :CRYPTO) t2 on t1.date >= t2.date
                                where t1.crypto = t2.crypto and t1.crypto = :CRYPTO
                                group by t1.date, t1.quantite
                                order by t1.date) as stock
                                where stock.date = c.date and c.crypto = :CRYPTO
                                """)


def check_date(date):
    return lambda list: list[0].date() == date


class CumulDAO():

    def get(self):

        cryptos = db.session.query(Crypto).all()

        result = []
        for crypto in cryptos:

            with db.engine.connect() as conn:
                exe = conn.execute(sql_text_cumul_by_crypto, CRYPTO=crypto.symbol)

                for row in exe:
                    result.append(row)

        return result

    def getByCrypto(self, crypto):

        with db.engine.connect() as conn:
            result = conn.execute(sql_text_cumul_by_crypto, CRYPTO=crypto)
            res = []
            for row in result:
                res.append(row)
            return res
