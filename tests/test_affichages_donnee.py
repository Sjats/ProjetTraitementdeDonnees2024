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
