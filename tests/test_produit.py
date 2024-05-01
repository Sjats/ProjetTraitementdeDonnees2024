from classes.produit import Produit
from classes.article import Article
from classes.prix import Prix
import pytest
import re

@pytest.mark.parametrize(
    'produit', 'erreur', 'message_erreur',
    [
        (Produit(['seche_cheveux'], {'seche_cheveux1': Article(id_article,
                                                               Prix(30, 'EUR'),
                                                               'France')}),
         TypeError, "Le nom doit être une instance de str."),

        (Produit('seche_cheveux', Article(id_article,
                                            Prix(30, 'EUR'),
                                            'France')),
         TypeError, "Les articles doivent être une instance de dictionnaire."),

        (Produit('seche_cheveux', { 1 : Article(id_article,
                                                Prix(30, 'EUR'),
                                                'France')}),
         TypeError, (
             "Les clés du dictionnaire d'articles doivent être une "
             "instance de str."
         )),
        
        (Produit('seche_cheveux', { 'seche_cheveux1' : Prix(30, 'EUR')}),
         TypeError, (
             "Les valeurs du dictionnaire d'articles doivent être une "
             "instance d'Article"
         )),
        
     ]
)
def test_produit_init_echec(produit, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        produit