import copy

# J'ai importé copy à l'avance
# Début du programme. C'est à partir d'ici qu'on écrira le code

# On commence par préparer les différents models de données à manipuler
# On crée les models de produits et clients
productsModel = {
    "id": 0,
    "name": "",
    "quantity": 0,
    "price": 0
}

clientsModel = {
    "id": 0,
    "name": "",
    "totalExpenses": 0.0,
    "fidelityPoints": 0
}

# puis on crée la liste catalogue et une liste vierge de clients
productCatalog = []
clientsList = []


# Vous pouvez écrire vos fonctions à partir d'ici Merci d'écrire de façon propre et de commenter vos codes Une ligne
# d'espace entre les blocs de code et deux entre les grands blocs de code Une ligne d'espace avant les commentaires
# et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associé

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Toutes les fonctions ici >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Fonction à appeler chaque fois qu'il faudra poser une interrogation à 2 choix à l'utilisateur
def userTotalInterrogation(proposition, falseChoice, invalidInputStatement):
    # Cette fonction va renvoyer "True" si l'utilisateur tape juste la touche "Entrer" lorsqu'on lui demande son choix
    # s'il saisit la proposition de choix fausse reçue en paramètre, elle retournera "False" et pour tout autre entrée
    # elle retournera le message d'erreur lui aussi reçus en paramètre
    while True:
        choice = input("{} -> ".format(proposition))
        if not choice:
            return True
            break
        elif choice == falseChoice:
            return False
            break
        else:
            print(invalidInputStatement)


# cette fonction renvoie le choix du rôle de l'utilisateur
def role():
    while True:
        choice = input("Veuillez entrer votre choix -> ")
        if choice == "1":
            return True
            break
        elif choice == "2":
            return False
            break
        else:
            print("Saisie invalide")


# Prochaines fonctions

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin des fonction et debut de l'application >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Exécution
print("Bienvenue sur notre plateforme d'achat")
print("")
print("Administrateur ? - Tapez 1          |          Client ? - Tapez 2")
print("")
print("")

# Ici on commence à écrire en fonction du retour de la fonction role.
# Par exemple je gère les clients donc dès que la role retourne false, j'écris mon code
if not role():
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Début du code de roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    print("Roche écrit ici")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Toi Kévin tu écris à partir d'ici (ton interface et tes appels de fonctions)
else:
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Debut du code Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    print("Kévin écrit ici")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
