class Pessoa:
    olhos = 2
    
    def __init__(self, *filhos, nome=None, idade=None, localidade=None):
        self.nome = nome
        self.idade = idade
        self.localidade = localidade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'
    
    @staticmethod
    def metodo_estatico():
        return 40 + 37
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'
    

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

    
if __name__ == '__main__':
    igor = Mutante(nome='Igor')
    rogerio = Homem(igor, nome='Rogério')
    
    homem_1 = Homem(nome='José')
    homem_2 = Homem(nome='Malaquias')
    print(homem_1.nome)
    print(homem_2.nome) 
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
    print(f'Olhos: {Pessoa.olhos}')
    print(f'Olhos do Rogério: {rogerio.olhos}')
    print(f'Olhos do Igor: {igor.olhos}')
    print(f'Pessoa olhos: {id(Pessoa.olhos)} | Igor {id(igor.olhos)} | Rogerio {id(rogerio.olhos)}') 
    print(Pessoa.metodo_estatico(), rogerio.metodo_estatico()) 
    print(Pessoa.nome_e_atributos_de_classe(), rogerio.nome_e_atributos_de_classe()) 
    
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(igor.olhos)
    print(igor.cumprimentar())
    print(rogerio.cumprimentar())