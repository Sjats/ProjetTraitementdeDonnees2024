from produit import Produit
from article import Article
from prix import Prix
import numpy as np


class CategorieProduit:
    def __init__(self, nom: str, produits: dict[str, Produit]):
        self._nom = nom
        self._produits = produits
    
    def _CalculIndicesCategories(self):
        # Initialisation des variables de stock
        nombre_cat = dict()
        prix_cat = dict()
        indicescat01 = dict()
        indicescatfrance = dict()
        L=[]
        M=[]
        for produit in self._produits.values():
            for article in produit._articles.values():
                prix_cat[article._pays] = 0
                nombre_cat[article._pays] = 0

        for prod in self._produits.values():
            prix_prod = dict()
            # Calcul du prix moyen par pays
            # et stock dans prix_prod : dict(pays, prix_moyen)
            for key in prod._articles.keys():
                i = 0
                prix_prod_m = 0
                for key2 in prod._articles.keys():
                    if prod._articles[key]._pays == prod._articles[key2]._pays:
                        prix_prod_m += prod._articles[key]._prix._ConversionEuros()
                        i += 1
                prix_prod_m /= i
                prix_prod[prod._articles[key]._pays] = prix_prod_m
            for pays in prix_prod.keys():
                prix_cat[pays] += prix_prod[pays]
                nombre_cat[pays] += 1
            # Ici, j'ai la somme des prix des produits de la catégorie par pays
            # Et le nombre de pays dont le prix est référencé dans le pays.
        for pays in prix_cat.keys():
            prix_cat[pays] /= nombre_cat[pays]
        # Exclusion des valeurs extrêmes
        for value in prix_cat.values():
            L.append(value)
        q1, q3 = np.percentile(L, 25), np.percentile(L, 75)
        vai = q1 - (q3-q1)*1.5
        vas = q3 + (q3-q1)*1.5
        for keys in prix_cat.keys():
            if prix_cat[keys] < vai or prix_cat[keys] > vas:
                prix_cat[keys] = None
        for value in prix_cat.values():
            if value is not None:
                M.append(value)

        # Définition des variables utiles pour le calcul des indices
        prix_max = max(M)
        prix_min = min(M)
        if prix_cat['France'] is not None:
            prix_france = prix_cat['France']

        # Calcul de indicescat01
        for pays in prix_cat.keys():
            if prix_cat[pays] is not None:
                indcat01 = (prix_cat[pays] - prix_min)
                indcat01 /= (prix_max - prix_min)
                indcat01 = round(indcat01, 2)
                indicescat01[pays] = indcat01

        # Calcul de indicescatfrance
        for pays in prix_cat.keys():
            if prix_cat[pays] is not None:
                indcatfrance = round(prix_cat[pays] / prix_france, 2)
                indicescatfrance[pays] = indcatfrance

        # Return des indices
        return [indicescat01, indicescatfrance]


p1 = Produit("riz", {"riz1": Article('001', Prix('EUR', 10), "France"),
                    "riz2": Article("002", Prix('EUR', 20), "Espagne"),
                    "riz3": Article("003", Prix('EUR', 40), "Allemagne"),
                    "riz4": Article("004", Prix('EUR', 30), "Italie")})
p2 = Produit("pat", {"pat1": Article('101', Prix('EUR', 35), "France"),
                    "pat2": Article("102", Prix('EUR', 25), "Espagne"),
                    "pat3": Article("103", Prix('EUR', 15), "Allemagne"),
                    "pat4": Article("104", Prix('EUR', 27), "Italie")})
print(p1._CalculIndicesProduit())
print(p2._CalculIndicesProduit()) 
c1 = CategorieProduit("nourriture", {"riz": p1, "pat": p2})
print(c1._CalculIndicesCategories())

