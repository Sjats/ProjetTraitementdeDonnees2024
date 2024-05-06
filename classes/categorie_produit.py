import os
import pickle
import numpy as np
from classes.produit import Produit
from classes.prix import Prix


class CategorieProduit:
    def __init__(self, nom: str, produits: dict[str, Produit]):
        """Initialise un objet CategorieProduit avec un nom et un dictionnaire
        de produits associés.

        Parameters
        ----------
        nom : str
            Le nom de la catégorie de produits.
        produits : dict[str, Produit]
            Un dictionnaire contenant des produits associés à la catégorie,
            où les clés sont les noms des produits et les valeurs sont des
            objets Produit.

        Returns
        -------
        CategorieProduit:
            Un objet CategorieProduit initialisé avec le nom et les produits
            fournis.
        """
        # Vérification des types des arguments
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une instance de str.")

        if not isinstance(produits, dict):
            raise TypeError(
                "Les produits doivent être une instance de dictionnaire."
            )

        for produit_nom in produits.keys():
            if not isinstance(produit_nom, str):
                raise TypeError(
                    "Les clés du dictionnaire de produits doivent être une "
                    "instance de str."
                )

        for produit in produits.values():
            if not isinstance(produit, Produit):
                raise TypeError(
                    "Les valeurs du dictionnaire de produits doivent être une "
                    "instance de Produit"
                )

        # Initialisation des attributs
        self._nom = nom
        self._produits = produits
        self._CalculIndicesCategories()

    def _CalculIndicesCategories(self):
        """Calcule les indices associés à la catégorie de produits.
        Les indices sont calculés en fonction des prix moyens des articles par
        pays pour tous les produits de la catégorie.

        Returns
        -------
        list:
            Une liste contenant deux dictionnaires :
            indicescat01 (dict) : Un dictionnaire des indices 0-1 par pays pour
                                  la catégorie de produits, où les clés sont
                                  les noms des pays et les valeurs sont les
                                  indices calculés.
            indicescatfrance (dict) : Un dictionnaire des indices par rapport
                                      au prix en France par pays pour la
                                      catégorie de produits, où les clés sont
                                      les noms des pays et les valeurs sont les
                                      indices calculés.
        """
        # Initialisation des variables de stock
        nombre_cat = dict()
        prix_cat = dict()
        indicescat01 = dict()
        indicescatfrance = dict()
        L = []
        M = []
        for produit in self._produits.values():
            for article in produit._articles.values():
                prix_cat[article._pays] = 0
                nombre_cat[article._pays] = 0

        for prod in self._produits.values():
            prix_prod = dict()
            # Calcul du prix moyen par pays
            # et stock dans prix_cat : dict(pays, prix_moyen)
            for key in prod._articles.keys():
                i = 0
                prix_prod_m = 0
                for key2 in prod._articles.keys():
                    if prod._articles[key]._pays == prod._articles[key2]._pays:
                        if prod._articles[key]._prix.montant is not None:
                            prod._articles[key]._prix = Prix(
                                prod._articles[key]._prix.devise,
                                prod._articles[key]._prix.montant)
                            prix_prod_m += (
                                prod._articles[key]._prix.montant_euros)
                            i += 1
                if i != 0:
                    prix_prod_m /= i
                    prix_prod[prod._articles[key]._pays] = prix_prod_m
            for pays in prix_prod.keys():
                prix_cat[pays] += prix_prod[pays]
                nombre_cat[pays] += 1
        for pays in prix_cat.keys():
            if prix_cat[pays] is not None and nombre_cat[pays] is not None:
                if nombre_cat[pays] != 0:
                    prix_cat[pays] /= nombre_cat[pays]

        # Exclusion des valeurs extrêmes
            for value in prix_cat.values():
                if value is not None:
                    L.append(value)
            if len(L) > 0:
                q1, q3 = np.percentile(L, 25), np.percentile(L, 75)
                vai = q1 - (q3-q1)*1.5
                vas = q3 + (q3-q1)*1.5
                for keys in prix_cat.keys():
                    if prix_cat[keys] is not None:
                        if prix_cat[keys] < vai or prix_cat[keys] > vas:
                            prix_cat[keys] = None
                for value in prix_cat.values():
                    if value is not None:
                        M.append(value)

        # Définition des variables utiles pour le calcul des indices
        if len(M) > 0:
            prix_max = max(M)
            prix_min = min(M)
            if prix_cat['France'] is not None:
                prix_france = prix_cat['France']
        else:
            pass

        # Calcul de indicescat01
        for pays in prix_cat.keys():
            if prix_cat[pays] is not None:
                if prix_cat[pays] in M:
                    indcat01 = (prix_cat[pays] - prix_min)
                    indcat01 /= (prix_max - prix_min)
                    indcat01 = round(indcat01, 2)
                    indicescat01[pays] = indcat01
                else:
                    pass

        # Calcul de indicescatfrance
        for pays in prix_cat.keys():
            if prix_cat[pays] is not None:
                if prix_cat[pays] in M:
                    indcatfrance = round(prix_cat[pays] / prix_france, 2)
                    indicescatfrance[pays] = indcatfrance
                else:
                    pass

        # Return des indices
        self.indices = [indicescat01, indicescatfrance]

    def EnregistrementCategorieProduit(self):
        """
        Fonction qui enregistre les catégories dans l'endroit indiqué

        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre les catégories
        """

        if not os.path.exists("donnees/base_categorie.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = dict()

        else:
            # Ouvre la BDD
            with open("donnees/base_categorie.pkl", "rb") as file:
                database_fichier = pickle.load(file)

        database_fichier.update({self._nom: self})

        with open("donnees/base_categorie.pkl", "wb") as file:
            pickle.dump(database_fichier, file)
