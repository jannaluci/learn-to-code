
# 1- Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

"""print("Olá! Qual o seu nome?")
nome = input ()

print("Bem-vinde, ", nome,"! Qual a sua idade?")

idade_user = int(input ())

if idade_user >=18:
	print("Você é maior de idade!")
else:
	print("Você é menor de idade")

2- Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, 
senão escreva reprovado. 

print ("Olá! Por favor, inserir a nota um:")
n1 = int(input ())

print ("Por favor, inserir a nota dois:")
n2 = int(input())

if n1 >=6 or n2 >=6:
	print("Aprovado!")
else:
	print("Reprovado!")

"""
# 3- Escreva um programa que resolva uma equação de segundo grau. 
print("Digite o valor de a. Não esqueça de incluir o sinal!")
a = int(input())

print("Digite o valor de b. Não esqueça de incluir o sinal!")
b = int(input())

print("Digite o valor de c. Não esqueça de incluir o sinal!")
c = int(input())

print("Aguarde enquanto realizo o cálculo!")

delta = (b**2) - 4*a*c

x1 = (-b + (delta ** (1/2)))/(2*a)
x2 = (-b - (delta ** (1/2)))/(2*a)

print("Cálculo realizado. Quer que mostre o valor do delta?")
resp_delta = input().lower()

if resp_delta in ("sim", "s"):
	print ("O valor de delta é:", delta)
	print ("x1=", x1)
	print ("x2=", x2)
else:
	print ("x1=", x1)
	print ("x2=", x2)




# 4 -Escreva um programa que ordene uma lista numérica com três elementos.   

# 5 - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.    

