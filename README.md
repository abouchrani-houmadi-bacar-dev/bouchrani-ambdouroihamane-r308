# R3.08 · Travaux pratiques Python

Python 3.10 ou une version plus récente est nécessaire. Toutes les commandes se lancent à la racine du dépôt. Aucun paquet externe n’est requis.

## TP1 · Premiers exercices

```bash
python3 tp1/partie_a_dictionnaire.py
python3 tp1/partie_b_devine_nombre.py
python3 tp1/partie_c_manipulation_mots.py
python3 tp1/partie_d_jeu_pendu.py
```

## TP2 · Morpion

```bash
python3 -m tp2.morpion
```

X joue en premier. Pour choisir une case, saisissez la ligne et la colonne séparées par un espace. Les indices vont de 0 à 2. Par exemple, `1 1` désigne le centre de la grille. Le score est conservé tant que vous rejouez dans la même session.

```bash
python3 -m tp2.morpion --o humain          # Deux joueurs humains
python3 -m tp2.morpion --o malin           # IA qui gagne ou bloque si possible
python3 -m tp2.morpion --x ia --o malin    # Deux IA
```

## TP3 · Bibliothèque

```bash
python3 -m tp3.main
```

Le menu permet d’ajouter des livres et des utilisateurs, de gérer les emprunts et les retours, et de consulter le catalogue et les statistiques. Chaque titre et chaque nom d’utilisateur sont uniques. L’option 6 sauvegarde le catalogue dans `bibliotheque.csv` et les utilisateurs dans `bibliotheque.utilisateurs.csv`. Les deux fichiers sont relus au démarrage suivant. Utilisez `--fichier` pour choisir un autre catalogue.

```bash
python3 -m tp3.main --limite-emprunts 2
python3 -m tp3.main --auteur Orwell
python3 -m tp3.main --export-json catalogue.json
```
