class Pessoa:  
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

# Criando instância da classe Pessoa
pessoa1 = Pessoa('Alice', 25, 1.65)
pessoa2 = Pessoa('Bob', 30, 1.80)
pessoa3 = Pessoa('Dean', 40, 1.86)

# # Acessando os atributos
# print(pessoa1.nome)

resposta = input('Escreva seu nome: ').lower()

if resposta == "Alice".lower():
    print(pessoa1.nome, pessoa1.idade, pessoa1.altura)

elif resposta == "Bob".lower():
    print(pessoa2.nome, pessoa2.idade, pessoa2.altura)

elif resposta == "Dean".lower():
    print(pessoa3.nome, pessoa3.idade, pessoa3.altura)

else:
    print('Nenhuma pessoa encontrada!')