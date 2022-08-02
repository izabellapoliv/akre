from django.test import TestCase

from calculations.helpers.conteudo_segurado import calculate_total

class ConteudoSeguradoTestCase(TestCase):
    def test_value_is_correct(self):
        result = calculate_total(cotacao_taxa=0.16, valor_segurado=96000)
        self.assertEqual(result, 9600)
