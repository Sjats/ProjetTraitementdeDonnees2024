requete_top_5 = ["requete1", "requete2"]
requete_pays_ref = ["requete1", "requete2"]

configurations_sites = {
    "amazon": {
        "url_recherche": ["https://www.amazon", "/s?k="],
        "pays_domaines": [
                            ".com",
                            ".ca",
                            ".co.uk",
                            ".de",
                            ".fr",
                            ".es",
                            ".it",
                            ".nl",
                            ".se",
                            ".pl",
                            ".co.jp",
                            ".cn",
                            ".in",
                            ".com.au",
                            ".sg",
                            ".ae",
                            ".sa",
                            ".com.mx",
                            ".com.br",
                            ".com.tr"
                          ],

        "devant_prix":  "<span class=\"a-price aok-align-center\" data-a-size="
                        "\"xl\" data-a-color=\"base\"><span "
                        "class=\"a-offscreen\">",

        "devant_url_article": "<a class=\"a-link-normal s-no-outline\" "
                              "href=\"",
        "apres_url_article": "<div class=\"a-section aok-relative "
                             "s-image-square-aspect\"><img "
                             "class=\"s-image\" src=",
        "requete_top_5": requete_top_5,
        "requete_pays_ref": requete_pays_ref,

    },
    "site2": {
        "url_recherche": ["https://www.amazon", "/s?k="],
        "pays": "France",
        "devant_prix": "EUR",
        "devant_url_article": "a",
        "apres_url_article": "",
        "requete_top_5": "",
        "requete_pays_ref": "",

    }
}
