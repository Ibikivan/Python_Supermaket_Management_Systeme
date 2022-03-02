import copy

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
productCatalog = []
clientsList = []


# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et aucun espace en dessous, entre le commentaire et le bloc de code associé

# Maintenant je crée ma fonction qui va m'indiquer les produit achetables avec mes points
# Pour les besoins des tests je crée un catalogue de quelques produits (une fonction que j'appelle plusieurs fois)
def productCreator(ref, name, stock, price):
    currentProduct = copy.deepcopy(productsModel)
    currentProduct["ref"] = ref
    currentProduct["name"] = name
    currentProduct["quantity"] = stock
    currentProduct["price"] = price
    productCatalog.append(currentProduct)
    return currentProduct


# pour commencer je crée une fonction qui va calculer l'équivalence des points en argent
def howMuchItWorth(points):
    # Ici une fonction va être appelée pour récupérer les dépenses du client et calculer ses points et son résultat
    # retourné dans une variable Pas de paramètres nécessaires dans la version définitive de cette fonction
    pointsValue = points * 100
    return pointsValue


# ensuite je crée une fonction qui récupère ce nombre de point et affiche les produits qui y équivalent
def couldIBuyList():
    montant = howMuchItWorth(10)
    cheap = 1
    print("voici les produits que vous pouvez acheter actuellement avec vos points :")
    for product in productCatalog:
        if product["price"] <= montant:
            print("{}. {} -> prix: {}; quantité restante: {}".format(cheap, product["name"], product["price"],
                                                                     product["quantity"]))
            cheap += 1


productCreator("ba01", "banana", 50, 200)
productCreator("ma01", "mango", 50, 100)
productCreator("rul01", "ruler", 50, 50)
productCreator("phone01", "smart Phone", 50, 30000)
productCreator("tle01", "table", 50, 15000)

couldIBuyList()
