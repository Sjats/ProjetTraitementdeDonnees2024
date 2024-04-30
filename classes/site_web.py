from scrapingbee import ScrapingBeeClient
from .article import Article
# import requests
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

        self._nom = nom

        # Charge les attributs du site demandé sous forme de dictionnaire
        config_dict = renseigement_sites_web.configurations_sites.get(nom, {})

        # Initialisation des Attributs
        for key, value in config_dict.items():
            setattr(self, key, value)

        self.adresse_fichier = "donnees/"

    def recherche_prix(self, html):

        PrixPosition = (html.find(self.__devant_prix)
                        + len(self.__devant_prix))
        auxi = 0
        for position in range(0, 15):
            if (self.html[PrixPosition + position].isdigit()
                    or self.html[PrixPosition + position] in [".", " ", ","]):
                auxi += 1
            else:
                break

        return self.html[PrixPosition: PrixPosition + auxi]

    def recherche_articles(self):
        self.urls_articles = []
        self.__database = {}

        if hasattr(self, 'requete_top_5'):

            for requete in self.requete_top_5:
                for domaine in self._pays_domaines:

                    langue = domaine_a_langue.DomaineLangue(domaine)
                    pays = domaine_a_pays.DomainePays(domaine)
                    devise = DomaineDevise(domaine)

                    print(requete, langue)

                    translator = Translator(langue)
                    requte_trad = translator.translate(requete)

                    url = (self._url_recherche[0] + domaine +
                           self._url_recherche[1] + requte_trad)

                    html_recherche = client.get(url).content

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

                self.EnregistrementHtml()
                self.__database = {}

    def WebScrapping(self):
        self.recherche_articles()

    def EnregistrementHtml(self):

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
