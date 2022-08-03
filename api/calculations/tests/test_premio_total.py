from django.test import TestCase

from calculations.helpers.premio_liquido import PremioLiquido
from calculations.helpers.iof_total import calculate_iof_total
from calculations.helpers.premio_total import calculate_premio_total

class PremioTotalTestCase(TestCase):
    def test_without_optional_coverage(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 231.94)

    def test_with_seguro_conteudo_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_seguro_conteudo() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 255.13)

    def test_with_resp_civil_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_resp_civil() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 425.22)

    def test_with_danos_eletricos_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_danos_eletricos() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 316.77)

    def test_with_cobertura_vendaval_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_cobertura_vendaval() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 325.36)

    def test_with_assistencia_optional(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_assistencia() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 301.74)

    def test_with_all_optional_coverage(self):
        premio_liquido_class = PremioLiquido(aluguel=1000)
        premio_liquido = premio_liquido_class.with_seguro_conteudo() \
            .with_resp_civil() \
            .with_danos_eletricos() \
            .with_cobertura_vendaval() \
            .with_assistencia() \
            .calculate()
        iof_total = calculate_iof_total(premio_liquido)
        result = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)
        self.assertEqual(result, 696.47)
