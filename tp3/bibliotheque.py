class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        if not livre.titre or livre.titre in self.livres:
            return False
        self.livres[livre.titre] = livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        if not utilisateur.nom or utilisateur.nom in self.utilisateurs:
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    def emprunter(self, nom, titre):
        utilisateur = self.utilisateurs.get(nom)
        livre = self.livres.get(titre)
        if utilisateur is None or livre is None:
            return False
        return utilisateur.emprunter_livre(livre)

    def rendre(self, nom, titre):
        utilisateur = self.utilisateurs.get(nom)
        livre = self.livres.get(titre)
        if utilisateur is None or livre is None:
            return False
        return utilisateur.rendre_livre(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        for livre in self.livres.values():
            livre.afficher()
