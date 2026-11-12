from random import choice

from .grille import Grille


def cases_libres(tab):
    return [
        (x, y)
        for x, ligne in enumerate(tab)
        for y, case in enumerate(ligne)
        if case == Grille.VIDE
    ]


class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        x, y = input(f"{symbole} — ligne et colonne (0 à 2, séparées par un espace) : ").split()
        return int(x), int(y)


class JoueurIA:
    def prochain_coup(self, tab, symbole):
        return choice(cases_libres(tab))
