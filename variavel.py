# O "input" aguarda uma resposta do usuário
'''
Outro
Comentário
'''
# nome = input("Qual é o seu nome?")

# print("Olá,", nome, ", Este é um programa feito para testar o git e entender alguns conceitos iniciais de Python")
# print("exemplo1")

# print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

print("Tipo da variável a: ", type(a)) # tipo inteiro (números inteiros)
print("Tipo da variável b: ", type(b)) # tipo float (números reais)
print("Tipo da variável c: ", type(c)) # tipo string (alfanumerico, mas apenas texto)
print("Tipo da variável d: ", type(d)) # Tipo boolean (True, False)

a = 20

print("a: ", a)
b = "São Paulo"
print("b: ", b)
print("Tipo da variável a: ", type(a)) # tipo inteiro (números inteiros)
print("Tipo da variável b: ", type(b)) # tipo string

a = input("Informe um número: ")
b = input("Informe outro número: ")
print("a: ", a, "- b: ", b)
print("Tipo da variável a: ", type(a))
print("Tipo da variável b: ", type(b))
c = a + b # contatenou strings a e b
print("c: ", c)
print("Tipo da variável c: ", type(c))

d = int(a)
print("d: ", d)
print("Tipo da variável d: ", type(d)) # Agora é um inteiro

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
print("a: ", a, "- b: ", b)
print("Tipo da variável a: ", type(a))
print("Tipo da variável b: ", type(b))
c = a + b
print("c:", c)

a = float(input("Informe um número: "))    # Agora com float
b = float(input("Informe outro número: ")) # Agora com float
print("a: ", a, "- b: ", b)
print("Tipo da variável a: ", type(a))
print("Tipo da variável b: ", type(b))
c = a + b
print("c:", c)