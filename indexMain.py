import copy
import datetime
import csv
import random

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
    'gains': 0,
    "bonAchat": 0
}

# puis on crée la liste catalogue et une liste vierge de clients
productCatalog = []

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
        elif choice == choice4:
            return 0
            break
        else:
            print(invalidInputStatement)

# Fonction pour recuperer un nombre saisi par l'utilisateur 
def inputTest(proposal):
    while True:
        try:
            number = int(input("{} -> " . format(proposal)))
            break
        except:
            print("Erreur !! - Veuillez entrer un nombre SVP!")
    return number

#fonction qui retourne la liste des produits dont le stock est inferieur à la limite indiquée
def lowProductList(limit):
    resultat = []
    for product in productCatalog:
        if product["quantity"] < limit:
            resultat.append(product)
    return resultat

def afficheListeProduits(liste: list):
    print('Num\t|\tNom\t      Quantite\t          PrixU')
    for produit in liste:
        print(produit['id'], '\t|', produit['name'], ' \t      ', produit['quantity'], '\t          ', produit['price'])

def manageCsvFile():
    r = csv.reader(open('listeDeProduits.csv')) # Here your csv file
    lines = list(r)
    print(lines)
    return csv.writer(open('listeDeProduits.csv', 'w', newline=''))

def productAdd(name,quantity,price):
    newProductList=copy.deepcopy(productsModel)
    newProductList["name"]=name
    newProductList["quantity"]=quantity
    newProductList["price"]=price
    newProductList["id"]=len(productCatalog)
    productCatalog.append(newProductList)
    return newProductList

def productUpdateQuantity(name,quantity):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['quantity']=products['quantity'] + quantity
        return products

def productUpdatePrice(name ,price):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['price']=price
        return products
    
def productDel(name):
    exist=checkProduct(name)
    if exist :
        del productCatalog[int(exist)]

def checkProduct(name: str):
    i=0
    exist=False
    for products in productCatalog:
        if name.casefold()==str(products['name']).casefold():
            exist=True
            return str(i)
        i+=1
    
    if not exist:
        print("This product doesnot exist")
        return exist

def getProductName(prompt):
    while True:
        name = input(prompt)
        i = checkProduct(name)
        if i:
            return productCatalog[int(i)]['name']

#fonction pour identifier le gagnant de la semaine
#une fonction qui trie les clients par ordre décroissant des dépenses
def sortByExpense(client):
    return client.get('totalExpenses')

#fonction qui trie les clients
def sortByPoint(client):
    return client.get('fidelityPoints')

def getClientsList():
    #on lit le csv qui a la liste des client et leurs informations puis on ajoute au tableau
    with open('clients.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  
        lineCount = 0  
        clientsList = []
        for row in csvReader:
            if lineCount == 0:
                #print(f'Column names are: {", ".join(row)}')  
                lineCount += 1  
            else:  
                #print(f'id: {row[0]} name: {row[1]}, totalExpenses: {row[2]}, fidelityPoints: {row[3]}')  
                currentClient = copy.deepcopy(clientsModel)  
                currentClient["id"] = int(row[0])  
                currentClient["name"] = row[1]  
                currentClient["totalExpenses"] = float(row[2])  
                currentClient["fidelityPoints"] = int(row[3])   
                currentClient["gains"] = int(row[4])   
                currentClient["bonAchat"] = int(row[5])   
                clientsList.append(currentClient)  
                lineCount += 1  
        #print(f'Processed {lineCount} lines.')
        return clientsList

clientsList = getClientsList()

def bestClients(num):      
    #on utilise la fonction qui va trier les clients par ordre de dépenses
    clientsList.sort(key=sortByExpense, reverse=True)
    clientOrder = clientsList[:num]
    return clientOrder

'''    #on liste les 10 meilleurs clients
    print(f'Voici les 10 meilleurs sur le total de {lineCount-1} clients')
    for client in clientOrder:
        print (f'Nom : {client["name"]}, Total des dépenses : {client["totalExpenses"]}, Solde Points de fidélité : {client["fidelityPoints"]}')
'''

def findWinner():
    resultat = []
    #le vainqueur est choisi aléatoirement parmi les 10
    winner = random.choice(bestClients(10))
    winner['bonAchat'] = 10000
    resultat.append(winner)
    #on reinitialise la valeur des depenses totales de tous les clients
    return resultat

def afficheListeClients(liste: list):
    print('Num\t|\t\tNom\t\t                Depenses Totales\t          Valeur Bon D\'achat')
    for client in liste:
        print(client['id'], '\t|', client['name'], ' \t\t\t                ', client['totalExpenses'], '\t\t          ', client['bonAchat'])

'''    print("le gagnat du bon d'achat de 10 000F est...")
    print("Loading...")
    print("{} !".format(winner["name"]))

    #identifier les 3 clients qui ont le plus de points de fidelité
    clientOrder.sort(key=sortByPoint, reverse=True)
    print(f'Voici les 03 meilleurs sur le total de {lineCount-1} clients')
    for client in clientOrder[:3]:
        print (f'Nom : {client["name"]}, Total des dépenses : {client["totalExpenses"]}, Solde Points de fidélité : {client["fidelityPoints"]}')
'''
# Prochaines fonctions ROche


# Kévin stp ajoute tes fonctions à intégrer à partir d'ici

#Kevin Task: Une alerte sera remontée lorsque le stock d’un produit sera inférieur à 20
#l'idee ici est de presenter a l'administrateur la liste des produits dont le stock est bas, lorsqu'il se connecte
def alerteStock():
    resultat = []
    #recuperons les produits dont le stock est bas dans la liste
    for produit in productCatalog:
        if produit['quantity'] < 20:
            resultat.append(produit)
    #affichons ces produits s'il y'en a
    if resultat != []:
        print('\n Alerte! Ces produits ont atteint le stock critique: \n')
        afficheListeProduits(resultat)
        print('\n')
        input('Appuyez sur Entrer pour continuer: ')

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

        adminMenu()

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


# Prochaine fonction interface Roche

# Kévin stp ajoute tes fonctions d'interface à partir d'ici

# Menu d'administration
def displayAdminMenu():
    print('''\tEntrez le nombre correspondant à l'action choisie.
            1- Ajouter des produits au catalogue
            2- Modifier les produits disponibles
            3- Voir la liste des produits dont le stock a une limite
            4- Identifier les 3 mailleurs clients
            5- Tirer au sort le gagnant de la semaine    
            0- Revenir au menu precedent ''')

    return inputTest('Faites votre choix: ')

def adminMenu():
    selectedMenu = 0
    alerteStock()
    print('\n\tBienvenue sur la plateforme d\'Administration.')
    while True:
        action = displayAdminMenu()        
        if action == 0:
            roleSelectionMenu()
        elif action == 1:
            i = 0
            while True:
                i += 1
                produit = ['']
                name = input('Definir le nom du produit: ')
                qtity = inputTest('Definir la quantité: ')
                price = inputTest('Definir le prix: ')
                print('\nProduit ajoute avec succes')
                produit[0] = productAdd(name,qtity,price)
                afficheListeProduits(produit)
                if not input('Entrez 1 pour ajouter un autre produit ou Autre chose pour sortir: ') == '1':
                    break
            print('\n',i,'Produit(s) Ajoute(s) au catalogue.')
            if input('Entrez 0 pour Quitter ou autre chose pour revenir au menu precedent: ') == '0':
                break
        elif action == 2:
            i = 0
            whatToModify = doubleChoice('Entrez 1 pour modifier la Quantité ou 2 pour modifier le prix: ', '1', '2', 'Saisie Incorrecte!!!')
            if whatToModify:
                while True:
                    i += 1
                    produit = ['']
                    name = getProductName('Entrez le nom du produit à modifier: ')
                    qtity = inputTest('\nEntrez la quantité positive à ajouter(5) ou negative à retirer(-5): ')
                    print('\nProduit modifié avec succes')
                    produit[0] = productUpdateQuantity(name,qtity)
                    afficheListeProduits(produit)
                    if not input('\nEntrez 1 pour modifier un autre produit ou Autre chose pour sortir: ') == '1':
                        break
            else:
                while True:
                    i += 1
                    produit = ['']
                    name = input('Entrez le nom du produit à modifier: ')
                    price = inputTest('Definissez le nouveau prix du produit: ')
                    print('\nProduit modifié avec succes')
                    produit[0] = productUpdatePrice(name,price)
                    afficheListeProduits(produit)
                    if not input('\nEntrez 1 pour modifier un autre produit ou Autre chose pour sortir: ') == '1':
                        break
            print('\n',i,'Produit(s) modifié(s).')
            if input('\nEntrez 0 pour Quitter ou autre chose pour revenir au menu precedent: ') == '0':
                break
        elif action == 3:
            while True:
                limit = inputTest('Veuillez entrer la limite à controler')
                liste = lowProductList(limit)
                if len(liste) == 0:
                    print('il n\'y a pas de produit dont le stock est inferieur à ',limit,'\n')
                else:
                    print('le stock de ces produits est inferieur à ',limit,':')
                    afficheListeProduits(liste)
                if not input('Entrez 1 pour effectuer un autre contrôle ou Autre chose pour sortir: ') == '1':
                    break
            print('\n','Control de stock Terminé.')
            if input('\nEntrez 0 pour Quitter ou autre chose pour revenir au menu precedent: ') == '0':
                break
        elif action == 4:
            print('\nles 3 meilleurs clients sur',len(clientsList),'sont:')
            afficheListeClients(bestClients(3))
            if input('\nEntrez 0 pour Quitter ou autre chose pour revenir au menu precedent: ') == '0':
                break
        elif action == 5:
            print("Le gagnat du bon d'achat de 10 000F est...")
            print("Loading...")
            input('... Pressez Entrer pour le découvrir...\n')
            afficheListeClients(findWinner())
            #print(findWinner())
            if input('\nEntrez 0 pour Quitter ou autre chose pour revenir au menu precedent: ') == '0':
                break
    print(productCatalog)

# Prochaine fonction d'interface Kévin

# fin des fonctions de menu et début du processus d'exécution de l'application

productCatalog = [{"id": 1, "name": "OchocoAuLait", "quantity": 10, "price": 50},
                  {"id": 2, "name": "ParleG", "quantity": 10, "price": 50},
                  {"id": 3, "name": "Naya", "quantity": 100, "price": 50},
                  {"id": 4, "name": "Marie", "quantity": 100, "price": 50},
                  {"id": 5, "name": "Cream", "quantity": 100, "price": 50}]

roleSelectionMenu()
