from forex_python.converter import CurrencyRates


class Prix:
    def __init__(self, devise, montant):
        """
        Initialisation de la classe Prix

        Parameters
        ----------
        devise : str
            nom de la devise
        montant : float
            quanité du montant
        """
        if not isinstance(devise, str):
            raise TypeError("devise doit être de type str")

        if not (isinstance(montant, float) or montant is None
                or isinstance(montant, int)):
            # print(montant, type(montant))
            raise TypeError("montant doit être de "
                            "type float ou None")

        self.devise = devise
        self.montant = montant
        if self.devise != "EUR" and self.montant is not None:
            self. _ConversionEuros()
        elif self.montant is None:
            self.montant_euros = None
        else:
            self.montant_euros = self.montant

    def _ConversionEuros(self, offline=True):
        """
        Fonction qui calcul le montant en euros

        Returns
        -------
        montant_euros : float
            quanité eqivalente du montant en euros
        """
        if offline:
            taux = {'USD': 0.9308, 'SGD': 0.6882, 'EUR': 1.0, 'CAD': 0.6813,
                    'SEK': 0.0858, 'PLN': 0.231, 'JPY': 0.0061, 'AUD': 0.6127,
                    'BRL': 0.1821, 'TRY': 0.0289, 'MXN': 0.0549, 'GBP': 1.1691,
                    'AED': 0.2534, 'INR': 0.0112, 'CNY': 0.1293, 'RUB': 0.0102}
            self.montant_euros = taux[self.devise] * self.montant
        else:

            self.montant_euros = self.__ObtientTauxChange() * self.montant
        return self.montant_euros

    def __str__(self) -> str:
        return (str(self.montant) + " " + self.devise)

    def __ObtientTauxChange(self):
        """
        Fonction qui met à jour le taux de change
        """
        # verification que devise in ISO 4217 list à faire
        return (CurrencyRates().get_rate(self.devise, 'EUR'))
