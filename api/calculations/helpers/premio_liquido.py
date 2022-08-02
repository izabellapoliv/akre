from calculations.helpers.default import default_tax
from calculations.helpers.importancia_segurada import calculate_importancia_segurada
from calculations.helpers.resp_civil import calculate_resp_civil
from calculations.helpers.danos_eletricos import calculate_danos_eletricos
from calculations.helpers.cobertura_vendaval import calculate_cobertura_vendaval
from calculations.helpers.assistencia import calculate_value_assistencia

class PremioLiquido():
    __optionals = 0

    def calculate(self, aluguel):
        importancia_segurada = calculate_importancia_segurada(aluguel)
        return ((default_tax / 100) * importancia_segurada) + self.__optionals

    def with_assistencia(self):
        self.__optionals += calculate_value_assistencia()

    def with_cobertura_vendaval(self):
        self.__optionals += calculate_cobertura_vendaval()

    def with_resp_civil(self):
        self.__optionals += calculate_resp_civil()

    def with_danos_eletricos(self):
        self.__optionals += calculate_danos_eletricos()
