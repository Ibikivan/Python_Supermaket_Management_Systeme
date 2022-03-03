import copy
import datetime

LOGFILE = 'market.log'
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
#productCatalog = []
#clientsList = []
productCatalog = [{"id" : 1,"name" : "OchocoAuLaituiop","quantity" : 10,"price" : 50},{"id" : 2,"name" : "ParleG","quantity" : 10,"price" : 50},{"id" : 3,"name" : "Naya","quantity" : 100,"price" : 50},{"id" : 4,"name" : "Marie","quantity" : 100,"price" : 50},{"id" : 5,"name" : "Cream","quantity" : 100,"price" : 50}]
clientsList = [{"id" : 1,"name" : "Patricia","totalExpenses" : 0.0,"fidelityPoints" : 0},{"id" : 2,"name" : "Yolande","totalExpenses" : 0.0,"fidelityPoints" : 0}]

# Vous pouvez écrire vos fonctions à partir d'ici
# Merci d'écrire de façon propre et de commenter vos codes
# Une ligne d'espace entre les blocs de code et deux entre les grands blocs de code
# Une ligne d'espace avant les commentaires et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associé

def afficheListeProduits(liste :list):
    print('Num\t|\tNom\t      Quantite\t          PrixU')
    for produit in liste:
        print(produit['id'],'\t|',produit['name'],' \t      ',produit['quantity'],'\t          ',produit['price'])

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
        afficheListeProduits(resultat)



#Kevin Task: Log Files
#REF: https://waytolearnx.com/2020/06/date-et-heure-en-python.html
#l'idee est de resortir la structure a mettre en place pour produire un log d'activite
#le fichier de log dans le repertoire courant est nome log.txt
#le log contient les informations suivantes
# { la date, l'heure, l'auteur, l'action(du texte decrivant l'action effectuee),  }
def addToLog(actor,libele):
    #on ouvre le fichier en mode d'ajout 
    date = datetime.datetime.now()
    logContent = ''
    logContent += date.strftime('%A')+' '+ str(date.day) +'-'+str(date.month)+'-'+str(date.year) +' a '+str(date.hour)+':'+str(date.minute) +' '+actor +' '+libele
    logFile = open(LOGFILE,'a')
    logFile.write(logContent +'\n')
    logFile.close()

addToLog('Stephane','buy shoes for 5000frs')
#alerteStock()
afficheListeProduits(productCatalog)
