#!/usr/bin/python3


class CanalDeMensagem:
    """
        Classe Abstrata de canais
    """

    def __init__(self, destino, mensagem):
        self.destino = destino
        self.mensagem = mensagem

    def envio_mensagem(self):
        raise NotImplementedError('Deve ser implementado')




