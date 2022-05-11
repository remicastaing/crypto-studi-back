from flask_restx import Namespace, Resource, fields
import psycopg2
from psycopg2.extras import RealDictCursor
from core.db_connexion import get_connexion


api = Namespace('utilisateurs', description='opérations relatives aux utilisateurs')

conn = get_connexion()


@api.route('/')
class Utilisateurs(Resource):

    def get(self):
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("SELECT id, prenom, nom, email FROM utilisateurs ORDER BY nom")
            print("Nombre d'utilisateurs: ", cur.rowcount)
            row = cur.fetchall()
            cur.close()
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
