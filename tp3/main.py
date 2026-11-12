import argparse
from pathlib import Path

from .bibliotheque import Bibliotheque, fichier_utilisateurs
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
        if not bibliotheque.livres[titre].disponible:
            print("Emprunt refusé. Ce livre est déjà emprunté.")
        elif bibliotheque.emprunter(nom, titre):
            print("Emprunt enregistré.")
        else:
            print("Emprunt refusé. La limite d’emprunts est atteinte.")
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
    parser.add_argument("--fichier", type=Path, default=Path("bibliotheque.csv"), help="catalogue CSV")
    parser.add_argument("--limite-emprunts", type=int, help="nombre maximal d’emprunts par utilisateur")
    parser.add_argument("--auteur", help="chercher dans le catalogue sans ouvrir le menu")
    parser.add_argument("--export-json", type=Path, help="exporter le catalogue sans ouvrir le menu")
    args = parser.parse_args()
    if args.limite_emprunts is not None and args.limite_emprunts < 1:
        parser.error("--limite-emprunts doit être un entier positif")
    bibliotheque = Bibliotheque(args.limite_emprunts)
    try:
        bibliotheque.charger(args.fichier)
    except (OSError, ValueError) as erreur:
        print(f"Chargement impossible : {erreur}")
        return 1
    if args.auteur is not None:
        livres = bibliotheque.rechercher_par_auteur(args.auteur)
        if not livres:
            print("Aucun livre trouvé.")
        for livre in livres:
            livre.afficher()
    if args.export_json is not None:
        catalogues = (args.fichier.resolve(), fichier_utilisateurs(args.fichier).resolve())
        if args.export_json.resolve() in catalogues:
            parser.error("choisissez un fichier différent des fichiers CSV pour l’export")
        try:
            bibliotheque.exporter_json(args.export_json)
        except OSError as erreur:
            print(f"Export impossible : {erreur}")
            return 1
        print(f"Catalogue exporté vers {args.export_json}.")
    if args.auteur is not None or args.export_json is not None:
        return 0
    try:
        return menu(bibliotheque, args.fichier)
    except (EOFError, KeyboardInterrupt):
        print("\nSession interrompue. Les changements de cette session n’ont pas été sauvegardés.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
