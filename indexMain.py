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

# The CRUD on products 

#managecsvfile nous retour une liste contenant les elements du fichier csv
def manageCsvFile():
    r = csv.reader(open('listeDeProduits.csv')) # Here your csv file
    lines = list(r)
    return lines

def productAdd(name,quantity,price):
    newProductList=copy.deepcopy(productsModel)
    newProductList["name"]=name
    newProductList["quantity"]=quantity
    newProductList["price"]=price
    #productCatalog.append(newProductList)

    #add the values to a list and write in csv file
    exist=checkIfExistInCsv(name)
    if not exist :
        fieldname = [newProductList["id"] , name , quantity , price]
        lines=manageCsvFile()
        writer = csv.writer(open('listeDeProduits.csv', 'w', newline=''))
        writer.writerows(lines)
        writer.writerow(fieldname)
    
    return newProductList

#quantity=restOfQuantity
def productUpdateQuantity(name,quantity):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['quantity']=quantity
#update the values in csv file but check first if the product by name exist
    exist=checkIfExistInCsv(name)
    if exist :
        lines=manageCsvFile()
        lines[int(exist)][2]= quantity
        # print(lines)
        writer = csv.writer(open('listeDeProduits.csv', 'w', newline=''))
        writer.writerows(lines)

def productUpdatePrice(name,price):
    exist=checkProduct(name)
    if exist:
        products=productCatalog[int(exist)]
        products['price']=price
#pour modifier dans le fichier csv
#update the values in csv file but check first if the product by name exist
    exist=checkIfExistInCsv(name)
    if exist :
        lines=manageCsvFile()
        lines[int(exist)][3]= price
        # print(lines)
        writer = csv.writer(open('listeDeProduits.csv', 'w', newline=''))
        writer.writerows(lines)

    
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
    #increment to check the next column
        i+=1
    
    if not exist:
        print("This product doesnot exist")
        return exist

def checkIfExistInCsv(name):
    exist=False
    r = csv.reader(open('listeDeProduits.csv')) # Here your csv file
    lines = list(r)
  #  print(lines)
    i=0
    for column in lines:
    # print(column)
        if name.casefold() in column:  
            exist=True
            return str(i)
 #increment to check the next column
        i=i+1
    if not exist:
        print("This product doesnot exist")
        return exist

def productReadCsv():
    newProductList=copy.deepcopy(productsModel)
    lines=manageCsvFile()
    for row in lines:
        name=row[1]
        quantity=int(row[2])
        price=float(row[3])
        if not name=="name":
            newProductList=copy.deepcopy(productsModel)
            newProductList["name"]=name
            newProductList["quantity"]=quantity
            newProductList["price"]=price
            productCatalog.append(newProductList)
    return newProductList
#checkIfExistInCsv('banana')
#apple=productAdd('Apple',25,200)
#banana=productAdd('banana',22,100)
#bonbon=productAdd('bonbon',30,100)

#print(apple)
#applelist=apple.values()
#print(applelist)
#productDel('apple')
#productUpdateQuantity('bol',100)
#productUpdatePrice('banana',600)
#print(productCatalog)
#print(manageCsvFile)
hey=productReadCsv()
print(productCatalog)
