#!/usr/bin/python3

# Classes Abstratas


class Operacao:
    """
        Classe responsavel por definir como calculo deve ser feito

    """

    def calcular(self,p1,p2):
        raise NotImplementedError('Necessario Implementar')


class Calculadora:
    """
        Classe Responsavel por obter inputs e efetuar operacao de acordo com o solicitado

    """

    def __init__(self):
        self._operacoes = {}
        adicao = Adicao()
        self.adicionar_operacao('+',adicao)
        self.adicionar_operacao('*',Multiplicacao())


    def obter_inputs(self):
        """

            Deve obter sinal, p1 e p2 retornando valores nessa ordem
        :return: NotImplementedError
        """

        raise NotImplementedError('Precisa ser implementado')

    def efetuar_operacao(self):
        sinal, p1, p2 = self.obter_inputs()
        try:
            operacao_escolhida = self._operacoes[sinal]

        except KeyError:
            raise Exception('Operacao nao suportada')

        else:
            return operacao_escolhida.calcular(p1,p2)

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao


    # Classes Concretas

class CalculadoraInfixa(Calculadora):
    def obter_inputs(self):
        p1 = input('Digite o primeiro o numero ')
        p1 = float(p1)
        sinal = input('Digite o sinal da operacao {}: '.format(' ; '.join(self._operacoes.keys())))
        p2 = input('Digite o primeiro o numero ')
        p2 = float(p2)
        return sinal, p1, p2


class Adicao(Operacao):
    def calcular(self, p1, p2):
        return p1 + p2

class Multiplicacao(Operacao):
    def calcular(self,p1,p2):
        return p1 * p2



