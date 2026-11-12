class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        if not livre.emprunter(self.nom):
            return False
        self.emprunts.append(livre)
        return True

    def rendre_livre(self, livre):
        if livre not in self.emprunts or livre.emprunteur != self.nom:
            return False
        livre.rendre()
        self.emprunts.remove(livre)
        return True

    def afficher_emprunts(self):
        if not self.emprunts:
            print(f"{self.nom} n'a aucun emprunt.")
        for livre in self.emprunts:
            livre.afficher()
