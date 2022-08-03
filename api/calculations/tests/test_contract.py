from django.test import TestCase

from calculations.helpers.importancia_segurada import calculate_importancia_segurada

class ContractTestCase(TestCase):
    def test_importancia_segurada_is_correct(self):
        result = calculate_importancia_segurada(aluguel=1000)
        self.assertEqual(result, 120000)
