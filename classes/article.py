from prix import Prix


class Article:
    def __init__(self, id_article, prix, pays):
        """
        Initialisation de la classe Article
        Parameters
        ----------
        id_article : str
            Identifiant unique de l'article
        prix : Prix
            Prix de l'article
        pays : str
            Pays d'achat de l'article
        """

        if not isinstance(id_article, str):
            raise TypeError("id_article doit être de type str")

        if not isinstance(prix, Prix):
            raise TypeError("prix doit être de type Prix")

        if not isinstance(pays, str):
            raise TypeError("pays doit être de type str")

        self._id_article = id_article
        self._prix = prix
        self._pays = pays

    def __str__(self):
        text = ("Id Article : {}\nPrix : {}\nPays : {}"
                .format(self._id_article, self._prix, self._pays))
        return (text)
