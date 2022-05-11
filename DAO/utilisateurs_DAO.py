from DAO.DAO import DAO


class UtilisateurDAO(DAO):

    def getAll(self):
        return self.fetchAll("SELECT id, prenom, nom, email FROM utilisateurs ORDER BY nom")

    def get(self, id):
        return self.fetchAll("SELECT id, prenom, nom, email FROM utilisateurs where id = %s", (id,))
