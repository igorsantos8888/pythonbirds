class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None, localidade=None):
        self.nome = nome
        self.idade = idade
        self.localidade = localidade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
if __name__ == '__main__':
    igor = Pessoa(nome='Igor')
    rogerio = Pessoa(igor, nome='Rogério')
    print(Pessoa.cumprimentar(igor))
    print(id(igor))
    print(igor.cumprimentar())
    print(igor.nome)
    print(igor.idade)
    print(igor.localidade)
    
    for filho in rogerio.filhos:
        print(f'Nome: {filho.nome}')
    rogerio.sobrenome = 'Silva'
    del rogerio.filhos
    print(rogerio.__dict__)
    print(igor.__dict__)