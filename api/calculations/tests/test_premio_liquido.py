from django.test import TestCase

from calculations.helpers.premio_liquido import PremioLiquido

class PremioLiquidoTestCase(TestCase):
    def test_without_optional_coverage(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.calculate()
        self.assertEqual(result, 216)

    def test_with_seguro_conteudo_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_seguro_conteudo() \
            .calculate()
        self.assertEqual(result, 237.6)

    def test_with_resp_civil_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_resp_civil() \
            .calculate()
        self.assertEqual(result, 396)

    def test_with_danos_eletricos_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_danos_eletricos() \
            .calculate()
        self.assertEqual(result, 295)

    def test_with_cobertura_vendaval_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_cobertura_vendaval() \
            .calculate()
        self.assertEqual(result, 303)

    def test_with_assistencia_optional(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_assistencia() \
            .calculate()
        self.assertEqual(result, 281)

    def test_with_all_optional_coverage(self):
        premio_liquido = PremioLiquido(aluguel=1000)
        result = premio_liquido.with_seguro_conteudo() \
            .with_resp_civil() \
            .with_danos_eletricos() \
            .with_cobertura_vendaval() \
            .with_assistencia() \
            .calculate()
        self.assertEqual(result, 648.60)
