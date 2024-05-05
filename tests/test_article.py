import pytest
import re
from classes.article import Article
from classes.prix import Prix


@pytest.mark.parametrize(
    'article', 'erreur', 'message_erreur',
    [
        (Article({'Pays': 'France', 'Nom': 'Coffee+maker', 'Numéro': 0},
                 Prix(30, 'EUR'),
                 'France'),
         TypeError, "id_article doit être de type str"),

        (Article('France/Coffee+maker/0', 30, 'France'),
         TypeError, "prix doit être de type Prix"),

        (Article('France/Coffee+maker/0', Prix('EUR', 30), ['France']),
         TypeError, "pays doit être de type str"),
     ]
)
def test_produit_init_echec(article, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        article
