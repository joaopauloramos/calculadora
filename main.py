#!/usr/bin/python3


from framework import Calculadora,CalculadoraInfixa,Operacao

class CalculadoraPrefixa(Calculadora):
    """
        Classe de Operacoes prefixas
    """

    def obter_inputs(self):
        sinal = input('Digite o Sinal da operacao: ')
        p1 = input('Digite o primeiro o numero ')
        p1 = float(p1)
        p2 = input('Digite o primeiro o numero ')
        p2 = float(p2)

class Divisao(Operacao):
    def calcular(self,p1,p2):
        return p1/p2

calculadora = CalculadoraInfixa()
calculadora.adicionar_operacao('/',Divisao())

print(calculadora.efetuar_operacao())