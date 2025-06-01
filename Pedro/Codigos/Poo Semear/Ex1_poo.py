class Pessoa:

    def __init__(self,nome,idade,falando = False, comendo = False):
        self.nome = nome
        self.idade = idade
        self.falando = falando 
        self.comendo = comendo
    
    def comer(self,alimento):
        if self.falando:
            self.interrompe_comer()
            return
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        print(f"{self.nome} está comendo {alimento}")

    def falar(self,assunto):
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        if self.comendo:
            self.interrompe_falar()
            return
        print(f"{self.nome} está falando sobre {assunto}")

    def  interrompe_comer(self):
        print(f"{self.nome} não pode comer pois está falando")

    def interrompe_falar(self):
        print(f"{self.nome} não pode falar pois está comendo")

p1 = Pessoa("Gabriel",12)
p1.falar("politica")
