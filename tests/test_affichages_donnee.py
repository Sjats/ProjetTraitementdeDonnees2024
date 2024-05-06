import pytest
import re
from classes.affichages_donnee import AffichageDonnees


@pytest.mark.parametrize(
    'indices_produits', "indices_categories", 'erreur', 'message_erreur',
    [
        ([['France', 0.65, 1.0], ['Italy', 0.83, 1.28]],
         {'France': [0.65, 1.0], 'Italy': [0.83, 1.28]},
         TypeError, (
             "les indices des produits doivent"
             " être renseignés sous la forme "
             "d'un dictionnaire."
         )),

        ({'France': [0.65, 1.0], 'Italy': [0.83, 1.28]},
         [['France', 0.65, 1.0], ['Italy', 0.83, 1.28]],
         TypeError, (
             "Les indices des catégories de produits"
             " doivent être renseignés sous "
             "la forme d'un dictionnaire."
         ))
     ]
)
def test_produit_init_echec(indices_produits,
                            indices_categories,
                            erreur,
                            message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        AffichageDonnees(indices_produits, indices_categories,)


@pytest.mark.parametrize(
    'indices_produits', "indices_categories",
    [
        ({['France', 0.65, 1.0], ['Italy', 0.83, 1.28]},
         {'France': [0.65, 1.0], 'Italy': [0.83, 1.28]},
         TypeError, (
             "les indices des produits doivent"
             " être renseignés sous la forme "
             "d'un dictionnaire."
         )),

        ({'France': [0.65, 1.0], 'Italy': [0.83, 1.28]},
         {['France', 0.65, 1.0], ['Italy', 0.83, 1.28]},
         TypeError, (
             "Les indices des catégories de produits"
             " doivent être renseignés sous "
             "la forme d'un dictionnaire."
         ))
     ]
)
def test_produit_init_succes(indices_produits, indices_categories,):

    AffichageDonnees(indices_produits, indices_categories,)

# test pour plot_histogramme
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({'sur_quoi': 3, 'execute_apres': None}, TypeError, "sur_quoi doit être une instance de bool.")
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

def test_indices_assignment(kwargs, resultat_attendu):
    interface = AffichageDonnees(kwargs['indices_produits'], kwargs['indices_categorie_produit'])
    interface.plot_histogramme(kwargs['sur_quoi'], execute_apres=lambda: None)

    mon_dict = interface.mon_dict

    if resultat_attendu == 'indices_produits':
        assert mon_dict == kwargs['indices_produits']
    else:
        assert mon_dict == kwargs['indices_categorie_produit']
