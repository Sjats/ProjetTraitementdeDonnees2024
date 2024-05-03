import os
import pickle
from classes.article import Article
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
        # if not isinstance(nom, str):
        #     raise TypeError("Le nom doit être une instance de str.")

        # if not isinstance(articles, dict):
        #     raise TypeError(
        #         "Les articles doivent être une instance de dictionnaire."
        #     )

        # for nom_article in articles.keys():
        #     if not isinstance(nom_article, str):
        #         raise TypeError(
        #             "Les clés du dictionnaire d'articles doivent être une "
        #             "instance de str."
        #         )

        # for nom_article in articles.values():
        #     if not isinstance(nom_article, Article):
        #         raise TypeError(
        #             "Les valeurs du dictionnaire d'articles doivent être "
        #             "une instance d'Article"
        #         )

        # Initialisation des attributs
        self._nom = nom
        self._articles = articles

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
                        prix_prod_m += self._articles[key]._prix.montant
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
        return [indices01, indicesfrance]

    def EnregistrementProduit(self, adresse="donnees/"):
        """
        Fonction qui enregistre les produits dans l'endroit indiqué
        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre les produits
        """

        if not (isinstance(adresse, str) or adresse is None):
            raise TypeError("adresse est de type str")

        if not os.path.exists(adresse):
            raise ValueError("l'adresse fournie n'existe pas")

        if adresse is not None:
            self.adresse_fichier = adresse

        if not os.path.exists(self.adresse_fichier + "base_produit.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = dict()

        else:
            # Ouvre la BDD
            with open(self.adresse_fichier + "base_produit.pkl", "rb") as file:
                database_fichier = pickle.load(file)

        database_fichier.update(self)

        with open(self.adresse_fichier + "base_produit.pkl", "wb") as file:
            pickle.dump(database_fichier, file)

    def EnregistrementIndicesProduit(self, adresse="donnees/"):
        """
        Fonction qui enregistre les indice des produits dans l'endroit indiqué
        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre les indices des produits
        """

        if not (isinstance(adresse, str) or adresse is None):
            raise TypeError("adresse est de type str")

        if not os.path.exists(self.adresse_fichier):
            raise ValueError("l'adresse fournie n'existe pas")

        if adresse is not None:
            self.adresse_fichier = adresse

        if not os.path.exists(self.adresse_fichier +
                              "base_indice_produit.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = {}

        else:
            # Ouvre la BDD
            with open(self.adresse_fichier +
                      "base_indice_produit.pkl", "rb") as file:
                database_fichier = pickle.load(file)

        database_fichier.update(self._CalculIndicesProduit)

        with open(self.adresse_fichier +
                  "base_indice_produit.pkl", "wb") as file:
            pickle.dump(database_fichier, file)


NomsProduits = ['Pile', 'Airpods', 'Cable', 'Montre', 'Lampe', 'Tapis',
                'Senteur', 'Etagere', 'Balance', 'Poele', 'Fer', 'Couteau',
                'Kit de Survie', 'Brosse a dents', 'Support de Telephone',
                'Fromage', 'Boeuf', 'Patate', 'Salade', 'Onion', 'Pomme',
                'Myrtille', 'Glace', 'Pain', 'Lait', 'Oeuf', 'Yaourt',
                'Poulet', 'Poisson', 'Riz', 'Pates', 'Banane', 'Sac_a_dos',
                'Filtre a cafe', 'Papier Toilette']


Pile = Produit('Pile', dict())
Airpods = Produit('Airpods', dict())
Cable = Produit('Cable', dict())
Montre = Produit('Montre', dict())
Lampe = Produit('Lampe', dict())
Tapis = Produit('Tapis', dict())
Senteur = Produit('Senteur', dict())
Etagere = Produit('Etagere', dict())
Balance = Produit('Balance', dict())
Poele = Produit('Poele', dict())
Fer = Produit('Fer', dict())
Couteau = Produit('Couteau', dict())
Kit_de_Survie = Produit('Kit de Survie', dict())
Brosse_a_dents = Produit('Brosse a dents', dict())
Support_de_Telephone = Produit('Support de Telephone', dict())
Fromage = Produit('Fromage', dict())
Boeuf = Produit('Boeuf', dict())
Patate = Produit('Patate', dict())
Salade = Produit('Salade', dict())
Onion = Produit('Onion', dict())
Pomme = Produit('Pomme', dict())
Myrtille = Produit('Myrtille', dict())
Glace = Produit('Glace', dict())
Pain = Produit('Pain', dict())
Lait = Produit('Lait', dict())
Oeuf = Produit('Oeuf', dict())
Yaourt = Produit('Yaourt', dict())
Poulet = Produit('Poulet', dict())
Poisson = Produit('Poisson', dict())
Riz = Produit('Riz', dict())
Pates = Produit('Pates', dict())
Banane = Produit('Banane', dict())
Sac_a_dos = Produit('Sac_a_dos', dict())
Filtre_a_cafe = Produit('Filtre a cafe', dict())
Papier_Toilette = Produit('Papier Toilette', dict())


produits = [Pile, Airpods, Cable, Montre, Lampe, Tapis, Senteur, Etagere,
            Balance, Poele, Fer, Couteau, Kit_de_Survie, Brosse_a_dents,
            Support_de_Telephone, Fromage, Boeuf, Patate, Salade, Onion, Pomme,
            Myrtille, Glace, Pain, Lait, Oeuf, Yaourt, Poulet, Poisson, Riz,
            Pates, Banane, Sac_a_dos, Filtre_a_cafe, Papier_Toilette]


NomsArticles = ['AA+alkaline+battery+pack', 'Bluetooth+wireless+earbuds',
                'USB-C charging cable', 'Fitness smartwatch', 'LED+desk+lamp',
                'Non-slip+yoga+mat', 'Essential oil diffuser',
                'Modular storage shelf', 'Digital bathroom scale',
                'Non-stick cookware set', 'Steam iron',
                'Professional kitchen knife', 'First aid kit',
                'Electric toothbrush', 'Car phone mount', 'cheese', 'beef',
                'potatoes', 'lettuce', 'onions', 'apples', 'blueberries',
                'ice cream', 'bread', 'milk', 'eggs', 'yogurt', 'chicken',
                'fish', 'rice', 'pasta', 'bananas', 'Waterproof backpack',
                'Paper coffee filters', 'Biodegradable toilet paper']


Pays = ['United States', 'Singapore', 'Netherlands', 'Canada', 'Germany',
        'Spain', 'Sweden', 'Poland', 'Japan', 'Australia', 'Brazil', 'Turkey',
        'Mexico', 'United Kingdom', 'France', 'Italy', 'United Arab Emirates',
        'India', 'China', 'Russia']


def article_produit():
    with open("donnees/database.pkl", "rb") as file:
        dict_articles = pickle.load(file)
    for art in dict_articles.keys():
        for i in range(len(NomsArticles)):
            if art.split('/')[1] == NomsArticles[i]:
                produits[i]._articles[art] = dict_articles[art]


article_produit()


def bddinterfaceprod():
    """Crée la base de données nécessaire à l'interface pour accéder aux
    indices des produits par pays.
    Cette fonction parcourt les indices des produits pour chaque pays.
    Les indices sont stockés dans un dictionnaire de la forme
    {pays: {produit: [indice_01, indice_France]}}.

    Returns
    -------
    dict:
        Un dictionnaire contenant les indices des produits par pays.
        Les clés sont les noms des pays et les valeurs sont des dictionnaires
        contenant les indices des produits pour ce pays.
    """
    indiceprod = dict()
    for pays in Pays:
        indicepays = dict()
        for prod in produits:
            if pays not in prod._CalculIndicesProduit()[0].keys():
                indicepays[prod._nom] = np.nan
            else:
                indicepays[prod._nom] = (
                    [prod._CalculIndicesProduit()[0][pays],
                        prod._CalculIndicesProduit()[1][pays]]
                )
        indiceprod[pays] = indicepays
    return indiceprod
