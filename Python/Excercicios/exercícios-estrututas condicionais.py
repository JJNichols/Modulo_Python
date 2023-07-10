#1-Escreva um programa que solicite ao usuário dois números inteiros e exiba a soma, subtração, multiplicação e divisão entre esses números.

a = int(input("Digite um primeiro número a: "));
b = int(input("Digite um segundo número b: "));

soma            = a + b;
subtracao       = a - b;
multiplicacao   = a * b;
divisao         = a / b;

print ("Soma:  ", soma);
print ("Subtração: ", subtracao);
print ("Multiplicação: ", multiplicacao);
print ("Divisão: ", divisao);

print();

#2- Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e verifique se ela está acima do ponto de ebulição da água (100°C). Caso positivo, exiba a mensagem "A água está fervendo!".

temperatura = float(input("Digite temperatura em grau Celsius: "));

if temperatura > 100:
    print("A água está fervendo!");
else:
    print("A água não está fervendo!")

print();

#3- Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro é: "))

if numero % 2 == 0:
    print ("Par");
else:
    print("Ímpar");
    
print();

#4- Escreva um programa que solicite uma senha ao usuário e verifique se a senha está correta. Considere a senha correta como "123456".

senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Your password is right!");
else:
    print("Your password is wrong!");
    
print();

#5- Escreva um programa que solicite ao usuário uma idade e verifique se ela está entre 18 e 30 anos (inclusive).

idade = int(input("Digite sua idade: "));

if idade >= 18 and idade <= 30:
    print("Parabéns!! Sua idade está entre 18 a 30 anos.");
else:
    print("Descuple!  Sua idade não está entre 18 e 30 anos.");
    
print();

#6- Escreva um programa que solicite ao usuário três números inteiros e verifique se pelo menos um deles é positivo.

num1 = int(input("Digite um numero 1: "));
num2 = int(input("Digite um numero 2: "));
num3 = int(input("Digite um numero 3: "));

if num1 > 0 or num2 > 0 or num3 > 0:
    print("Pelo menos um dos números é POSITIVO!");
else:
    print("Infelizmente, dos números não é positivo!");
    
print();

#7- Escreva um programa que solicite ao usuário uma letra e verifique se ela é uma vogal (a, e, i, o, u).

vogal = input("Digite uma vogal: ");

if vogal.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Uma palavra tem vogal.");
else:
    print("Uma palavra não tem vogal.");
    
print();

#8- Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

number = int(input("Type a number: "));

if number > 0:
    print("The number is positive.");
elif number < 0:
    print ("The number is negative.");
else:
    print("The number is zero.");
    
print();

#9- Escreva um programa que solicite ao usuário três números e verifique se eles estão em ordem crescente.

number1 = float(input("Enter the 1st numbers: "));
number2 = float(input("Enter the 2nd numbers: "));
number3 = float(input("Enter the 3rd numbers: "));

if(number1 and number2) and (number2 and number3):
    print("The numbers are in ascending orders.");
else:
    print("The numbers are not in ascending order.");
    
print();

#10- Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.

numero1 = int(input("Digite um número interiro: "));

if(numero1 % 3 == 0) and (numero1 % 5 == 0):
    print("Um número é um múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("Um número não é múltiplo de 3 e 5 mesmo tempo.");
    
print();


