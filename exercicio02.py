'''
Fazer um programa que pergunte um número inteiro e apresente ao usuário
o antecessor e o sucessor do número informado
'''

# 1. Mais uma vez, o input deve ser convertido para um valor que pode ser calculado.
a = int(input("Informe um número"))

# 2. A processo de cálculo pedido.
su = a + 1
an = a - 1

# 3. Saída de dados.
print("O antecessor de",a, "é: ",an, "E o sucessor é: ",su)
