class Pessoa:
    olhos = 2
    
    def __init__(self, *filhos, nome=None, idade=None, localidade=None):
        self.nome = nome
        self.idade = idade
        self.localidade = localidade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    @staticmethod
    def metodo_estatico():
        return 40 + 37
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'
    
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
    rogerio.olhos = 1
    print(rogerio.__dict__)
    print(igor.__dict__)
    Pessoa.olhos = 3
    print(f'Olhos: {Pessoa.olhos}')
    print(f'Olhos do Rogério: {rogerio.olhos}')
    print(f'Olhos do Igor: {igor.olhos}')
    print(f'Pessoa olhos: {id(Pessoa.olhos)} | Igor {id(igor.olhos)} | Rogerio {id(rogerio.olhos)}') 
    print(Pessoa.metodo_estatico(), rogerio.metodo_estatico()) 
    print(Pessoa.nome_e_atributos_de_classe(), rogerio.nome_e_atributos_de_classe()) 