from core.DAO import DAO


class UtilisateurDAO(DAO):

    def getAll(self):
        return self.fetchAll("SELECT id, prenom, nom, email FROM utilisateurs ORDER BY nom")

    def get(self, id):
        return self.fetchAll("SELECT id, prenom, nom, email FROM utilisateurs where id = %s", (id,))

    def create_utilisateur(self, prenom: str, nom: str, email: str):
        return self.insert("INSERT INTO utilisateurs(prenom, nom, email) VALUES(%s, %s, %s)\
                           RETURNING id, prenom, nom, email ", (prenom, nom, email))
