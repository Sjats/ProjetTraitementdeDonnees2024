from forex_python.converter import CurrencyRates


class Prix:
    def __init__(self, devise, montant):
        self.devise = devise
        self.montant = montant
        if self.devise != "EUR":
            self.montant_euros = None
        else:
            self.montant_euros = self.montant

    def _ConversionEuros(self):
        self.montant_euros = self.__ObtientTauxChange() * self.montant
        return self.montant_euros

    def __ObtientTauxChange(self):
        # verification que devise in ISO 4217 list à faire
        return (CurrencyRates().get_rate(self.devise, 'EUR'))
