import pickle

requete_amazon = [
    "Coffee+maker",
    "AA+alkaline+battery+pack",
    "Non-slip+yoga+mat",
    "Bluetooth+wireless+earbuds",
    "LED+desk+lamp",
    "Portable+external+battery",
    "Portable+Bluetooth+speaker",
    "Professional+hair+clippers",
    "Non-stick cookware set",
    "Insulated thermos",
    "USB charging hub",
    "Gardening starter kit",
    "Folding storage box",
    "Cordless stick vacuum",
    "Essential oil diffuser",
    "First aid kit",
    "Fitness smartwatch",
    "Waterproof backpack",
    "Car phone mount",
    "Digital bathroom scale",
    "Retractable ballpoint pen",
    "USB-C charging cable",
    "Steam iron",
    "Electric toothbrush",
    "Paper coffee filters",
    "Professional kitchen knife",
    "Modular storage shelf",
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

requete_iherb = [
    "Organic+Extra+Virgin+Olive+Oil",
    "Organic Apple Cider Vinegar",
    "Raw Honey",
    "Quinoa",
    "Almond Butter",
    "Chia Seeds",
    "Coconut Oil",
    "Green Tea",
    "Dark Chocolate",
    "Mixed Nuts",
    "Protein Powder",
    "Multivitamin",
    "Omega-3 Fish Oil",
    "Turmeric Supplement",
    "Vitamin D3",
    "Calcium Supplement",
    "Magnesium Citrate",
    "Collagen Powder",
    "Biotin Supplement",
    "Whey Protein",
    "Plant-Based Protein",
    "B Complex Vitamin",
    "Iron Supplement",
    "Fiber Supplement",
    "Antioxidant Blend"
]

requete_supermarche = [
    "bread",
    "milk",
    "eggs",
    "cheese",
    "yogurt",
    "chicken",
    "beef",
    "pork",
    "fish",
    "shrimp",
    "rice",
    "pasta",
    "potatoes",
    "lettuce",
    "tomatoes",
    "carrots",
    "onions",
    "apples",
    "bananas",
    "oranges",
    "strawberries",
    "blueberries",
    "cookies",
    "chips",
    "ice cream"
]

configurations_sites = {
    "amazon": {
        "_url_recherche": ["https://www.amazon.", "/s?k="],
        "_pays_domaines": [
                            "in",
                            "com",
                            "co.jp",
                            "sg",
                            "ae",
                            "com.mx",
                            "com.br",
                            "com.tr",
                            "ca",
                            "co.uk",
                            "de",
                            "fr",
                            "es",
                            "it",
                            "nl",
                            "se",
                            "pl",
                            "cn",
                            "com.au",
                          ],

        "_devant_prix_entier":  ['span', {'class': "a-price-whole"}],

        "_devant_prix_decimal": ['span', {'class': "a-price-fraction"}],

        "requete": requete_amazon,
        "_scraping_type": "Bee",
        "_pays": None,

    },
    "iherb": {
        "_url_recherche": ["https://", ".iherb.com/search?kw="],
        "_pays_domaines": ['www',
                           'uk',
                           'ca',
                           'au',
                           'cn',
                           'jp',
                           'de',
                           'fr',
                           'it',
                           'es',
                           'nl',
                           'se',
                           'no',
                           'br',
                           'mx',
                           'sg',
                           'hk'],

        "_devant_prix_entier":  ['span', {'class': "price "}],

        "_devant_prix_decimal": None,

        "requete": requete_iherb,
        "_scraping_type": "Normal",
        "_pays": None,
    },
    "supermarches0": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "TilePrice_tile_price"
                                          "_current__Jy4AT",
                                          "data-testid": "Tile price current",
                                          "data-qa": "tile_product_price"
                                          }],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches1": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches2": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches3": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches4": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches5": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches6": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches7": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    }, "supermarches8": {
        "_url_recherche": ["https://", ""],
        "_pays_domaines": ['www.freshdirect.com/search?search='],
        "_devant_prix_entier":  ['span', {'class': "price "}],
        "_devant_prix_decimal": None,
        "_pays": "ww",
        "requete": requete_supermarche,
        "_scraping_type": "Normal"
    },
}
requetes = {"varié": requete_amazon,
            "alimentaire": requete_supermarche,
            "vitamines": requete_iherb}

with open("donnees/rsw_data.pkl", "wb") as file:
    pickle.dump(configurations_sites, file)
with open("donnees/rr_data.pkl", "wb") as file:
    pickle.dump(requetes, file)
