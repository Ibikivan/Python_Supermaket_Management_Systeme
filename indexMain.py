import copy
import csv
import random
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
    "totalExpenses" : 0,
    "fidelityPoints" : 0
}

# puis on crée la liste catalogue et une liste vierge de clients
productCatalog = []
clientsList = []

# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associé

#fonction pour identifier le gagnant de la semaine
#une fonction qui trie les clients par ordre décroissant des dépenses
def sortByExpense(client):
    return client.get('totalExpenses')
#fonction qui trie les clients
def sortByPoint(client):
    return client.get('fidelityPoints')

#on lit le csv qui a la liste des client et leurs informations puis on ajoute au tableau
with open('clients.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            #print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            #print(f'id: {row[0]} name: {row[1]}, totalExpenses: {row[2]}, fidelityPoints: {row[3]}')  
            currentClient = copy.deepcopy(clientsModel)  
            currentClient["id"] = row[0]  
            currentClient["name"] = row[1]  
            currentClient["totalExpenses"] = int(row[2])  
            currentClient["fidelityPoints"] = int(row[3])   
            clientsList.append(currentClient)  
            lineCount += 1  
    #print(f'Processed {lineCount} lines.')
    
    #on utilise la fonction qui va trier les clients par ordre de dépenses
    clientsList.sort(key=sortByExpense, reverse=True)
    clientOrder = clientsList[:15]

    #on liste les 10 meilleurs clients
    print(f'Voici les 10 meilleurs sur le total de {lineCount-1} clients')
    for client in clientOrder:
        print (f'Nom : {client["name"]}, Total des dépenses : {client["totalExpenses"]}, Solde Points de fidélité : {client["fidelityPoints"]}')
    
    #le vainqueur est choisi aléatoirement parmi les 10
    winner = random.choice(clientOrder)
    print("le gagnat du bon d'achat de 10 000F est...")
    print("Loading...")
    print("{} !".format(winner["name"]))

    #identifier les 3 clients qui ont le plus de points de fidelité
    clientOrder.sort(key=sortByPoint, reverse=True)
    print(f'Voici les 03 meilleurs sur le total de {lineCount-1} clients')
    for client in clientOrder[:3]:
        print (f'Nom : {client["name"]}, Total des dépenses : {client["totalExpenses"]}, Solde Points de fidélité : {client["fidelityPoints"]}')
    
