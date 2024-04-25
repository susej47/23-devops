""" Test de la función suma para ejemplo devops

    El tercero de los test debe fallar para probar Action
"""
import unittest
from app import suma


class SumaTest(unittest.TestCase):
    """ Docstring class """

    def test1(self):
        """ Docstring def
        """
        res = suma(1, 5)
        self.assertEqual(res, 6)

    def test2(self):
        """ Docstring def """
        res = suma(0, 0)
        self.assertEqual(res, 0)

    def test3(self):
        """ Esta prueba DEBE FALLAR"""
        res = suma("1", "4")
        self.assertEqual(res, 5)
