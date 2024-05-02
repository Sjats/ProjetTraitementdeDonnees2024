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

    def _ConversionEuros(self):
        """
        Fonction qui calcul le montant en euros

        Returns
        -------
        montant_euros : float
            quanité eqivalente du montant en euros
        """
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
