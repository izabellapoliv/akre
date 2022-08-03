from calculations.helpers.default import default_tax
from calculations.helpers.conteudo_segurado import calculate_premio_liquido_conteudo
from calculations.helpers.importancia_segurada import calculate_importancia_segurada
from calculations.helpers.resp_civil import value_resp_civil
from calculations.helpers.danos_eletricos import value_danos_eletricos
from calculations.helpers.cobertura_vendaval import value_vendaval
from calculations.helpers.assistencia import value_assistencia

class PremioLiquido():
    __optionals = 0
    __aluguel = 0

    def __init__(self, aluguel):
        self.__aluguel = aluguel

    def calculate(self):
        importancia_segurada = calculate_importancia_segurada(self.__aluguel)
        return ((default_tax / 100) * importancia_segurada) + self.__optionals

    def with_assistencia(self):
        self.__optionals += value_assistencia
        return self

    def with_cobertura_vendaval(self):
        self.__optionals += value_vendaval
        return self

    def with_resp_civil(self):
        self.__optionals += value_resp_civil
        return self

    def with_danos_eletricos(self):
        self.__optionals += value_danos_eletricos
        return self

    def with_seguro_conteudo(self):
        importancia_segurada = calculate_importancia_segurada(self.__aluguel)
        self.__optionals += calculate_premio_liquido_conteudo(importancia_segurada)
        return self
