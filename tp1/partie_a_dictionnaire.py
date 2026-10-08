#definition d'un dictionnaire pour stocker les notes des étudiant

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

def charger_etudiants(nom_fichier):
    etudiants = {}
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                nom, note = ligne.strip().split(":")
                etudiants[nom] = float(note)

        print("Données chargées depuis le fichier", nom_fichier)
        return etudiants

    except FileNotFoundError:
        print("Le fichier n'existe pas. Aucun étudiant chargé.")
        return etudiants

    except OSError as erreur:
        print("Erreur lors du chargement des données :", erreur)
        return etudiants
        


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


#sauvegarder etudiants dans le fichier "etudiants.txt")
sauvegarder_etudiants(etudiants, "etudiants.txt")

etudiants_charges = charger_etudiants("etudiants.txt")
print("Étudiants chargés:", etudiants_charges)
