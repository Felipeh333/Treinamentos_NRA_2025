class Pessoa:
    # atributos do objeto
    def __init__(self, nome, idade, falando, comendo = False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    # metodo de instancia: comer
    def comer(self, alimento):
        if self.falando == True and self.comendo == True:
            print(f'ERRO! Não se pode falar enquanto se come {alimento}!')
            return
        elif self.comendo == True:
            print(f'{self.nome} já está comendo')
            return
        else:
            print(f'{self.nome} não está comendo')
            return
    
    # metodo de instancia: falar
    def falar(self, assunto):
        if self.comendo == False and self.falando == True:
            print(f'{self.nome} está falando sobre {assunto}')
            return
        else:
            print(f'ERRO! {self.nome} está comendo, não está falando sobre {assunto}')
            return

# valores meramente exemplarees
p1 = Pessoa('Pedro', 18, False, False)
p1.comer('abóbora')
p1.falar('fisiculturismo')
