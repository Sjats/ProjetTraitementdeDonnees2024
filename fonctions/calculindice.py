

from ..classes.article import Article
import numpy as np


class Produit:
    def __init__(self, nom, articles):
        self._nom = nom
        self._articles = articles
    
    def _calculindicesproduit(self):
        indices = dict()
        prix_prod = dict()
        L=[]
        for key in self._articles.keys():
            i=0
            for key2 in self._articles.keys():
                if self._articles[key]._pays == self._articles[key2]._pays:
                    prix_prod_moyen +=  self._articles[key].prix._conversioneuros()
                    i+=1
            prix_prod_moyen /= i
            prix_prod[self._articles[key]._pays] = prix_prod_moyen

        for value in prix_prod.values():
            L.append(value)

        vai = np.percentile(L, 25) - (np.percentile(L, 75)-np.percentile(L, 25))*1.5
        vas = np.percentile(L, 75) + (np.percentile(L, 75)-np.percentile(L, 25))*1.5
        
        for keys in prix_prod.keys():
            if prix_prod[keys] < vai or prix_prod[keys] > vas:
                prix_prod[keys] = None
        
        ind1 = (prix_prod - prix_min) / (prix_max - prix_min)

        for key in self._articles.keys():
            indices[self._articles[key]._pays] = ind1