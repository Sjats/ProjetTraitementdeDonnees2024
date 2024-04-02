from article import Article
import requests
import os
import pickle
from prix import Prix
from ..fonctions import DomaineDevise


class SiteWeb:
    def __init__(self, nom, **fonctionalites_recherche):
        self._nom = nom

        self.__url_recherche = fonctionalites_recherche.get(
                                        "url_recherche", None)

        self.__pays = fonctionalites_recherche.get(
                                        "pays", None)

        self.__devant_prix = fonctionalites_recherche.get(
                                        "devant_prix", None)

        self.__devant_url_article = fonctionalites_recherche.get(
                                        "url_article", None)

        self.__apres_url_article = fonctionalites_recherche.get(
                                        "apres_url_article", None)

        self.__adresse_fichier = fonctionalites_recherche.get(
                                        "adresse_fichier", "donnees/")

        self.__requete_top_5 = fonctionalites_recherche.get(
                                        "requete_top_5", None)
        self.__requete_pays_ref = fonctionalites_recherche.get(
                                        "requete_pays_ref", None)

        self.__entete = {
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)'
                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61'
                ' Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;'
                'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-'
                'exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    def recherche_articles(self):
        """
        Fait la rêquete de recherche des 5 premieres pages de produits
        return: le code source html de ces n-premiers sites daans une variable
        interne
        """

        htmls = []
        payss = []

        for url_articles, pays in self.__urls_articles:
            resultat_recherche = requests.get(url_articles,
                                              headers=self.__entete)
            payss.append(pays)

            resultat_recherche.raise_for_status()

            self.htmls.append(resultat_recherche.text)

        self.__database = {}
        self.__database_html = {}

        for num, html in enumerate(htmls):
            auxi = len(str(num))
            id_article = (str(self._nom) + "-" +
                          "0"*(4 - auxi) + str(num))
            prix = self.recherche_prix(html)
            pays = payss[num]
            devise = DomaineDevise(pays)
            self.__database_html[id_article] = html
            self.__database[id_article] = Article(id_article,
                                                  Prix(prix, devise),
                                                  pays)

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

        self.__prix = self.html[PrixPosition: PrixPosition + auxi]

    def recherche_url_articles(self):

        if self.__requete_top_5 is not None:
            for pays in self.__pays:

                url = (self.__url_recherche[0] + pays + self.__url_recherche[1]
                       + self.__requete_top_5)

                html_recherche = requests.get(url, headers=self.entete).text

                pos_avant_link = 0
                for num_article in range(5):
                    pos_avant_link = (
                        html_recherche.find(
                            (self.__devant_url_article) +
                            len(self.__devant_url_article),
                            pos_avant_link + 1
                            ))

                    pos_apres_link = html_recherche.find(
                                    self.__apres_url_article) - 2

                    url = (self.__url_recherche[0] + pays +
                           html_recherche[pos_avant_link: pos_apres_link])

                    self.__urls_articles.append(url, pays)

        if self.__requete_pays_ref is not None:
            pass

    def WebScrapping(self):
        self.recherche_url_articles()
        self.recherche_articles()
        self.EnregistrementHtml()

    def EnregistrementHtml(self):

        if not os.path.exists(self.__adresse_fichier + "database.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_fichier = {}

        else:
            # Ouvre la BDD
            with open(self.__adresse_fichier + "database.pkl", "rb") as file:
                database_fichier = pickle.load(file)

        if not os.path.exists(self.__adresse_fichier + "database_html.pkl"):
            # Cree un dictionnaire vide si le fichier n'existe pas
            database_html_fichier = {}

        else:
            # On ouvre la BDD
            with open(self.__adresse_fichier +
                      "database_html.pkl", "rb") as file:

                database_html_fichier = pickle.load(file)

        database_fichier.update(self.__database)
        database_html_fichier.update(self.__database_html)

        with open(self.__adresse_fichier + "database.pkl", "wb") as file:
            pickle.dump(database_fichier, file)

        with open(self.__adresse_fichier + "database_html.pkl", "wb") as file:
            pickle.dump(database_html_fichier, file)
