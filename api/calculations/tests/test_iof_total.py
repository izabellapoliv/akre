from django.test import TestCase

from calculations.helpers.premio_liquido import PremioLiquido
from calculations.helpers.iof_total import calculate_iof_total

class IOFTotalTestCase(TestCase):
    def test_without_optional_coverage(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 15.94)

    def test_with_seguro_conteudo_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_seguro_conteudo() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 17.53)

    def test_with_resp_civil_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_resp_civil() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 29.22)

    def test_with_danos_eletricos_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_danos_eletricos() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 21.77)

    def test_with_cobertura_vendaval_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_cobertura_vendaval() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 22.36)

    def test_with_assistencia_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_assistencia() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 20.74)

    def test_with_all_optional_coverage(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_seguro_conteudo() \
            .with_resp_civil() \
            .with_danos_eletricos() \
            .with_cobertura_vendaval() \
            .with_assistencia() \
            .calculate()
        result = calculate_iof_total(premio_liquido)
        self.assertEqual(result, 47.87)
