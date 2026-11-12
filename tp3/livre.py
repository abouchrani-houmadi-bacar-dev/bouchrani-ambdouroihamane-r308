class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunteur = None

    @property
    def disponible(self):
        return self.emprunteur is None

    def afficher(self):
        statut = "disponible" if self.disponible else f"emprunté par {self.emprunteur}"
        print(f"{self.titre} — {self.auteur} ({self.annee}) — {statut}")

    def emprunter(self, nom):
        if not self.disponible or not nom:
            return False
        self.emprunteur = nom
        return True

    def rendre(self):
        if self.disponible:
            return False
        self.emprunteur = None
        return True
