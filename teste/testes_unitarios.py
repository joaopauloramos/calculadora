import unittest
from unittest.case import TestCase

from framework import Adicao, Calculadora

class AdicaoCasosDeTeste(TestCase):
    def teste_com_numero_positivos(self):
        adicao = Adicao()
        for i in range(10):
            self.assertEqual(2* i,adicao.calcular(i,i ))

class CalculadoraTestes(TestCase):
    def teste_adicionar_operacao(self):
        obj_qq = ''
        calculadora = Calculadora()
