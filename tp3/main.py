import argparse
from pathlib import Path

from .bibliotheque import Bibliotheque
from .livre import Livre
from .utilisateur import Utilisateur


MENU = """
1. Ajouter un livre
2. Ajouter un utilisateur
3. Emprunter un livre
4. Rendre un livre
5. Afficher les livres
6. Quitter et sauvegarder
"""


def ajouter_livre(bibliotheque):
    titre = input("Titre : ").strip()
    auteur = input("Auteur : ").strip()
    try:
        annee = int(input("Année : "))
    except ValueError:
        print("Année invalide. Saisissez un nombre entier.")
        return
    if not titre or not auteur:
        print("Le titre et l’auteur sont obligatoires.")
    elif bibliotheque.ajouter_livre(Livre(titre, auteur, annee)):
        print("Livre ajouté.")
    else:
        print("Ce titre existe déjà.")


def ajouter_utilisateur(bibliotheque):
    nom = input("Nom : ").strip()
    if not nom:
        print("Le nom est obligatoire.")
    elif bibliotheque.ajouter_utilisateur(Utilisateur(nom)):
        print("Utilisateur ajouté.")
    else:
        print("Ce nom existe déjà.")


def gerer_emprunt(bibliotheque, choix):
    nom = input("Nom de l’utilisateur : ").strip()
    titre = input("Titre : ").strip()
    if nom not in bibliotheque.utilisateurs:
        print("Utilisateur inconnu.")
    elif titre not in bibliotheque.livres:
        print("Livre inconnu.")
    elif choix == "3":
        if bibliotheque.emprunter(nom, titre):
            print("Emprunt enregistré.")
        else:
            print("Emprunt refusé. Ce livre est déjà emprunté.")
    elif bibliotheque.rendre(nom, titre):
        print("Retour enregistré.")
    else:
        print("Retour refusé. Ce livre n’est pas emprunté par cet utilisateur.")


def menu(bibliotheque, fichier):
    while True:
        print(MENU)
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_livre(bibliotheque)
        elif choix == "2":
            ajouter_utilisateur(bibliotheque)
        elif choix in ("3", "4"):
            gerer_emprunt(bibliotheque, choix)
        elif choix == "5":
            bibliotheque.afficher_livres()
        elif choix == "6":
            try:
                bibliotheque.sauvegarder(fichier)
            except OSError as erreur:
                print(f"Sauvegarde impossible : {erreur}")
                continue
            print("Bibliothèque sauvegardée.")
            return 0
        else:
            print("Choix invalide.")


def main():
    parser = argparse.ArgumentParser(description="Gérer une bibliothèque.")
    parser.add_argument("--fichier", type=Path, default=Path("bibliotheque.csv"))
    args = parser.parse_args()
    bibliotheque = Bibliotheque()
    try:
        bibliotheque.charger(args.fichier)
    except (OSError, ValueError) as erreur:
        print(f"Chargement impossible : {erreur}")
        return 1
    try:
        return menu(bibliotheque, args.fichier)
    except (EOFError, KeyboardInterrupt):
        print("\nSession interrompue. Les changements de cette session n’ont pas été sauvegardés.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
