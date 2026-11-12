class Grille:
    """Grille de morpion. x désigne la ligne et y la colonne, de 0 à 2."""

    VIDE = " "

    def __init__(self):
        self.tab = [[self.VIDE for _ in range(3)] for _ in range(3)]

    def afficher(self):
        print("\n---------\n".join(" | ".join(ligne) for ligne in self.tab))

    def jouer(self, x, y, joueur):
        if joueur not in ("X", "O") or not (0 <= x < 3 and 0 <= y < 3):
            return False
        if self.tab[x][y] != self.VIDE:
            return False
        self.tab[x][y] = joueur
        return True

    def est_gagnant(self, j):
        if j not in ("X", "O"):
            return False
        lignes = [*self.tab, *zip(*self.tab)]
        lignes.append([self.tab[i][i] for i in range(3)])
        lignes.append([self.tab[i][2 - i] for i in range(3)])
        return any(all(case == j for case in ligne) for ligne in lignes)

    def est_plein(self):
        return all(self.VIDE not in ligne for ligne in self.tab)
