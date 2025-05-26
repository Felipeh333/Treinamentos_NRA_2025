# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama:Exemplificar uma classe chamada pessoa e seus métodos

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        print(f'{self.nome} chegou!')

    def comer(self, alimento):
        if self.falando:
            print(
                'Erro-Não se pode comer enquanto fala, se quiser muito comer use interromper_fala()')
        elif not self.falando:
            if self.comendo:
                print(f'{self.nome} já está comendo')
                return
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True

    def interromper_comer(self):
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(
                'Erro - Não se pode falar enquanto come, se quiser muito falar use interromper_comer')
        elif not self.comendo:
            print(f'{self.nome} está falando sobre {assunto}')
            self.falando = True

    def interromper_fala(self):
        self.falando = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade


Pessoa1 = Pessoa('Jefinho', 4)

Pessoa1.falar('Futebol')

Pessoa1.comer('Jiló')

Pessoa1.interromper_fala()

Pessoa1.comer('Jiló')
