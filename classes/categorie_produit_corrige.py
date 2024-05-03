import os
import pickle
from classes.produit import *
import numpy as np




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


    def __str__(self):
        return f'{self._nom}, {self._produits}'


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
                            prix_prod_m += prod._articles[key]._prix.montant
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


    def EnregistrementCategorieProduit(self, adresse="donnees/"):
        """
        Fonction qui enregistre les catégories dans l'endroit indiqué
        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre les catégories
        """


        if not (isinstance(adresse, str) or adresse is None):
            raise TypeError("adresse est de type str")


        if not os.path.exists(self.adresse_fichier):
            raise ValueError("l'adresse fournie n'existe pas")


        if adresse is not None:
            self.adresse_fichier = adresse


        if not os.path.exists(self.adresse_fichier + "base_categorie.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = {}


        else:
            # Ouvre la BDD
            with open(self.adresse_fichier +
                      "base_categorie.pkl", "rb") as file:
                database_fichier = pickle.load(file)


        database_fichier.update(self)


        with open(self.adresse_fichier + "base_categorie.pkl", "wb") as file:
            pickle.dump(database_fichier, file)


    def EnregistrementIndicesCategorieProduit(self, adresse="donnees/"):
        """
        Fonction qui enregistre les indice des catégories dans l'endroit
        indiqué


        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre les indices des catégories
        """


        if not (isinstance(adresse, str) or adresse is None):
            raise TypeError("adresse est de type str")


        if not os.path.exists(self.adresse_fichier):
            raise ValueError("l'adresse fournie n'existe pas")


        if adresse is not None:
            self.adresse_fichier = adresse


        if not os.path.exists(self.adresse_fichier +
                              "base_indice_categorie.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = {}


        else:
            # Ouvre la BDD
            with open(self.adresse_fichier +
                      "base_indice_categorie.pkl", "rb") as file:
                database_fichier = pickle.load(file)


        database_fichier.update(self._CalculIndicesCategories)


        with open(self.adresse_fichier +
                  "base_indice_categorie.pkl", "wb") as file:
            pickle.dump(database_fichier, file)




NomsCategories = ['Electronique', 'Mobilier', 'Electromenager_Ustensiles',
                  'Nourriture']


Electronique = CategorieProduit('Electronique', dict())
Mobilier = CategorieProduit('Mobilier', dict())
Electromenager_Ustensiles = CategorieProduit('Electromenager_Ustensiles',
                                             dict())
Nourriture = CategorieProduit('Nourriture', dict())


categories = [Electronique, Mobilier, Electromenager_Ustensiles, Nourriture]


NomsProduitsElectronique = ['Pile', 'Airpods', 'Cable', 'Montre']


NomsProduitsMobilier = ['Lampe', 'Tapis', 'Senteur', 'Etagere', 'Balance']


NomsProduitsUstensile = ['Poele', 'Fer', 'Couteau', 'Brosse a dents',
                         'Support de Telephone']


NomsProduitsNourriture = ['Fromage', 'Boeuf', 'Patate', 'Salade', 'Onion',
                          'Pomme', 'Myrtille', 'Glace', 'Pain', 'Lait', 'Oeuf',
                          'Yaourt', 'Poulet', 'Poisson', 'Riz', 'Pates',
                          'Banane', 'Sac_a_dos', 'Filtre a cafe',
                          'Papier Toilette']


produits = [Pile, Airpods, Cable, Montre, Lampe, Tapis, Senteur, Etagere,
            Balance, Poele, Fer, Couteau, Kit_de_Survie, Brosse_a_dents,
            Support_de_Telephone, Fromage, Boeuf, Patate, Salade, Onion, Pomme,
            Myrtille, Glace, Pain, Lait, Oeuf, Yaourt, Poulet, Poisson, Riz,
            Pates, Banane, Sac_a_dos, Filtre_a_cafe, Papier_Toilette]




def produit_categorie():
    for prod in produits:
        if prod._nom in NomsProduitsElectronique:
            Electronique._produits[prod._nom] = prod
        elif prod._nom in NomsProduitsMobilier:
            Mobilier._produits[prod._nom] = prod
        elif prod._nom in NomsProduitsUstensile:
            Electromenager_Ustensiles._produits[prod._nom] = prod
        elif prod._nom in NomsProduitsNourriture:
            Nourriture._produits[prod._nom] = prod




produit_categorie()




def bddinterfacecat():
    """Crée la base de données nécessaire à l'interface pour accéder aux
    indices des catégories de produits par pays.
    Cette fonction parcourt les indices des catégories pour chaque pays.
    Les indices sont stockés dans un dictionnaire de la forme
    {pays: {catégorie: [indice_01, indice_France]}}.


    Returns
    -------
    dict:
        Un dictionnaire contenant les indices des catégories de produits par
        pays.
        Les clés sont les noms des pays et les valeurs sont des dictionnaires
        contenant les indices des catégories de produits pour ce pays.
    """
    indicecat = dict()
    for pays in Pays:
        indicepays = dict()
        for cat in categories:
            if pays not in cat._CalculIndicesCategories()[0].keys():
                indicepays[cat._nom] = np.nan
            else:
                indicepays[cat._nom] = (
                    [cat._CalculIndicesCategories()[0][pays],
                     cat._CalculIndicesCategories()[1][pays]]
                )
        indicecat[pays] = indicepays
    return indicecat




if __name__ == "__main__":
    # Ca sera pour les tests
    # p1 = Produit("riz", {"riz1": Article('001', Prix('EUR', 10), "France"),
    #                      "riz2": Article("002", Prix('EUR', 20), "Spain"),
    #                      "riz3": Article("003", Prix('EUR', 25), "Germany"),
    #                      "riz4": Article("004", Prix('EUR', 30), "Italy")})
    # p2 = Produit("pat", {"pat1": Article('101', Prix('EUR', 35), "France"),
    #                      "pat2": Article("102", Prix('EUR', 25), "Spain"),
    #                      "pat3": Article("103", Prix('EUR', 15), "Germany"),
    #                      "pat4": Article("104", Prix('EUR', 20), "Italy")})
    # print(p1._CalculIndicesProduit())
    # print(p2._CalculIndicesProduit())
    # c1 = CategorieProduit("nourriture", {"riz": p1, "pat": p2})
    # print(c1._CalculIndicesCategories())
    # produit_categorie()
    # print(Nourriture._CalculIndicesCategories())
    print(bddinterfacecat())