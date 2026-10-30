# Importation du module ramdom  
import random

# Listes des mots disponibles 
mots = ["python", "programmation", "pendu", "développeur"]

MAX_ERREURS = 7

def choisir_mot(liste):
    mot = random.choice(liste)
    return mot.upper()

mot_secret = choisir_mot(mots)
print("Mot choisi :", mot_secret)

