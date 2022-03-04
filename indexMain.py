import copy
import datetime

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
    "fidelityPoints": 0
}

# puis on crée la liste catalogue et une liste vierge de clients
productCatalog = []
clientsList = []


# Vous pouvez écrire vos fonctions à partir d'ici Merci d'écrire de façon propre et de commenter vos codes Une ligne
# d'espace entre les blocs de code et deux entre les grands blocs de code Une ligne d'espace avant les commentaires
# et pas de ligne d'espace en dessous, entre le commentaire et le bloc de code associé

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Toutes les fonctions ici >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Fonction à appeler chaque fois qu'il faudra poser une interrogation à 2 choix à l'utilisateur
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
def role():
    while True:
        choice = input("Veuillez entrer votre choix -> ")
        if choice == "1":
            return True
            break
        elif choice == "2":
            return False
            break
        else:
            print("Saisie invalide")

#affiche une liste de produits passés en paramètre
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
        input('Appuyez sur Entrer pour continuer: ')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin des fonction et debut de l'application >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Exécution
print("Bienvenue sur notre plateforme d'achat")
print("")
print("Administrateur ? - Tapez 1          |          Client ? - Tapez 2")
print("")
print("")

# Ici on commence à écrire en fonction du retour de la fonction role.
# Par exemple je gère les clients donc dès que le role retourne false, j'écris mon code
if not role():
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Début du code de roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    print("Roche écrit ici")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Roche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Toi Kévin tu écris à partir d'ici (ton interface et tes appels de fonctions)
else:
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Debut du code Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    alerteStock()
    print(''' 
        Bienvenue sur la plateforme d'Administration.
        Entrez le nombre correspondant à l'action choisie.
            1- Ajouter des produits au catalogue
            2- Modifier le stock des produits présents
            3- Voir la liste des produits dont le stock est inferieur à 10
            4- Identifier les 3 mailleurs clients
            5- Tirer au sort le gagnant de la semaine    ''')
        
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fin du code de Kévin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
