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


client = ScrapingBeeClient(api_key="8GKVX0VKUZWJBY2GS4KKFEEZCVCS"
                                   "UASEVRYQKMZHVHZZ9106YSXVRRW09XS6"
                                   "4ZJF7HP6REVKQNM7R4EH")
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

        self._entete = {"User-Agent": "Mozilla/5.0 (Linux; "
                        "Android 11; SAMSUNG SM-G973U) Apple"
                        "WebKit/537.36 (KHTML, like Gecko) Sa"
                        "msungBrowser/14.2 Chrome/87.0.4280.14"
                        "1 Mobile Safari/537.36",
                        'Accept-Encoding': 'identity',
                        "Accept": "text/html,application/xhtml+"
                        "xml,application/xml;q=0.9,*/*;q=0.8",
                        "DNT": "1", "Connection": "close",
                        "Upgrade-Insecure-Requests": "1"}

    def recherche_articles(self, requete):
        if requete is not None:
            self.requete = requete
        self.urls_articles = []
        self.__database = {}

        for requete in self.requete:
            for domaine in self._pays_domaines:
                print(domaine, requete)
                if self._pays is None:

                    langue = domaine_a_langue.DomaineLangue(domaine)
                    pays = domaine_a_pays.DomainePays(domaine)
                    devise = DomaineDevise(domaine)
                else:
                    langue = domaine_a_langue.DomaineLangue(self._pays)
                    pays = domaine_a_pays.DomainePays(self._pays)
                    devise = DomaineDevise(self._pays)

                translator = Translator(langue)
                requte_trad = translator.translate(requete)

                url = (self._url_recherche[0] + domaine +
                       self._url_recherche[1] + requte_trad)

                if self._scraping_type == "Bee":
                    html_recherche = client.get(url).content

                if self._scraping_type == "Normal":
                    html_recherche = requests.get(url, headers=self._entete)
                    html_recherche = html_recherche.text
                soup = BeautifulSoup(html_recherche, "html.parser")

                prix_entier = soup.find_all(self._devant_prix_entier[0],
                                            self._devant_prix_entier[1])
                print(prix_entier)
                if self._devant_prix_decimal is not None:
                    prix_decimal = soup.find_all(self._devant_prix_decimal[0],
                                                 self._devant_prix_decimal[1])
                index = 0

                for i in range(min(5, max(len(prix_entier)-1, 0))):

                    str_prix_entier = str(prix_entier[i].get_text(strip=True))
                    str_prix_entier = str_prix_entier.replace(',', '', 1)
                    str_prix_entier = str_prix_entier.replace('.', '', 1)

                    if str_prix_entier.isdigit():

                        if prix_decimal is None or len(prix_decimal) < 2:
                            montant = float(str_prix_entier)

                        else:
                            str_prix_decimal = prix_decimal[i].get_text(
                                strip=True)

                            montant = (float(str_prix_entier) +
                                       float(str_prix_decimal) * 0.01)
                    else:
                        montant = None
                    id_article = pays + "/" + requete + "/" + str(index)
                    article = Article(id_article,
                                      Prix(devise, montant),
                                      pays)

                    self.__database[id_article] = article
                    index += 1

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

    def EnregistrementHtml(self, adresse="donnees/"):
        """
        Fonction qui enregistre les articles dans l'endroit indiqué
        Parameters
        ----------
        adresse : str
            endroit dans lequel on enregistre le dictionnaire
        """

        if not (isinstance(adresse, str) or adresse is None):
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
