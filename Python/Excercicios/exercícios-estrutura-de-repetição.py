#1-Utilizando um loop "while", imprima os números de 1 a 10.

numero = 0;

while numero <= 9:
    numero = numero + 1
    print(numero);
    

#2- Utilizando um loop "for", imprima os números de 1 a 10.

for numero in range(1, 11):
    print(numero);

#3- Utilizando um loop "while", calcule a soma dos números de 1 a 100.

numero = 1
soma = 0

while numero <= 100:
    soma   = numero + soma;
    numero = numero + 1;
    print("A soma dos números de 1 a 100 é: ", soma);
    

#4- Utilizando um loop "for", calcule a soma dos números de 1 a 100.

numero = 1
soma = 0

for numero in range(1, 101):
    print ("O range de números de 1 a 100 é ", numero);
    soma += numero;
    print("A soma dos números de 1 a 100 é ", soma);
    
#5- Utilizando um loop "while", imprima os números pares de 1 a 20.

numero = 2;

while numero <= 20:
    print("Os números pares de 1 a 20 é ", numero);
    numero += 2
print();
    

#6- Utilizando um loop "for", imprima os números pares de 1 a 20.

for numero in range(2, 21, 2):
    print("Os números pares de 1 a 20 é ", numero);
print();

#7- Utilizando um loop "while", inverta uma string digitada pelo usuário.

string = input("Digite uma string: ");
invertida = "";
inverta = len(string) -1;

while inverta >=0:
    invertida += string[inverta];
    inverta -= 1;
print("Inverida: ",invertida);

#8- Utilizando um loop "for", verifique se uma palavra digitada pelo usuário é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = input("Digite uma palavra: ");
palindromo = ""

for letra in palavra:
    palindromo = letra + palindromo;
    
   
if palavra == palindromo:
    print("A palavra é uma palíndromo.");
else:
    print("A palavra não é um palíndrom.");
    
#9- Utilizando um loop "while", encontre o menor número inteiro cujo quadrado seja maior do que 1000.

num = 1

while num ** 2 <= 1000:
    num += 1;

print("O menor interior cujo quardrado seja maior do que 100 é: ", num);
print();



#**DESAFIO** 10- Utilizando um loop "for", imprima os elementos de uma lista em ordem inversa.

lista = [1,2, 3, 4, 5, 6, 7, 8];

for elemento in range(len(lista) -1,-1, -1):
    print(lista[elemento]);
