import pickle
from classes.article import Article
from classes.prix import Prix
import numpy as np


class Produit:
    def __init__(self, nom: str, articles: dict[str, Article]):
        """Initialise un objet Produit avec un nom et un dictionnaire
        d'articles.

        Parameters
        ----------
        nom : str
            Le nom du produit.

        articles : dict[str, Article]
            Un dictionnaire contenant des articles associés au produit,
            où les clés sont les noms des articles et les valeurs sont
            des objets Article.

        Returns
        -------
        Produit
            Un objet Produit initialisé avec le nom et les articles fournis.
        """
        # Vérification des types des arguments
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une instance de str.")

        if not isinstance(articles, dict):
            raise TypeError(
                "Les articles doivent être une instance de dictionnaire."
            )

        for nom_article in articles.keys():
            if not isinstance(nom_article, str):
                raise TypeError(
                    "Les clés du dictionnaire d'articles doivent être une "
                    "instance de str."
                )

        for nom_article in articles.values():
            if not isinstance(nom_article, Article):
                raise TypeError(
                    "Les valeurs du dictionnaire d'articles doivent être "
                    "une instance d'Article"
                )

        # Initialisation des attributs
        self._nom = nom
        self.__select_articles(articles)
        self._CalculIndicesProduit()

    def _CalculIndicesProduit(self):
        """Calcule les indices associés aux produits.
        Les indices sont calculés en fonction des prix moyens des articles par
        pays.

        Returns
        -------
        list:
            Une liste contenant deux dictionnaires :
            indices01 (dict) : Un dictionnaire des indices 0-1 par pays pour
                                  leproduits, où les clés sont les noms des
                                  pays et les valeurs sont les indices
                                  calculés.
            indicesfrance (dict) : Un dictionnaire des indices par rapport
                                      au prix en France par pays pour le
                                      produit, où les clés sont les noms des
                                      pays et les valeurs sont les indices
                                      calculés.
        """
        # Initialisation des variables de stock
        indices01 = dict()
        indicesfrance = dict()
        prix_prod = dict()
        L = []  # Liste pour stocker les prix moyens par pays

        # Calcul du prix moyen par pays
        for key in self._articles.keys():
            i = 0
            prix_prod_m = 0
            for key2 in self._articles.keys():
                if self._articles[key]._pays == self._articles[key2]._pays:
                    if self._articles[key]._prix.montant is not None:
                        self._articles[key]._prix = Prix(
                            self._articles[key]._prix.devise,
                            self._articles[key]._prix.montant)
                        prix_prod_m += self._articles[key]._prix.montant_euros
                        i += 1
            if i != 0:
                prix_prod_m /= i
                prix_prod[self._articles[key]._pays] = prix_prod_m
                L.append(prix_prod_m)

        # Exclusion des valeurs extrêmes
        if len(L) > 0:
            q1, q3 = np.percentile(L, 25), np.percentile(L, 75)
            vai = q1 - (q3 - q1) * 1.5
            vas = q3 + (q3 - q1) * 1.5
            M = [value for value in L if vai <= value <= vas]
        else:
            M = []

        # Calcul des indices seulement si M contient des valeurs
        if len(M) > 0:
            prix_max = max(M)
            prix_min = min(M)
            if prix_prod['France'] is not None:
                prix_france = prix_prod['France']

        # Calcul de indices01
        for key in self._articles.keys():
            if self._articles[key]._pays in prix_prod:
                if prix_prod[self._articles[key]._pays] is not None:
                    if prix_prod[self._articles[key]._pays] in M:
                        ind01 = (
                            prix_prod[self._articles[key]._pays] - prix_min
                            )
                        ind01 /= (prix_max - prix_min)
                        ind01 = round(ind01, 2)
                        indices01[self._articles[key]._pays] = ind01
                    else:
                        pass
            else:
                pass

        # Calcul de indicesfrance
        for key in self._articles.keys():
            if self._articles[key]._pays in prix_prod:
                if prix_prod[self._articles[key]._pays] is not None:
                    if prix_prod[self._articles[key]._pays] in M:
                        indfrance = round(
                            prix_prod[self._articles[key]._pays] / prix_france,
                            2
                            )
                        indicesfrance[self._articles[key]._pays] = indfrance
                    else:
                        pass

        # Return des indices
        self.indices = [indices01, indicesfrance]

    def Enregistrement_prod(self):
        """
        Fonction qui enregistre les produits
        """
        with open("donnees/base_produit.pkl", "rb") as file:
            database_fichier = pickle.load(file)

        database_fichier.update({self._nom: self})

        with open("donnees/base_produit.pkl", "wb") as file:
            pickle.dump(database_fichier, file)

    def __select_articles(self, articles):
        self._articles = {}
        self._pays = []
        for art in articles.keys():
            aux = art.split("/")
            if aux[1] == self._nom:
                self._articles.update({art: articles[art]})
                if aux[0] not in self._pays:
                    self._pays.append(aux[0])
