from classes.categorie_produit import CategorieProduit
import pickle

with open("donnees/base_produit.pkl", "rb") as file:
    bdd_produits = pickle.load(file)

NomsCategories = ['Electronique', 'Mobilier', 'Electromenager_Ustensiles',
                  'Nourriture']

liste_prod_cat = [
    ['AA+alkaline+battery+pack', 'Bluetooth+wireless+earbuds',
     'Fitness smartwatch', 'Waterproof backpack', 'USB-C charging cable',
     'Electric toothbrush', 'Polarized sunglasses'],
    ['Modular storage shelf', 'LED+desk+lamp', 'Non-slip+yoga+mat',
     'Digital bathroom scale'],
    ['Non-stick cookware set', 'Essential oil diffuser',
     'First aid kit', 'Paper coffee filters', 'Professional kitchen knife',
     'Biodegradable toilet paper'],
    ['cheese', 'beef', 'potatoes', 'lettuce', 'onions', 'apples',
     'blueberries', 'ice cream', 'bread', 'milk', 'eggs', 'yogurt', 'chicken',
     'fish', 'rice', 'pasta', 'bananas']

]

cat = []

for nom_cat in range(len(NomsCategories)):
    cat.append(CategorieProduit(NomsCategories[nom_cat], dict()))

    for nom_prod in bdd_produits.keys():
        if nom_prod in liste_prod_cat[nom_cat]:
            cat[-1]._produits[nom_prod] = bdd_produits[nom_prod]


for c in cat:
    c._CalculIndicesCategories()
    c.EnregistrementCategorieProduit()
    c.EnregistrementIndicesCategorieProduit()
