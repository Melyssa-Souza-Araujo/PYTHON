print("Olá, Mundo!")
print(2026)

nome = "Ana"          # Texto (chamado de String ou 'str')
idade = 25            # Número inteiro (chamado de Integer ou 'int')
altura = 1.68         # Número com vírgula/ponto (chamado de Float)
estudante = True      # Verdadeiro ou Falso (chamado de Boolean ou 'bool')

# Usando as variáveis:
print(nome)
print("A idade da", nome, "é", idade)

soma = 10 + 5
multiplicacao = 4 * 2
quadrado = 3 ** 2  # 3 elevado a 2 (3²)

print(soma)          # Saída: 15
print(quadrado)      # Saída: 9

idade = 18

if idade >= 18:
    print("Você é maior de idade. Pode tirar a habilitação!")
else:
    print("Você é menor de idade.")

frutas = ["Maçã", "Banana", "Morango"]

# Pegando o primeiro item da lista (Índice 0)
print(frutas[0])  # Saída: Maçã

# Adicionando um item novo
frutas.append("Uva")
print(frutas)  # Saída: ['Maçã', 'Banana', 'Morango', 'Uva']

nome = input("Qual o seu nome? ")
print("Olá, " + nome + "! Prazer em te conhecer.")

# range(5) gera números de 0 a 4
for i in range(5):
    print("Número:", i)

contador = 1
while contador <= 3:
    print("Contagem:", contador)
    contador = contador + 1  # Aumenta o contador para não ficar em loop infinito

def saudar_usuario(nome_pessoa):
    print("Olá, " + nome_pessoa + "! Bem-vindo ao curso de Python.")

# Chamando a função
saudar_usuario("Carlos")
saudar_usuario("Mariana")
