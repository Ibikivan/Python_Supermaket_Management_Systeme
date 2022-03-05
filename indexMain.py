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
    "fidelityPoints": 0,
    "gains": 0.0
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


# Cette fonction demande une saisie de nombre entier et le retourne si la saisie ne déclenche aucune exception
def intInputTest(proposal):
    while True:
        try:
            number = int(input("{} -> ".format(proposal)))
            break
        except:
            print("Erreur !! - Veuillez entrer un nombre SVP!")
    return number


# Cette fonction demande une saisie de nombre flottant et le retourne si la saisie ne déclenche aucune exception
def floatInputTest(proposal):
    while True:
        try:
            number = float(input("{} -> ".format(proposal)))
            break
        except:
            print("Erreur !! - Veuillez entrer un nombre SVP!")
    return number


# Fonction de Kévin pour afficher la liste des produits du catalogue non csv
def afficheListeProduits(liste: list):
    print('Num\t|\tNom\t      Quantite\t          PrixU')
    for produit in liste:
        print(produit['id'], '\t|', produit['name'], ' \t      ', produit['quantity'], '\t          ', produit['price'])


# Les 3 prochaines fonctions sont réalisée par natacha pour permettre à un client d'effectuer un achat
# Fonction qui effectue l'achat proprement dit et de soustraire la quantité achetée au catalogue et retourne le prix tle
def buyProduct(produitChoice, quantity):
    for produit in productCatalog:
        if produitChoice == produit["name"]:
            total = quantity * produit["price"]
            produit["quantity"] -= quantity
            print("achat confirmé de {} {} à un prix total de {}".format(quantity, produitChoice, total))
            return total


# Cette fonction calcule total de points d'un client en fonction de ses achats et les lui attribue
def pointsCount(name):
    for client in clientsList:
        if client["name"] == name:
            points = int(client["totalExpenses"] / 100)
    return points


# Cette fonction réalise invite le client à réaliser l'achat et exécute toute la procédure
def currentBuy(name):
    totalAchat = 0
    print("liste les produits:")
    afficheListeProduits(productCatalog)
    print("")
    print("Bonjour vous êtes sur le point de faire un achat :")

    while True:
        # On récupère les valeurs à envoyer en paramètre à la fonction d'achat
        choice = input("veuillez indiquer le produit souhaité: -> ")
        quantity = intInputTest("combien voulez-vous de {}: -> ".format(choice))  # on vérifie le type de la qté

        print("")
        prix = buyProduct(choice, quantity)  # on appelle la fonction d'achat et on récupère le montant total des achats
        if prix:  # penser à vérifier les quantités en stock avant l'achat
            print("")
        else:
            print("désolé vous entré un produit qui n'existe pas !")
            prix = 0

        totalAchat += prix
        continuer = userTotalInterrogation("Acheter autre chose ? - Tapez Entrer    |    Tapez 'non' pour Arrêter",
                                           "non", "Veuillez entrer un choix valide SVP !")
        if not continuer:
            print("vos dépenses totales s'élèvent à : {}".format(totalAchat))

            # Puis on ajoute le montant total des achats au client
            for client in clientsList:
                if client["name"] == name:
                    client["totalExpenses"] += totalAchat

            # Et on ajoute le nombre de points total dû à ces achats client
            for client in clientsList:
                if client["name"] == name:
                    client["fidelityPoints"] = pointsCount(name)
            break


# Cette fonction va vérifier l'existence d'un utilisateur et retourner True s'il existe
def isHeExist(name):
    for client in clientsList:
        if client["name"] == name:
            return True

    return False


def clientIdentification(idPurpose):
    print("{}, veuillez vous identifier svp !!".format(idPurpose))
    name = input("Quel est votre nom ? - > ")
    addClient(name)
    return name


# Cette fonction va vérifier l'existence d'un client et l'ajouter s'il n'existe pas
def addClient(name):
    if not isHeExist(name):
        currentClient = copy.deepcopy(clientsModel)
        currentClient["id"] = currentClient["id"] = len(clientsList) + 1
        currentClient["name"] = name
        clientsList.append(currentClient)
        print("client ajouté à la liste")
        return True
    else:
        print("ce lient existe déjà")


# Maintenant je crée ma fonction qui va m'indiquer les produit achetables avec mes points
# pour commencer je crée une fonction qui va calculer l'équivalence des points en argent
def howMuchItWorth(points):
    # Ici une fonction va être appelée pour récupérer les dépenses du client et calculer ses points et son résultat
    # retourné dans une variable Pas de paramètres nécessaires dans la version définitive de cette fonction
    pointsValue = points * 100
    return pointsValue


def couldIBuyList():
    montant = howMuchItWorth(10)
    cheap = 1
    print("voici les produits que vous pouvez acheter actuellement avec vos points :")
    for product in productCatalog:
        if product["price"] <= montant:
            print("{}. {} -> prix: {}; quantité restante: {}".format(cheap, product["name"], product["price"],
                                                                     product["quantity"]))
            cheap += 1


# Prochaines fonctions Roche


# Kévin stp ajoute tes fonctions à intégrer à partir d'ici

# ---- Ici -------

# Prochaines fonctions Kévin

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

        print("Kévin appelle ses fonctions ici")

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
        promotionalMenu()
    elif clientSelect == 0:
        roleSelectionMenu()


def buyingMenu():
    name = clientIdentification("vous êtes sur le point de faire un achat")

    while True:
        currentBuy(name)

        relay = userTotalInterrogation("Tapez Entrer pour revenir au MENU CLIENTS    |    Tapez '1' pour acheter "
                                       "de nouveau", "1", "Erreur de saisie, veuillez recommencer !")
        if relay:
            clientsMenu()
            break


def promotionalMenu():
    # le client devra déjà être dans la liste des clients
    print("Je demande au client de s'identifier")
    name = clientIdentification("Nous allons consulter votre solde de points")

    print("j'affiche la liste des produits achetables avec le nombre de points de ce client")

    print("je met en forme et j'affiche le nombre de points du client")

    print("ici j'affiche les propositions Acheter avec ses points ou retourner au menu")


# Prochaine fonction interface Roche

# Kévin stp ajoute tes fonctions d'interface à partir d'ici

# ---- Ici -------

# Prochaine fonction d'interface Kévin

# fin des fonctions de menu et début du processus d'exécution de l'application

productCatalog = [{"id": 1, "name": "OchocoAuLait", "quantity": 10, "price": 50},
                  {"id": 2, "name": "ParleG", "quantity": 10, "price": 50},
                  {"id": 3, "name": "Naya", "quantity": 100, "price": 50},
                  {"id": 4, "name": "Marie", "quantity": 100, "price": 50},
                  {"id": 5, "name": "Cream", "quantity": 100, "price": 50}]

clientsList = [
    {"id": 1, "name": "nat", "totalExpenses": 0, "fidelityPoints": 0, "gains": 0.0}
]

#addClient("roche")

# roleSelectionMenu()

addClient("roche")
addClient("Audrey")
addClient("Audrey")

#print(isHeExist("audrey"))

print(clientsList)

# print(inputTest("Veuillez fournir un nombre à vérifier svp !!"))
