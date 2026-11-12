import csv
from pathlib import Path
from tempfile import NamedTemporaryFile

from .livre import Livre
from .utilisateur import Utilisateur


COLONNES_LIVRES = ("titre", "auteur", "année", "disponible", "emprunteur")


def fichier_utilisateurs(fichier):
    return fichier.with_name(f"{fichier.stem}.utilisateurs.csv")


def _ecrire_csv(chemin, colonnes, lignes):
    fichier = NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", dir=chemin.parent, delete=False
    )
    temporaire = Path(fichier.name)
    try:
        with fichier:
            writer = csv.writer(fichier)
            writer.writerow(colonnes)
            writer.writerows(lignes)
        temporaire.replace(chemin)
    finally:
        temporaire.unlink(missing_ok=True)


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

    def sauvegarder(self, fichier):
        chemin = Path(fichier)
        _ecrire_csv(fichier_utilisateurs(chemin), ("nom",), ((nom,) for nom in self.utilisateurs))
        lignes = (
            (livre.titre, livre.auteur, livre.annee, livre.disponible, livre.emprunteur or "")
            for livre in self.livres.values()
        )
        _ecrire_csv(chemin, COLONNES_LIVRES, lignes)

    def charger(self, fichier):
        chemin = Path(fichier)
        chargee = Bibliotheque()

        try:
            source = chemin.open(encoding="utf-8-sig", newline="")
        except FileNotFoundError:
            return False

        try:
            with source:
                lecteurs = fichier_utilisateurs(chemin)
                if lecteurs.is_file():
                    with lecteurs.open(encoding="utf-8-sig", newline="") as noms:
                        reader = csv.reader(noms, strict=True)
                        if next(reader, None) != ["nom"]:
                            raise ValueError(f"En-tête incorrect dans {lecteurs.name}.")
                        for ligne in reader:
                            if len(ligne) != 1 or not chargee.ajouter_utilisateur(Utilisateur(ligne[0])):
                                raise ValueError(f"Utilisateur invalide à la ligne {reader.line_num}.")
                reader = csv.DictReader(source, strict=True)
                if reader.fieldnames != list(COLONNES_LIVRES):
                    raise ValueError(f"En-tête incorrect dans {chemin.name}.")
                for ligne in reader:
                    chargee._charger_livre(ligne, reader.line_num)
        except csv.Error as erreur:
            raise ValueError(f"CSV invalide : {erreur}") from erreur

        self.livres = chargee.livres
        self.utilisateurs = chargee.utilisateurs
        return True

    def _charger_livre(self, ligne, numero):
        try:
            if None in ligne or None in ligne.values():
                raise ValueError("nombre de colonnes incorrect")
            livre = Livre(ligne["titre"], ligne["auteur"], int(ligne["année"]))
            nom = ligne["emprunteur"]
            disponibilite = ligne["disponible"].strip().lower()
            if disponibilite != ("false" if nom else "true"):
                raise ValueError("disponibilité incohérente avec l’emprunteur")
            if not self.ajouter_livre(livre):
                raise ValueError("titre vide ou déjà présent")
            if nom:
                if nom not in self.utilisateurs:
                    self.ajouter_utilisateur(Utilisateur(nom))
                self.emprunter(nom, livre.titre)
        except ValueError as erreur:
            raise ValueError(f"Livre invalide à la ligne {numero} : {erreur}.") from erreur
