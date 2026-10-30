# importation du module random 
import random  

mots = ["python", "programmation", "pondu"]

# fonction pour choisir un mot aléatoire dans la liste 

def choisir_mot(liste):
    mot = random.choice(liste)
    return mot.upper()


mot_secret = choisir_mot(mots)
print("Choisis un mot :", mot_secret)
