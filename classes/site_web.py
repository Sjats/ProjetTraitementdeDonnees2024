from scrapingbee import ScrapingBeeClient
from .article import Article
import requests
import os
import pickle
from .prix import Prix
from fonctions.domaine_a_devise import DomaineDevise
from fonctions import domaine_a_pays
from donnees import renseigement_sites_web
from fonctions import domaine_a_langue
from translate import Translator
from bs4 import BeautifulSoup


client = ScrapingBeeClient(api_key="WJ6LI7YZEB7N5JUA4YB4E2EUL8EMU2OF1"
                           "LFWTN7UYGJP683QO3CWIJAAZE7SO2W3WN5YKE32XDJ9E08U")
# cle api web scraping


class SiteWeb:
    def __init__(self, nom):
        """
        Initialisation de la classe SiteWeb

        Parameters
        ----------
        nom : str
            nom du site web dont on veut recuperer des donnees,
            Attention il doit figurer dans la lise de renseignements
        """

        if not isinstance(nom, str):
            raise TypeError("nom est de type str")

        if nom not in renseigement_sites_web.configurations_sites.keys():
            val_nom = renseigement_sites_web.configurations_sites.keys()

            raise ValueError("nom non valide, les noms valides"
                             " sont " + str(val_nom))
        self._nom = nom

        # Charge les attributs du site demandé sous forme de dictionnaire
        config_dict = renseigement_sites_web.configurations_sites.get(nom, {})

        # Initialisation des Attributs
        for key, value in config_dict.items():
            setattr(self, key, value)

        self.adresse_fichier = "donnees/"

        self._entete = {"User-Agent": "Mozilla/5.0 (Wind"
                        "ows NT 10.0; Win64; x64; rv:66.0) Gecko/2010010"
                        "1 Firefox/66.0",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "text/html,application/xhtml+"
                        "xml,application/xml;q=0.9,*/*;q=0.8",
                        "DNT": "1", "Connection": "close",
                        "Upgrade-Insecure-Requests": "1"}

    def recherche_articles(self):

        self.urls_articles = []
        self.__database = {}

        for requete in self.requete:
            for domaine in self._pays_domaines:

                langue = domaine_a_langue.DomaineLangue(domaine)
                pays = domaine_a_pays.DomainePays(domaine)
                devise = DomaineDevise(domaine)

                print(requete, langue)

                translator = Translator(langue)
                requte_trad = translator.translate(requete)

                url = (self._url_recherche[0] + domaine +
                       self._url_recherche[1] + requte_trad)

                if self._scraping_type == "Bee":
                    html_recherche = client.get(url).content

                if self.scraping_type == "Normal":
                    html_recherche = requests.get(url, headers=self.entete)
                    html_recherche = html_recherche.text

                soup = BeautifulSoup(html_recherche, "html.parser")

                prix_entier = soup.find_all(self._devant_prix_entier[0],
                                            self._devant_prix_entier[1])
                prix_decimal = soup.find_all(self._devant_prix_decimal[0],
                                             self._devant_prix_decimal[1])

                for i in range(min(5, max(len(prix_entier)-1, 0))):

                    str_prix_entier = str(prix_entier[i].text.strip())
                    str_prix_entier = str_prix_entier.replace(',', '')

                    if str_prix_entier.isdigit():

                        if prix_decimal is None or len(prix_decimal) < 2:
                            montant = str_prix_entier

                        else:
                            str_prix_decimal = prix_decimal[i].text.strip()
                            montant = (float(str_prix_entier) +
                                       float(str_prix_decimal) * 0.01)
                    else:
                        montant = None

                    id_article = pays + "/" + requete + "/" + str(i)
                    article = Article(id_article,
                                      Prix(devise, montant),
                                      pays)

                    self.__database[id_article] = article

            self.EnregistrementHtml()  # A treure
            self.__database = {}  # A treure

    def WebScrapping(self, requetes=None):
        """
        Fonction qui réalise le web scraping d'un site web et enregistre
        les articles trouvés sous forme de dictionnaire. Veuillez modifier
        le parametre "adresse_fichier" pour indiquer où vous voulez sauvegarder
        votre recherche
        Parameters
        ----------
        requetes : list[str] or None
            liste des requetes qui seront lancés sur le site web
        """
        if not (isinstance(requetes, list) or requetes is None):
            raise TypeError("requetes est de type list")

        if requetes is not None:
            for art in requetes:
                if not isinstance(art, str):
                    raise TypeError("les elements de requetes sont "
                                    "de type str")
            self.requete = requetes

        self.recherche_articles()
        self.EnregistrementHtml()

    def EnregistrementHtml(self, adresse=None):
        """
        Fonction qui enregistre les articles dans l'endroit indiqué
        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre le dictionnaire
        """

        if not (isinstance(adresse, list) or adresse is None):
            raise TypeError("adresse est de type str")

        if not os.path.exists(self.adresse_fichier):
            raise ValueError("l'adresse fournie n'existe pas")

        if adresse is not None:
            self.adresse_fichier = adresse

        if not os.path.exists(self.adresse_fichier + "database.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = {}

        else:
            # Ouvre la BDD
            with open(self.adresse_fichier + "database.pkl", "rb") as file:
                database_fichier = pickle.load(file)

        database_fichier.update(self.__database)

        with open(self.adresse_fichier + "database.pkl", "wb") as file:
            pickle.dump(database_fichier, file)
