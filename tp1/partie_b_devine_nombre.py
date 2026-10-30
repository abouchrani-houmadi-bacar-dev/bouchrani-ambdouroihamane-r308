
# Importation du module random pour générer un nombre aléatoire
import random

# Génération d'un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

print("J'ai choisi un nombre entre 1 et 100.")
print("Tu dois le trouver en 10 essais maximum.")

# Boucle pour demander un nombre à l'utilisateur
for essai in range(1, 11):
    try:
        proposition = int(input(f"Essai {essai}/10 - Propose un nombre : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if proposition < nombre_secret:
        print("C'est plus grand.")
    elif proposition > nombre_secret:
        print("C'est plus petit.")
    else:
        print(f"Bravo ! Tu as trouvé le nombre secret {nombre_secret} en {essai} essais.")
        break
else:
    print(f"Désolé, tu n'as pas trouvé le nombre secret {nombre_secret}.")
