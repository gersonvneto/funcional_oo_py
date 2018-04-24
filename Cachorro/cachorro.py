############
# Funcional e OO
# Prof. Neylson
# Gerson Vasconcelos Neto
# aula 2 - python
###########
# Programando um cachorro

class Cachorro:
    def __init__(self, n, i, r):
        self.nome = n
        self.idade = i
        self.raca = r
        self.temOsso = False
        
    def latir(self):
        if self.temOsso:
            print('Estou com um osso na boca')
        print('Au, Au!')
        
    def darPata(self):
        print('Toma a patinha...')
        
    def fazAniversario(self):
        print('Fiz aniversário!')
        self.idade += 1
        print(f'Agora eu tenho {self.idade} anos!')
    
    def pegaOsso(self):
        if self.temOsso:
            print('Já estou com um osso!')
        else:
            self.temOsso = True
            print('Hummm.. que osso gostoso!')
            
    def largaOsso(self):
        if self.temOsso:
            self.temOsso = False
            print('Larguei o osso!')
        else:
            print('Osso? Aonde??')
    
        