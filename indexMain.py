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

# Fonction à appeler chaque fois qu'il faudra poser une interrogation totale avec un choix récurrent à l'utilisateur
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
def doubleChoice(proposal, choice1, choice2, invalidInputStatement):
    while True:
        choice = input("{} -> ".format(proposal))
        if choice == choice1:
            return True
            break
        elif choice == choice2:
            return False
            break
        else:
            print(invalidInputStatement)


def tripleChoice(proposal, choice1, choice2, choice3, invalidInputStatement):
    while True:
        choice = input("{} -> ".format(proposal))
        if choice == choice1:
            return 1
            break
        elif choice == choice2:
            return 2
            break
        elif choice == choice3:
            return 0
            break
        else:
            print(invalidInputStatement)


def fouthChoice(proposal, choice1, choice2, choice3, choice4, invalidInputStatement):
    while True:
        choice = input("{} -> ".format(proposal))
        if choice == choice1:
            return 1
            break
        elif choice == choice2:
            return 2
            break
        elif choice == choice3:
            return 3
            break
        elif choice == choice3:
            return 0
            break
        else:
            print(invalidInputStatement)


def afficheListeProduits(liste: list):
    print('Num\t|\tNom\t      Quantite\t          PrixU')
    for produit in liste:
        print(produit['id'], '\t|', produit['name'], ' \t      ', produit['quantity'], '\t          ', produit['price'])


# Prochaines fonctions

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin des fonction et debut de l'application >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# à partir d'ici se trouvent les fonctions des différents menus que j'ai créés pour l'exécution

# Cette fonction affiche le menu du choix entre admin et client et est la première fonction appelée. Penser à lui donner
# un choix d'arrêt pour quitter le programme
def roleSelectionMenu():
    print("")
    print("Bienvenue sur notre plateforme d'achat")
    print("")
    print("Administrateur ? - Tapez 1          |          Client ? - Tapez 2")
    print("")
    print("")

    # Ici on commence à écrire en fonction du retour de la fonction role.
    # Par exemple je gère les clients donc dès que la role retourne false, j'écris mon code
    if not doubleChoice("Veuillez entrer votre choix", "1", "2", "Saisie invalide !"):
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Début du code de roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # ce code doit afficher la liste des produits du catalogue et propose d'entrer de jeux au client s'il souhaite
        # acheter, connaître son solde de points et afficher les produits qu'ils peuvent acheter.
        clientsMenu()

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Toi Kévin tu écris à partir d'ici (ton interface et tes appels de fonctions)
    else:
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Debut du code Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        print(
            tripleChoice("Veuillez entrer un choix pour tester la fonction", "1", "2", "3", "saisie invalide de test"))

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Cette fonction affiche le catalogue et le menu d'accueil de client
def clientsMenu():
    print("")
    print("BIENVENUE AU SUPER MARCHE SPAR")
    print("voici ci-dessous notre catalogue de produits :")
    print()

    afficheListeProduits(productCatalog)

    print("")
    print("Veuillez choisir une action à effectuer !")
    clientSelect = tripleChoice("Faire un achat ? - Tapez '1'    |    Consulter votre solde de points ? - Tapez '2'  "
                                "  |    Quitter ? - Tapez '0'", "1", "2", "0", "Veuillez faire un choix valide SVP"
                                                                               " !!")

    # Après avoir appelé la fonction 'tripleChoice pour permettre à l'utilisateur de faire un choix, j'utilise le
    # retour de cette fonction pour afficher le prochain menu choisit par l'utilisateur
    if clientSelect == 1:
        buyingMenu()
    elif clientSelect == 2:
        print("pointsMenu()")
    elif clientSelect == 0:
        roleSelectionMenu()


def buyingMenu():
    print("vous êtes sur le point de faire un achat !")


# Prochaine fonction

# fin des fonctions de menu et début du processus d'exécution de l'application

productCatalog = [{"id": 1, "name": "OchocoAuLait", "quantity": 10, "price": 50},
                  {"id": 2, "name": "ParleG", "quantity": 10, "price": 50},
                  {"id": 3, "name": "Naya", "quantity": 100, "price": 50},
                  {"id": 4, "name": "Marie", "quantity": 100, "price": 50},
                  {"id": 5, "name": "Cream", "quantity": 100, "price": 50}]

roleSelectionMenu()
