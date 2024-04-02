from article import Article
import requests


class SiteWeb:
    def __init__(self, nom, fonctionalites_recherche):
        self._nom = nom
        self.__url_recherche = fonctionalites_recherche["url_recherche"]
        self.__devant_prix = fonctionalites_recherche["devant_prix"]
        self.__url_choix_article = fonctionalites_recherche["choix_article"]
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

    def recherche_code_html_page_article(self):
        """
        Fait la rêquete de recherche des n-premieres pages de produits
        return: le code source html de ces n-premiers sites daans une variable
        interne
        """

        self.__html = []

        for url_articles in self.__urls_articles:
            resultat_recherche = requests.get(url_articles,
                                              headers=self.__entete)

            resultat_recherche.raise_for_status()

            self.__html.append(resultat_recherche.text)

    def recherche_prix(self):

        PrixPosition = (self.html.find(self.__devant_prix)
                        + len(self.__devant_prix))
        auxi = 0
        for position in range(0, 15):
            if (self.html[PrixPosition + position].isdigit()
                    or self.html[PrixPosition + position] in [".", " ", ","]):
                auxi += 1
            else:
                break

        self.__prix = self.html[PrixPosition: PrixPosition + auxi]
        
