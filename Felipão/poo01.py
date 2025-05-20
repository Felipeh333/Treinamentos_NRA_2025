class Pessoa:
    def __init__(self, comendo, falando):
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        if self.comendo:
            print('A pessoa já está comendo.')
        elif self.comendo == False and self.falando == True:
            print('A pessoa não pode comer enquanto fala. O método interromper_fala() pode ser útil.')
        else:
            print('A pessoa está comendo.')
            self.comendo = True
    
    def falar(self, assunto):
        if self.comendo:
            print('A pessoa não pode falar enquanto come. O método interromper_comer() pode ser útil.')
        else:
            print(f'A pessoa está falando sobre {assunto}.')
            self.falando = True

    def interromper_comer(self):
        if self.comendo:
            print('A pessoa parou de comer.')
            self.comendo = False
        else:
            print('A pessoa não está comendo no momento.')

    def interromper_fala(self):
        if self.falando:
            print('A pessoa parou de falar.')
            self.falando = False
        else:
            print('A pessoa não está falando no momento.')