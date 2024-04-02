from article import Article
from prix import Prix
import numpy as np


class Produit:
    def __init__(self, nom: str, articles: dict):
        self._nom = nom
        self._articles = articles

    def _calculindicesproduit(self):
        # Initialisation des variables de stock
        indices01 = dict()
        indicesfrance = dict()
        prix_prod = dict()
        L = []
        M = []

        # Calcul du prix moyen par pays et stock dans prix_prod : dict(pays, prix_moyen)
        for key in self._articles.keys():
            i = 0
            prix_prod_moyen = 0
            for key2 in self._articles.keys():
                if self._articles[key]._pays == self._articles[key2]._pays:
                    prix_prod_moyen += self._articles[key]._prix._conversioneuros()
                    i += 1
            prix_prod_moyen /= i
            prix_prod[self._articles[key]._pays] = prix_prod_moyen

        # Exclusion des valeurs extrêmes
        for value in prix_prod.values():
            L.append(value)
        vai = np.percentile(L, 25) - (np.percentile(L, 75)-np.percentile(L, 25))*1.5
        vas = np.percentile(L, 75) + (np.percentile(L, 75)-np.percentile(L, 25))*1.5
        for keys in prix_prod.keys():
            if prix_prod[keys] < vai or prix_prod[keys] > vas:
                prix_prod[keys] = None
        for value in prix_prod.values():
            if value != None:
                M.append(value)

        # Définition des variables utiles pour le calcul des indices
        prix_max = max(M)
        prix_min = min(M)
        if prix_prod['France'] != None:
            prix_france = prix_prod['France']

        # Calcul de indices01
        for key in self._articles.keys():
            if prix_prod[self._articles[key]._pays] != None:
                ind01 = (prix_prod[self._articles[key]._pays] - prix_min) / (prix_max - prix_min)
                indices01[self._articles[key]._pays] = ind01
        
        # Calcul de indicesfrance
        for key in self._articles.keys():
            if prix_prod[self._articles[key]._pays] != None:
                indfrance = prix_prod[self._articles[key]._pays] / prix_france
                indicesfrance[self._articles[key]._pays] = indfrance
        
        # Return des indices
        return [indices01, indicesfrance]

p1 = Produit('riz', {'000': Article('000', Prix('EUR', 8000.0), 'Angleterre'), '001': Article('001', Prix('EUR',50.0), 'France'), '002': Article('002', Prix('EUR',20.0), 'Espagne'),'003': Article('003', Prix('EUR',30.0), 'Allemagne')})

print(p1._articles)
print(p1._calculindicesproduit())

