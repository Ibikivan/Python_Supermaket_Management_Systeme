from ast import Delete
import copy
import csv
from operator import ne
from turtle import update
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

# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associé
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
    productCatalog.append(newProductList)
    #writer = manageCsvFile()
    #writer.writerows(newProductList.values())
    return newProductList

def productUpdateQuantity(name,quantity):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['quantity']=quantity

def productUpdatePrice(name,price):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['price']=price

    
def productDel(name):
    exist=checkProduct(name)
    if exist :
        del productCatalog[int(exist)]

def checkProduct(name):
    i=0
    exist=False
    for products in productCatalog:
        if name.casefold()==products['name'].casefold():
            exist=True
            return str(i)
            #products.clear()
       # else:
          #  return "This product doesnot exist"
        i+=1
    
    if not exist:
        print("This product doesnot exist")
        return exist



apple=productAdd("Apple",25,200)
banana=productAdd("banana",22,100)
#print(apple)
#applelist=apple.values()
#print(applelist)
productDel('apple')
productUpdateQuantity('banana',60)
productUpdatePrice('banana',200)
print(productCatalog)
#print(manageCsvFile)