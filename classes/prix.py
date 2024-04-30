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
        # Devises = []
        if not isinstance(devise, str):
            raise TypeError("devise doit être de type str")

        # if devise not in Devises:
        #    raise ValueError("La devise fournie n'est "
        #                     "pas homologuée dans ISO 4217")

        if not (isinstance(montant, float) or montant is None
                or isinstance(montant, int)):
            raise TypeError("devise doit être de "
                            "type float ou None")

        self.devise = devise
        self.montant = montant
        if self.devise != "EUR":
            self. _ConversionEuros()
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

    def __ObtientTauxChange(self):
        """
        Fonction qui met à jour le taux de change
        """
        # verification que devise in ISO 4217 list à faire
        return (CurrencyRates().get_rate(self.devise, 'EUR'))
