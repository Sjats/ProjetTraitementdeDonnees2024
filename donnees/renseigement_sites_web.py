requete_amazon = [
#    "Coffee+maker",
#    "AA+alkaline+battery+pack",
#    "Non-slip+yoga+mat",
#    "Bluetooth+wireless+earbuds",
#    "LED+desk+lamp",
#    "Portable+external+battery",
#    "Portable+Bluetooth+speaker",
#    "Professional+hair+clippers",
#    "Non-stick cookware set",
#    "Insulated thermos",
#    "USB charging hub",
#    "Gardening starter kit",
#    "Folding storage box",
#    "Cordless stick vacuum",
#    "Essential oil diffuser",
#    "First aid kit",
#    "Fitness smartwatch",
#    "Waterproof backpack",
#    "Car phone mount",
#    "Digital bathroom scale",
#   "Retractable ballpoint pen",
#    "USB-C charging cable",
#    "Steam iron",
#    "Electric toothbrush",
#    "Paper coffee filters",
#    "Professional kitchen knife",
#    "Modular storage shelf",
    "Polarized sunglasses",
    "Shiatsu massage cushion",
    "Biodegradable toilet paper",
    "Waterproof sports bag",
    "LED headlamp",
    "Compact and sturdy umbrella",
    "Hand sanitizer gel",
    "Mosquito repellent bracelet",
    "High-speed HDMI cable",
    "Contactless forehead thermometer",
    "Gardening gloves",
    "Lightning charging cable",
    "Insulated travel mug",
    "Combination padlock",
    "Ergonomic mouse pad",
    "Reusable water bottle",
    "Cat 7 Ethernet cable",
    "Portable solar charger",
    "Rechargeable LED flashlight"
]
requete_pays_ref = ["requete1", "requete2"]

configurations_sites = {
    "amazon": {
        "_url_recherche": ["https://www.amazon", "/s?k="],
        "_pays_domaines": [
                            ".sg",
                            ".ae",
                            ".com.mx",
                            ".com.br",
                            ".com.tr",
                            ".co.jp",
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
                            ".cn",
                            ".in",
                            ".com.au",
                          ],

        "_devant_prix_entier":  ['span', {'class': "a-price-whole"}],

        "_devant_prix_decimal": ['span', {'class': "a-price-fraction"}],

        "requete": requete_amazon,
        "_scraping_type": "Bee"

    },
    "site2": {
        "url_recherche": ["https://www.amazon", "/s?k="],
        "pays": "France",
        "devant_prix": "EUR",
        "devant_url_article": "a",
        "apres_url_article": "",
        "requete_top_5": "",
        "requete_pays_ref": "",
        "_scraping_type": "Normal"

    }
}
