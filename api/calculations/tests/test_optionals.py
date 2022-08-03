from django.test import TestCase

from calculations.helpers.conteudo_segurado import calculate_total
from calculations.helpers.resp_civil import calculate_cobertura_resp_civil
from calculations.helpers.danos_eletricos import calculate_cobertura_danos_eletricos
from calculations.helpers.cobertura_vendaval import calculate_cobertura_vendaval
from calculations.helpers.assistencia import value_assistencia

class OptionalsTestCase(TestCase):
    def test_conteudo_segurado_is_correct(self):
        result = calculate_total(importancia_segurada=120000)
        self.assertEqual(result, 12000)

    def test_resp_civil_is_correct(self):
        result = calculate_cobertura_resp_civil()
        self.assertEqual(result, 15000)

    def test_danos_eletricos_is_correct(self):
        result = calculate_cobertura_danos_eletricos()
        self.assertEqual(result, 6000)

    def test_cobertura_vendaval_is_correct(self):
        result = calculate_cobertura_vendaval()
        self.assertEqual(result, 5000)

    def test_value_assistencia_is_correct(self):
        result = value_assistencia
        self.assertEqual(result, 65)
