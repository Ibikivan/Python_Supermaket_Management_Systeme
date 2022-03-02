import copy
from pickle import TRUE
from unicodedata import name
# J'ai importé copy à l'avance
# Début du programme. C'est à partir d'ici qu'on écrira le code

# On commence par préparer les différents models de données à manipuler
# On crée les models de produits et clients
productsModel = {
    "id" : 0,
    "name" : "",
    "quantity" : 0,
    "price" : 0
}

clientsModel = {
    "id" : 0,
    "name" : "",
    "totalExpenses" : 0.0,
    "fidelityPoints" : 0
}

# puis on crée la liste catalogue et une liste vierge de clients
productCatalog = []
clientsList = []
productCatalog = [ 
    { "id":1, "name":"biscuit", "prix":1000, "quantity":20},   {"id":3, "name":"riz", "prix":3000, "quantity":10},
    {"id":2, "name":"bonbons", "prix":1200, "quantity":25},     {"id":4, "name":"pattes", "prix":2000, "quantity":30}
]

clientsList = [
    {"id":1, "name":"nat", "totalExpenses":0}
]

# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associer 
# Permettre a un client d effectuer un achat

def afficheliste():
    for produit in productCatalog:
        print("name : {}; prix : {}; quantiteRestante : {}".format(produit["name"], produit["prix"], produit["quantity"]))


def achatProduit (produitChoix, quantityChoix):
    for produit in productCatalog:
        if produitChoix == produit["name"]:
            total = quantityChoix * produit["prix"]
            produit["quantity"] -= quantityChoix
            print("achat confirmé de {} {} à un prix total de {}" . format(quantityChoix, produitChoix, total))
            return total


def pointsCumule(): 
    client = clientsList[0]
    totalCumule = client["totalExpenses"]/100
    print ("votre total de point cumule est: {}".format(int(totalCumule)))


def achatencours():
    totalAchat = 0
    while True:
        print("liste lesproduits")
        afficheliste()
        print("")
        print("Bonjour vous êtes sur le point de faire un achat :")
        choix = input("veuillez indiquer le produit sohaité: -> ")
        quantite = int(input("combien voulez-vous de {}: -> ". format(choix)))

        prix = achatProduit(choix, quantite)
        if prix:
            print("")
        else:
            print("desolé vous entré un produit qui n'exsite pas !")
            prix = 0

        totalAchat += prix
        continuer = input("Contunuer ? -> ")
        if continuer == "non":
            print ("vos depenses totales s'elevent à : {}" .format (totalAchat))
            client = clientsList[0]
            client["totalExpenses"] += totalAchat
            print (clientsList)
            pointsCumule()
            break


achatencours()


    