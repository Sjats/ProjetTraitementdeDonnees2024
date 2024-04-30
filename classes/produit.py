import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from article import Article
from prix import Prix
from fonctions.domaine_a_pays import domaine_a_pays
import numpy as np

"""
    Examples
    --------
    >>> p1 = Produit("riz", {"riz1": Article('001', Prix('EUR', 10), "France"),
                     "riz2": Article("002", Prix('EUR', 20), "Espagne"),
                     "riz3": Article("003", Prix('EUR', 40), "Allemagne"),
                     "riz4": Article("004", Prix('EUR', 30), "Italie")})
    >>> print(p1._CalculIndicesProduit())
    [{'France': 0.0, 'Espagne': 0.33, 'Allemagne': 1.0, 'Italie': 0.67}, {'France': 1.0, 'Espagne': 2.0, 'Allemagne': 4.0, 'Italie': 3.0}]
    """
class Produit:
    def __init__(self, nom: str, articles: dict):
        """Initialise un objet Produit avec un nom et un dictionnaire
        d'articles.

        Parameters
        ----------
        nom : str
            Le nom du produit.

        articles : dict
            Un dictionnaire contenant des articles associés au produit,
            où les clés sont les noms des articles et les valeurs sont
            des objets Article.

        Returns
        -------
        Produit
            Un objet Produit initialisé avec le nom et les articles fournis.
        """
        self._nom = nom
        self._articles = articles

    def _CalculIndicesProduit(self):
        """Calcule les indices associés au produit, à savoir indices01 et
        indicesfrance.
        Les indices sont calculés en fonction des prix moyens des articles par
        pays.

        Returns
        -------
        list
            Une liste contenant deux dictionnaires :
            indices01 (dict) : Un dictionnaire des indices 0-1 par pays,
                               où les clés sont les noms des pays et les
                               valeurs sont les indices calculés.
            indicesfrance (dict) : Un dictionnaire des indices par rapport au
                                   prix en France par pays, où les clés sont
                                   les noms des pays et les valeurs sont les
                                   indices calculés.
        """
        # Initialisation des variables de stock
        indices01 = dict()
        indicesfrance = dict()
        prix_prod = dict()
        L = []
        M = []

        # Calcul du prix moyen par pays
        # et stock dans prix_prod : dict(pays, prix_moyen)
        for key in self._articles.keys():
            i = 0
            prix_prod_m = 0
            for key2 in self._articles.keys():
                if self._articles[key]._pays == self._articles[key2]._pays:
                    prix_prod_m += self._articles[key]._prix.montant_euros
                    i += 1
            prix_prod_m /= i
            prix_prod[self._articles[key]._pays] = prix_prod_m

        # Exclusion des valeurs extrêmes
        for value in prix_prod.values():
            L.append(value)
        q1, q3 = np.percentile(L, 25), np.percentile(L, 75)
        vai = q1 - (q3-q1)*1.5
        vas = q3 + (q3-q1)*1.5
        for keys in prix_prod.keys():
            if prix_prod[keys] < vai or prix_prod[keys] > vas:
                prix_prod[keys] = None
        for value in prix_prod.values():
            if value is not None:
                M.append(value)

        # Définition des variables utiles pour le calcul des indices
        prix_max = max(M)
        prix_min = min(M)
        if prix_prod['France'] is not None:
            prix_france = prix_prod['France']

        # Calcul de indices01
        for key in self._articles.keys():
            if prix_prod[self._articles[key]._pays] is not None:
                ind01 = (prix_prod[self._articles[key]._pays] - prix_min)
                ind01 /= (prix_max - prix_min)
                ind01 = round(ind01, 2)
                indices01[self._articles[key]._pays] = ind01

        # Calcul de indicesfrance
        for key in self._articles.keys():
            if prix_prod[self._articles[key]._pays] is not None:
                indfrance = round(prix_prod[self._articles[key]._pays] / prix_france, 2)
                indicesfrance[self._articles[key]._pays] = indfrance

        # Return des indices
        return [indices01, indicesfrance]

if __name__ == "__main__":
    p1 = Produit("riz", {"riz1": Article('001', Prix('EUR', 10), "France"),
                        "riz2": Article("002", Prix('EUR', 20), "Spain"),
                        "riz3": Article("003", Prix('EUR', 40), "Germany"),
                        "riz4": Article("004", Prix('USD', 30), "Italy")})
    p2 = Produit("pat", {"pat1": Article('101', Prix('EUR', 35), "France"),
                        "pat2": Article("102", Prix('EUR', 25), "Spain"),
                        "pat3": Article("103", Prix('EUR', 15), "Germany"),
                        "pat4": Article("104", Prix('USD', 27), "Italy")})
    print(p1._CalculIndicesProduit())
    print(p2._CalculIndicesProduit())

    def bddinterfaceprod():
        indiceprod = dict()
        for pays in domaine_a_pays.values():
            indicepays = dict()
            for prod in [p1, p2]:
                if pays not in prod._CalculIndicesProduit()[0].keys():
                    indicepays[prod._nom] = np.nan
                else :
                    indicepays[prod._nom] = [prod._CalculIndicesProduit()[0][pays], prod._CalculIndicesProduit()[1][pays]]
            indiceprod[pays] = indicepays
        return indiceprod

    print(bddinterfaceprod())


