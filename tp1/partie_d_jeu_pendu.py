# Importation du module ramdom  
import random

# Listes des mots disponibles 
mots = ["python", "programmation", "pendu", "développeur"]

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

# Affichage du mot choisi et du mot masqué
mot_secret = choisir_mot(mots)
print("Mot choisi :", mot_secret)

# Affichage du mot masqué
mot_masque = masque(mot_secret)
print("Mot masqué :", mot_masque)

# Test de la fonction reveler_lettre
mot_masque = reveler_lettre(mot_secret, mot_masque, "P")
print("Après avoir proposé P :", mot_masque)

# Test de la fonction lettre_deja_proposee
lettres_proposees = ["P", "A", "B"]

print(lettre_deja_proposee("P", lettres_proposees))
print(lettre_deja_proposee("Z", lettres_proposees))