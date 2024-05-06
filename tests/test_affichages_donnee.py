import pytest
import re
from classes.affichages_donnee import AffichageDonnees


import pytest
import re
from affichages_donnee import AffichageDonnees

# test pour le init
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({'indices_produits':['France', 'riz'],
        'indices_categorie_produit':{}},
          TypeError, "Les indices des produits doivent être renseignés"
                        " sous la forme d'un dictionnaire."),

        ({'indices_produits':{},
        'indices_categorie_produit':['France',
                                     'Articles de sport et de plein air'
        ]}, TypeError, "Les indices des catégories de produits"
                            " doivent être renseignés sous "
                            "la forme d'un dictionnaire."),

        ({'indices_produits':{'France': ['riz', [82, 75]]},
        'indices_categorie_produit':{}}, TypeError,
        "Les informations pour un pays dans produit"
        " doivent être sous forme de dictionnaire"),

        ({'indices_produits':{'France': {'riz': (82, 75)}},
        'indices_categorie_produit':{}}, TypeError,
        "Les valeures numériques des indices des "
        "produits doivent être renseignés sous forme de liste"),

        ({'indices_produits':{},
        'indices_categorie_produit':{'France': [
            'Articles de sport et de plein air', [60, 65]
        ]}}, TypeError,
        "Les informations pour un pays dans catégorie"
        " doivent être sous forme de dictionnaire"),

        ({'indices_produits':{},
        'indices_categorie_produit':{'France': {
            'Articles de sport et de plein air': (60, 65)
        }}}, TypeError,
        "Les valeures numériques des indices des "
        "catégories doivent être renseignés sous forme de liste"),
    ]
)

def test_init_echec_affichage_donnees(kwargs, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        AffichageDonnees(**kwargs)


# test pour plot_histogramme
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({'sur_quoi': 3, 'execute_apres': None}, TypeError, "sur_quoi doit"
        " être une instance de bool.")
    ]
)
def test_plot_histo_bool_echec(kwargs, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        interface = AffichageDonnees({}, {})
        interface.plot_histogramme(**kwargs)

@pytest.mark.parametrize(
    'kwargs, resultat_attendu',
    [
        ({'sur_quoi' :True, 'indices_produits':{
        'France': {
            'riz': [82, 75],
            'banane': [60, 65]
        }}, 'indices_categorie_produit':{
        'France': {
            'High-Tech': [82, 75],
            'Articles de sport et de plein air': [60, 65]
        }}}, 'indices_produits'),

        ({'sur_qoui': False, 'indices_produits':{
        'France': {
            'riz': [82, 75],
            'banane': [60, 65]
        }}, 'indices_categorie_produit':{
        'France': {
            'High-Tech': [82, 75],
            'Articles de sport et de plein air': [60, 65]
        }}}, 'indices_categorie_produit')
    ]
)

def test_mon_dict_histo_assignment(kwargs, resultat_attendu):
    interface = AffichageDonnees(kwargs['indices_produits'], kwargs['indices_categorie_produit'])
    interface.plot_histogramme(kwargs['sur_quoi'], execute_apres=lambda: None)

    mon_dict = interface.mon_dict

    if resultat_attendu == 'indices_produits':
        assert mon_dict == kwargs['indices_produits']
    else:
        assert mon_dict == kwargs['indices_categorie_produit']

#test pour afficher carte

@pytest.mark.parametrize(
    'kwargs, resultat_attendu',
    [
        ({'sur_quoi' :True, 'indices_produits':{
        'France': {
            'riz': [82, 75],
            'banane': [60, 65]
        }}, 'indices_categorie_produit':{
        'France': {
            'High-Tech': [82, 75],
            'Articles de sport et de plein air': [60, 65]
        }}}, 'indices_produits'),

        ({'sur_qoui': False, 'indices_produits':{
        'France': {
            'riz': [82, 75],
            'banane': [60, 65]
        }}, 'indices_categorie_produit':{
        'France': {
            'High-Tech': [82, 75],
            'Articles de sport et de plein air': [60, 65]
        }}}, 'indices_categorie_produit')
    ]
)

def test_mon_dict_carte_assignment(kwargs, resultat_attendu):
    interface = AffichageDonnees(kwargs['indices_produits'], kwargs['indices_categorie_produit'])
    interface.AfficherCarte(kwargs['sur_quoi'])

    mon_dict = interface.mon_dict

    if resultat_attendu == 'indices_produits':
        assert mon_dict == kwargs['indices_produits']
    else:
        assert mon_dict == kwargs['indices_categorie_produit']
