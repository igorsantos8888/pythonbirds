class Pessoa:
    def __init__(self, nome=None, idade=None, localidade=None):
        self.nome = nome
        self.idade = idade
        self.localidade = localidade
    
    
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
if __name__ == '__main__':
    p = Pessoa('Igor', 25, 'RJ')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    print(p.localidade)