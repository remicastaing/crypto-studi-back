from core.db_connexion import get_connexion
import psycopg2
from psycopg2.extras import RealDictCursor, DictCursorBase

class DAO():
    connexion = get_connexion()
    def __init__(self) -> None:
        pass

    def cursor(self) -> DictCursorBase:
        return self.connexion.cursor(cursor_factory=RealDictCursor)

    def fetchAll(self, requete: str, params = None) :

        try: 
            cursor = self.cursor()
            if params:
                cursor.execute(requete, params)
            else:
                cursor.execute(requete)
            row = cursor.fetchall()
            cursor.close()
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def fetchone(self, requete: str, params):
        try: 
            cursor = self.cursor()
            if params:
                cursor.execute(requete, params)
            else:
                cursor.execute(requete)
            row = cursor.fetchone()
            cursor.close()
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert(self, requete: str, valeurs):
        try: 
            cursor = self.cursor()

            cursor.execute(requete, valeurs)


            result = cursor.fetchone()

            self.connexion.commit()

            cursor.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)        