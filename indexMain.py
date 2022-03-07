import copy
import csv

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
    "won": 0.0
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
def buyProduct(produitChoice, quantity, totalAchat):
    for produit in productCatalog:
            if produitChoice == produit["name"]:
                if produit["quantity"] >= quantity:
                    total = quantity * produit["price"]
                    produit["quantity"] -= quantity
                    print("achat confirmé de {} {} à un prix total de {}".format(quantity, produitChoice, total))
                    print("Totaux achats en cours {}. Atteignez 1000 Fr pour gagner 1 point! ;-)".format(totalAchat))
                    return total

                else:
                    print("Désolé il ne reste que {} - {} en stock".format(produit["quantity"], produit["name"]))
                    if userTotalInterrogation("Modifier vos quantités ? - Tapez 'Entrer'   |   Annuler l'achat ? Tapez '0'", "0", "Erreur de saisie, veuillez réessayer !"):
                        newQuantity = int(input("Entrer la nouvelle valeur -> "))
                        total = buyProduct(produitChoice, newQuantity, totalAchat)
                        return total

                    else:
                        print("Merci de votre patience, le stock sera vite mis à jour")
                        return True


def buyProductWithPoints(choice, quantity, name):
    montantPoints = 0

    for client in clientsList:
        if client["name"] == name:
            montantPoints = client["won"]

    for produit in productCatalog:
        if choice == produit["name"]:
            if produit["quantity"] >= quantity:
                total = quantity * produit["price"]

                if montantPoints >= total:
                    produit["quantity"] -= quantity
                    print("achat confirmé de {} {} à un prix total de {}".format(quantity, choice, total))
                    return total

                else:
                    print("désolé vos gains sont insuffisants pour faire cet achat !")
                    if userTotalInterrogation("Convertir vos point ? - Tapez 'Entrer'    |    Annuler ? - Tapez '0'", "0", "Erreur de saisie, Veuillez réessayer !"):
                        convertPointToWon(name)  #Convertis les points en argent et les attribuent au client
                        choice = input("veuillez indiquer le produit souhaité: -> ")
                        quantity = intInputTest("combien voulez-vous de {} ?:".format(choice))
                        total = buyProductWithPoints(choice, quantity, name)
                        return total

                    else:
                        return True

            else:
                print("Désolé il ne reste que {} - {} en stock".format(produit["quantity"], produit["name"]))
                if userTotalInterrogation("Modifier vos quantités ? - Tapez 'Entrer'   |   Annuler l'achat ? Tapez '0'",
                                          "0", "Erreur de saisie, veuillez réessayer !"):
                    newQuantity = intInputTest("Entrer la nouvelle valeur".format(choice))
                    total = buyProduct(choice, newQuantity)
                    return total

                else:
                    print("Merci de votre patience, le stock sera vite mis à jour")
                    return True


# Cette fonction calcule total de points d'un client en fonction de ses achats et les lui attribue
def pointsCount(currentExpenses):
    points = currentExpenses / 1000
    return int(points)


# Cette fonction réalise invite le client à réaliser l'achat et exécute toute la procédure
def currentBuy(name):
    totalAchat = 0

    while True:
        print("")
        print("liste les produits:")
        print("")
        afficheListeProduits(productCatalog)
        print("")

        for client in clientsList:
            if client["name"] == name:
                points = client["fidelityPoints"]
                wonValue = client["won"]

        # On récupère les valeurs à envoyer en paramètre à la fonction d'achat
        print("")
        print("'{}' - Total Points : {} - Total Gain : {}".format(name, points, wonValue))
        choice = input("veuillez indiquer le produit souhaité: -> ")
        quantity = intInputTest("combien voulez-vous de {} ?:".format(choice))  # on vérifie le type de la qté

        print("")
        prix = buyProduct(choice, quantity, totalAchat)  # on appelle la fonction d'achat et on récupère le montant total des achats
        if prix:  # penser à vérifier les quantités en stock avant l'achat
            print("")
        else:
            print("désolé vous avez sélectionné un produit qui n'existe pas !")
            print("")
            prix = 0

        totalAchat += prix

        continuer = userTotalInterrogation("Acheter autre chose ? - Tapez Entrer    |    Tapez '0' pour Arrêter",
                                           "0", "Veuillez entrer un choix valide SVP !")

        if not continuer:
            fidelity = pointsCount(totalAchat)
            print("Dépenses totales : {}    |    Points de fidélité gagnés : {}".format(totalAchat, fidelity))

            # Puis on ajoute le montant total des achats au client
            for client in clientsList:
                if client["name"] == name:
                    client["totalExpenses"] += totalAchat

            # Et on ajoute le nombre de points total dû à ces achats client
            for client in clientsList:
                if client["name"] == name:
                    client["fidelityPoints"] += fidelity
            break


def currentBuyWithPoints(name):
    totalAchat = 0

    while True:
        print("")
        print("liste les produits:")
        print("")
        couldIBuyList(name)
        print("")

        for client in clientsList:
            if client["name"] == name:
                points = client["fidelityPoints"]
                wonValue = client["won"]

        # On récupère les valeurs à envoyer en paramètre à la fonction d'achat
        print("'{}' - Total Points : {} - Total Gain : {}".format(name, points, wonValue))
        choice = input("veuillez indiquer le produit souhaité: -> ")
        quantity = intInputTest("combien voulez-vous de {} ?:".format(choice))  # on vérifie le type de la qté

        print("")
        prix = buyProductWithPoints(choice, quantity, name)  # on appelle la fonction d'achat et on récupère le montant total des achats
        if prix:  # penser à vérifier les quantités en stock avant l'achat
            print("")
        else:
            print("désolé vous avez sélectionné un produit qui n'existe pas !")
            prix = 0
            print("")

        # Et on retire le montant total des achats effectués aux gains totaux du client
        for client in clientsList:
            if client["name"] == name:
                client["won"] -= prix

        totalAchat += prix
        continuer = userTotalInterrogation("Acheter autre chose ? - Tapez Entrer    |    Tapez '0' pour Arrêter",
                                           "0", "Veuillez entrer un choix valide SVP !")

        if not continuer:
            print("Achats effectués !")
            print("")

            break


# Cette fonction va vérifier l'existence d'un utilisateur et retourner True s'il existe
def isHeExist(name):
    for client in clientsList:
        if client["name"] == name:
            return True

    return False


def clientIdentification(idPurpose):
    print("{}, veuillez vous identifier svp !!".format(idPurpose))
    name = input("Quel est votre nom ? -> ")
    addClient(name)
    return name


# Cette fonction va vérifier l'existence d'un client et l'ajouter s'il n'existe pas
def addClient(name):
    if not isHeExist(name):

        currentClient = copy.deepcopy(clientsModel)
        currentClient["id"] = currentClient["id"] = len(clientsList) + 1
        currentClient["name"] = name
        clientsList.append(currentClient)
        print("")
        print("Merci Mr/Mme {}, vous avez êtes ajouté à notre liste de clients !".format(name))
        print("")
        return True

    else:
        print("")
        print("Merci Mr/Mme {}, Content de vous retrouver".format(name))
        print("")


# Maintenant je crée ma fonction qui va m'indiquer les produit achetables avec mes points
# pour commencer je crée une fonction qui va calculer l'équivalence des points en argent
def howMuchItWorth(points):
    # Ici une fonction va être appelée pour récupérer les dépenses du client et calculer ses points et son résultat
    # retourné dans une variable Pas de paramètres nécessaires dans la version définitive de cette fonction
    pointsValue = points * 100
    return pointsValue


def convertPointToWon(name):
    for client in clientsList:
        if client["name"] == name:
            addValue = howMuchItWorth(client["fidelityPoints"])
            if addValue != 0:
                client["won"] += addValue
                client["fidelityPoints"] = 0
                print("")
                print("vos points on été convertis en {} Fcfa. Merci !".format(addValue))
                print("")
            else:
                print("")
                print("Désolé Mr/Mme {}, aucun point à convertir. Effectuez des achats normaux pour en gagner.".format(name))
                print("")

def couldIBuyList(name):
    # On récupère les points du client
    for client in clientsList:
        if client["name"] == name:
            points = client["fidelityPoints"]
            gains = client["won"]

    # On calcule la valeur de ces points en argent
    montant = howMuchItWorth(points)
    cheap = 1

    print("voici les produits que vous pouvez acheter actuellement avec vos points :")
    print("")
    for product in productCatalog:
        if product["price"] <= montant or product["price"] <= gains:
            print("{}. {} -> prix: {}; quantité restante: {}".format(cheap, product["name"], product["price"],
                                                                     product["quantity"]))
            cheap += 1

    return montant


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
    print("Administrateur ? - Tapez 1          |          Client ? - Tapez 2          |          Quitter ? - Tapez 0")
    print("")
    print("")

    # Ici on commence à écrire en fonction du retour de la fonction role.
    # Par exemple je gère les clients donc dès que la role retourne false, j'écris mon code
    relay = tripleChoice("Veuillez entrer votre choix", "1", "2", "0", "Saisie invalide !")
    if relay == 2:
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Début du code de roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # ce code doit afficher la liste des produits du catalogue et propose d'entrer de jeux au client s'il souhaite
        # acheter, connaître son solde de points et afficher les produits qu'ils peuvent acheter.
        clientsMenu()

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Toi Kévin tu écris à partir d'ici (ton interface et tes appels de fonctions)
    elif relay == 1:
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Debut du code Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        print("Kévin appelle ses fonctions ici")

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif relay == 0:
        outGoingMenu()


# Cette fonction affiche le catalogue et le menu d'accueil de client
def clientsMenu():
    print("")
    print("BIENVENUE AU SUPER MARCHE SPAR")
    print("voici ci-dessous notre catalogue de produits :")
    print()

    afficheListeProduits(productCatalog)

    print("")
    print("|----- une promotion est actuellement en cours, retrouvez les détails dans la section 'Consulter votre solde de points' -----|")

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
    print("")
    name = clientIdentification("vous êtes sur le point de faire un achat")

    while True:
        print("|------------------------------ MENU D'ACHATS ------------------------------|")

        currentBuy(name)

        relay = userTotalInterrogation("Tapez Entrer pour revenir au MENU CLIENTS    |    Tapez '1' pour acheter "
                                           "de nouveau", "1", "Erreur de saisie, veuillez recommencer !")
        if relay:
            clientsMenu()
            break



def promotionalMenu():
    # le client devra déjà être dans la liste des clients
    print("")
    name = clientIdentification("Nous allons consulter votre solde de points")

    while True:
        print("|---------------------------- MENU PROMOTIONNEL ----------------------------|")
        print("")

        for client in clientsList:
            if client["name"] == name:
                points = client["fidelityPoints"]
                id = client["id"]
                wonValue = client["won"]

        if couldIBuyList(name) != 0 or wonValue != 0:
            pass
        else:
            print("")
            print("Désolé vous ne pouvez rien acheter avec vos gains,")
            print("faites des achats ordinaires pour gagner des points à convertir !")

        print("")
        print("Durant la promotion, vos achats vous rapporteront des points de fidélité")
        print("et chaque semaines vous serez tiré au sors pour gagner un bon d'achat de 10 000 sur la base de vos achats.")

        print("")
        print("Client id : {} - Nom : {} - Total Points : {} - Total Gain : {}".format(id, name, points, wonValue))

        print("")
        relay = tripleChoice("Faire un achat avec vos points ? - Tapez '1'    |    convertir vos points ? - Tapez '2'    |    retour ? "
                     "- Tapez '0'", "1", "2", "0", "Erreur de saisie, veuillez recommencer !")

        if relay == 1:
            for client in clientsList:
                if client["name"] == name:
                    currentBuyWithPoints(name)
        elif relay == 2:
            convertPointToWon(name)
        elif relay == 0:
            clientsMenu()
            break


def outGoingMenu():
    print("")
    print("Merci d'avoir utilisé nos services. à la revoillure !!")


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
    {"id": 1, "name": "nat", "totalExpenses": 0, "fidelityPoints": 10, "won": 1000.0}
]

#addClient("roche")

roleSelectionMenu()

#addClient("roche")
#addClient("Audrey")
#addClient("Audrey")

#promotionalMenu()

#couldIBuyList("nat")

#currentBuyWithPoints("nat")

#buyingMenu()

#print(clientsList)

# print(inputTest("Veuillez fournir un nombre à vérifier svp !!"))
