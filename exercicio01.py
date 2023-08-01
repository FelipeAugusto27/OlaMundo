'''
Elabore um progrmama que pergunte ao aluno as suas 3 notas escolares
O programa deverá calcular a média das 3 notas inseridas e
exibir esta média
'''

# 1. sempre começando com o input, lembrando que input é sempre string. Portando, deve-se converter para float (inclui decimais).
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))

# 2. com as informações em mãos, é média deverá ser calculada e informada.
# v = (v + v + v)/3
media = (nota1 + nota2 + nota3)/3

# 3. agora o output
print("A sua média é de: ", media)
