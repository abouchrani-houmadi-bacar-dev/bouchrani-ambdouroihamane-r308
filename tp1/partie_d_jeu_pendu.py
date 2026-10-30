# Importation du module ramdom  
import random

# Listes des mots disponibles 
mots = ["PYTHON", "PROGRAMMATION", "PENDU", "DÉVELOPPEUR"]

MAX_ERREURS = 7

# Fonction pour choisir un mot aléatoire dans la liste
def choisir_mot(liste):
    mot = random.choice(liste)
    return mot.upper()

# Fonction pour créer un masque du mot choisi
def masque(mot):
    return ["_" for lettre in mot]

# Fonction pour révéler les lettres correctes dans le mot masqué"
def reveler_lettre(mot, masque_mot, lettre):
    for i in range(len(mot)):
        if mot[i] == lettre.upper():
            masque_mot[i] = lettre.upper()
    return masque_mot

# Fonction pour vérifier si une lettre a déjà été proposée
def lettre_deja_proposee(lettre, lettres_proposees):
    return lettre.upper() in lettres_proposees

# Fonction pour traiter la lettre proposée par l'utilisateur
def traiter_lettre(mot, masque_mot, lettre, lettres_proposees, erreurs):
    lettre = lettre.upper()

    if lettre_deja_proposee(lettre, lettres_proposees):
        print("Tu as déjà proposé cette lettre.")
        return masque_mot, erreurs

    lettres_proposees.append(lettre)

    if lettre in mot:
        masque_mot = reveler_lettre(mot, masque_mot, lettre)
        print("Bonne lettre !")
    else:
        erreurs += 1
        print("Mauvaise lettre !")

    return masque_mot, erreurs
# Fonction pour vérifier si le joueur a gagné
def partie_gagnee(masque_mot):
    return "_" not in masque_mot

# Fonction pour vérifier si le joueur a perdu
def partie_perdue(erreurs):
    return erreurs >= MAX_ERREURS



# Lancement du jeu
mot_secret = choisir_mot(mots)
mot_masque = masque(mot_secret)
lettres_proposees = []
erreurs = 0

print("Bienvenue dans le jeu du Pendu !")
print("Mot à deviner :", " ".join(mot_masque))
print("Tu as droit à 7 erreurs maximum.")

# Boucle principale du jeu
while not partie_gagnee(mot_masque) and not partie_perdue(erreurs):

    print("\nMot à deviner :", " ".join(mot_masque))
    print("Erreurs :", erreurs, "/", MAX_ERREURS)
    print("Lettres déjà proposées :", lettres_proposees)

    lettre = input("Propose une lettre : ").strip().upper()

    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        continue

    mot_masque, erreurs = traiter_lettre(
        mot_secret, mot_masque, lettre, lettres_proposees, erreurs

    )

# Résultat final de la partie
if partie_gagnee(mot_masque):
    print("\nBravo ! Tu as gagné !")
    print("Le mot était :", mot_secret)
else:
    print("\nPerdu ! Tu as atteint les 7 erreurs.")
    print("Le mot secret était :", mot_secret)