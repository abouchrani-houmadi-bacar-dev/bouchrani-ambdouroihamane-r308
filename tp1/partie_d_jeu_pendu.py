# Importation du module ramdom  
import random

# Listes des mots disponibles 
mots = ["python", "programmation", "pendu", "développeur"]

MAX_ERREURS = 7

def choisir_mot(liste):
    mot = random.choice(liste)
    return mot.upper()

def masque(mot):
    return ["_" for lettre in mot]


mot_secret = choisir_mot(mots)
print("Mot choisi :", mot_secret)

mot_masque = masque(mot_secret)
print("Mot masqué :", mot_masque)
