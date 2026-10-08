import os


#definition d'un dictionnaire pour stocker les notes des étudiants

#Fonction pour ajouter un étudiant et sa note dans le dictionnaire
def ajouter_etudiant(d, nom, note):
    d[nom] = note

#fonction pour calculer la moyenne de la classe et l'étudiant avec la meilleure note
def moyenne_classe(d):
    if len(d) ==0:
        return None

    nom = max(d, key=d.get)
    return nom, d[nom]

#Fonction pour sauvegarder les données dans un fichier avec gestion d'erreur
def sauvegarder_etudiants(d, nom_fichier):
    try:
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            for nom, note in d.items():
                fichier.write(f"{nom}:{note}\n")

        print("Données sauvegardées dans le fichier", nom_fichier)

    except OSError as erreur:
        print("Erreur lors de la sauvegarde des données :", erreur)
        


# listes des étudiants et leurs notes
etudiants = {
    "Alice": 12.0,
    "Bob": 15.0,
    "Claire": 9.5
}

ajouter_etudiant(etudiants, "David", 14.0)

####affichier le dictionnaire des étudiants et la moyenne de la classe

#afficher la listes des étudiants et leurs notes
print(etudiants)

#afficher la moyenne de la classe et l'étudiant avec la meilleure note
print("Moyenne de la classe:", moyenne_classe(etudiants))

#afficher l'étudiant avec la meilleure note
print("L'étudiant avec la meilleure note est:", moyenne_classe(etudiants)[0], "avec une note de", moyenne_classe(etudiants)[1])
