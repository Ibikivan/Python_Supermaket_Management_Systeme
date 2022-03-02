import copy
<<<<<<< HEAD
import datetime
from queue import Empty
=======
>>>>>>> 957526e2dcd7dda8ce151d1f3884c59902b2491f

# J'ai importé copy à l'avance
# Début du programme. C'est à partir d'ici qu'on écrira le code

# On commence par préparer les différents models de données à manipuler
# On crée les models de produits et clients
productsModel = {
    "ref": "",
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
#productCatalog = []
#clientsList = []
productCatalog = [{"id" : 1,"name" : "Ochoco","quantity" : 10,"price" : 50},{"id" : 2,"name" : "ParleG","quantity" : 10,"price" : 50},{"id" : 3,"name" : "Naya","quantity" : 100,"price" : 50},{"id" : 4,"name" : "Marie","quantity" : 100,"price" : 50},{"id" : 5,"name" : "Cream","quantity" : 100,"price" : 50}]
clientsList = [{"id" : 1,"name" : "Patricia","totalExpenses" : 0.0,"fidelityPoints" : 0},{"id" : 2,"name" : "Yolande","totalExpenses" : 0.0,"fidelityPoints" : 0}]


# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et aucun espace en dessous, entre le commentaire et le bloc de code associé

# Créons la fonctionnalité de listage des produits dont la quantité en stock est inférieure à 10
# Pour les besoins des tests je crée un catalogue de quelques produits (une fonction que j'appelle plusieurs fois)
def productCreator(ref, name, stock, price):
    currentProduct = copy.deepcopy(productsModel)
    currentProduct["ref"] = ref
    currentProduct["name"] = name
    currentProduct["quantity"] = stock
    currentProduct["price"] = price
    productCatalog.append(currentProduct)
    return currentProduct


# Maintenant je vais créer une fonction pour simuler la vente en enlevant un élément au stock des produits
def sellSimulator(productName, quantity):
    for product in productCatalog:
        if product["name"] == productName:
            product["quantity"] -= quantity


# Maintenant je crée ma fonction qui va lister les produits dont le stock est inférieur à 10
def lowProductList(limit):
    chip = 1
    print("ATTENTION ! Liste des produit dont le stock est inférieur à {} unités" . format(limit))
    for product in productCatalog:
        if product["quantity"] < limit:
            print("{}. {} -> {} : stock actuel = {} unités" . format(chip, product["ref"], product["name"], product["quantity"]))
            chip += 1


productCreator("ba01", "banana", 50, 200)
productCreator("ma01", "mango", 50, 100)
productCreator("rul01", "ruler", 50, 50)
productCreator("phone01", "smart Phone", 50, 30000)
productCreator("tle01", "table", 50, 15000)

sellSimulator("table", 49)
sellSimulator("smart Phone", 47)
sellSimulator("banana", 42)
sellSimulator("ruler", 35)

lowProductList(10)

<<<<<<< HEAD
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
        print('Alerte! Ces produits ont atteint le stock critique')
        print(resultat)

#Kevin Task: Log Files
#REF: https://waytolearnx.com/2020/06/date-et-heure-en-python.html
#l'idee est de resortir la structure a mettre en place pour produire un log d'activite
#le fichier de log dans le repertoire courant est nome log.txt
#le log contient les informations suivantes
# { la date, l'heure, l'action(du texte decrivant l'action effectuee),  }
def addToLog(libele):
    #on ouvre le fichier en mode d'ajout 
    date = datetime.datetime.now()
    print(date.strftime('%A'))

#addToLog('')
alerteStock()
=======
#print(productCatalog)
>>>>>>> 957526e2dcd7dda8ce151d1f3884c59902b2491f
