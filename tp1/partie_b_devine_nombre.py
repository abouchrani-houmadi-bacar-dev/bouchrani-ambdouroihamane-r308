#importation du module random pour générer un nombre aléatoire
import random 
#génération d'un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

print("J'ai choisi un nombre entre 1 et 10.")
print("Tu dois le trouver en 10 essais maxium")

#boucle pour demander à l'utilisateur de proposer un nombre jusqu'à ce qu'il trouve le nombre secret ou qu'il ait fait 10 essais
for essai in range(1, 11): 
    try:
        proposition = int(input(f"Essai {essai}/10 - Propose un nombre: "))
        continue
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    if proposition < nombre_secret:        
        print("C'est plus petit.")
    elif proposition > nombre_secret:
        print("C'est plus grand.")
    else:
        print(f"Bravo! Tu as trouvé le nombre secret {nombre_secret} en {essai} essais.")
        break
else:
    print(f"Désolé, tu n'as pas trouvé le nombre secret {nombre_secret}.")
