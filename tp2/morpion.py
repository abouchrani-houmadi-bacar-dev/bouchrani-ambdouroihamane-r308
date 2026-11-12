import argparse

from .grille import Grille
from .joueurs import JoueurHumain, JoueurIA, JoueurIAMalin


def jouer_partie(joueur_x, joueur_o):
    grille = Grille()
    joueurs = {"X": joueur_x, "O": joueur_o}
    symbole = "X"

    while True:
        grille.afficher()
        try:
            x, y = joueurs[symbole].prochain_coup(grille.tab, symbole)
        except ValueError:
            print("Saisissez deux nombres entiers séparés par un espace.")
            continue
        if not grille.jouer(x, y, symbole):
            print("Coup invalide. Choisissez une case libre de la grille.")
            continue

        if grille.est_gagnant(symbole):
            grille.afficher()
            print(f"Victoire de {symbole} !")
            return symbole
        if grille.est_plein():
            grille.afficher()
            print("Match nul.")
            return None
        symbole = "O" if symbole == "X" else "X"


def main():
    types_joueurs = {"humain": JoueurHumain, "ia": JoueurIA, "malin": JoueurIAMalin}
    parser = argparse.ArgumentParser(description="Jouer au morpion.")
    parser.add_argument("--x", choices=types_joueurs, default="humain", help="joueur X")
    parser.add_argument("--o", choices=types_joueurs, default="ia", help="joueur O")
    args = parser.parse_args()
    joueur_x = types_joueurs[args.x]()
    joueur_o = types_joueurs[args.o]()
    score = {"X": 0, "O": 0, None: 0}

    try:
        while True:
            resultat = jouer_partie(joueur_x, joueur_o)
            score[resultat] += 1
            print(f"Score — X : {score['X']} | O : {score['O']} | Nuls : {score[None]}")
            if input("Rejouer (o/n) ? ").strip().lower() != "o":
                break
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()
