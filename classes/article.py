class Article:

    def __init__(self, id_article, prix, pays):
        self._id_article = id_article
        self._prix = prix
        self._pays = pays

    def __str__(self):
        text = ("Id Article : {}\nPrix : {}\nPays : {}"
                .format(self._id_article, self._prix, self._pays))
        return (text)
