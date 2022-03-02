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

# Créons la fonctionnalité de listage des produits dont la quantité en stock est inférieure à 10
# Pour les besoins des tests je crée un catalogue de quelques produits (une fonction que j'appelle plusieurs fois)
def clientCreator(id, name, expenses):
    currentClient = copy.deepcopy(clientsModel)
    currentClient["id"] = id
    currentClient["name"] = name
    currentClient["totalExpenses"] = expenses
    clientsList.append(currentClient)
    return currentClient


# Maintenant je crée ma fonction qui va m'indiquer les produit achetables avec mes points
# pour commencer je crée une fonction qui va calculer l'équivalence des points en argent
def howMuchItWorth(points):
    # Ici une fonction va être appelée et son résultat retourné dans une variable. Pas de paramètres au final
    pointsValue = points * 100
    return pointsValue


# ensuite je crée une fonction qui récupère ce nombre de point et affiche les produits qui y équivalent
def couldIBuyList():
    for


clientCreator(1, "ibikiv", 30000)
clientCreator(2, "dylan", 25000)
clientCreator(3, "jacques", 110000)
clientCreator(4, "marina", 18000)
clientCreator(5, "sanson", 534000)



print(howMuchItWorth(50))
