from django.test import TestCase

from calculations.helpers.conteudo_segurado import calculate_total
from calculations.helpers.importancia_segurada import calculate_importancia_segurada
from calculations.helpers.resp_civil import calculate_cobertura_resp_civil
from calculations.helpers.danos_eletricos import calculate_danos_eletricos
from calculations.helpers.cobertura_vendaval import calculate_cobertura_vendaval
from calculations.helpers.assistencia import calculate_value_assistencia

from calculations.helpers.premio_liquido import PremioLiquido

class ContractTestCase(TestCase):
    def test_importancia_segurada_is_correct(self):
        result = calculate_importancia_segurada(aluguel=1000)
        self.assertEqual(result, 120000)

    def test_conteudo_segurado_is_correct(self):
        result = calculate_total(importancia_segurada=120000)
        self.assertEqual(result, 12000)

    def test_resp_civil_is_correct(self):
        result = calculate_cobertura_resp_civil()
        self.assertEqual(result, 15000)

    def test_danos_eletricos_is_correct(self):
        result = calculate_danos_eletricos()
        self.assertEqual(result, 6000)

    def test_cobertura_vendaval_is_correct(self):
        result = calculate_cobertura_vendaval()
        self.assertEqual(result, 5000)

    def test_value_assistencia_is_correct(self):
        result = calculate_value_assistencia()
        self.assertEqual(result, 65)

    def test_premio_liquido_without_optional_coverage(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.calculate()
        self.assertEqual(result, 216)

    def test_premio_liquido_with_seguro_conteudo_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_seguro_conteudo() \
            .calculate()
        self.assertEqual(result, 237.6)

    def test_premio_liquido_with_resp_civil_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_resp_civil() \
            .calculate()
        self.assertEqual(result, 396)
