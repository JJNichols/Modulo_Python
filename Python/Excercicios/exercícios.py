
#1 - Crie duas variáveis, nome e idade, e atribua a elas seus próprios valores. Em seguida, use a formatação de strings paraimprimir a seguinte mensagem: "Olá, meu nome é [nome] e eu tenho [idade] anos."

nome  = "Jason";
idade = 48;

print(f"Ola, meu nome é {nome} e eu tenho {idade} anos.");
print();

#2- Crie uma variável chamada frase e atribua a ela uma string. Em seguida, use a função len() para imprimir o comprimento da frase.

frase = "Eu amo viajar no mundo!";
tamanhoFrase = len(frase);
print(frase);
print("Tamanho: ", tamanhoFrase);
print();

#3 - Crie duas variáveis, nome e sobrenome, e atribua a elas seus próprios valores. Concatene as variáveis para criar uma nova variável chamada nome_completo e imprima o resultado.

nome         = "Jason John ";
sobreNome    = "Nichols"
nomeCompleto = nome + '' + sobreNome;
print (nomeCompleto);
print();

#4- Crie uma variável chamada frase e atribua a ela uma string. Use o método upper() para imprimir a frase em letras maiúsculas.
frase = "Preciso estudar mais Python!"
print("Maiúscula: ", frase.upper());
print();

#5- Crie uma variável chamada frase e atribua a ela uma string contendo uma frase completa. Use o método split() para dividir a frase em uma lista de palavras e imprima o resultado.

frase = "Meu amigo leu todas as palavras da frase!";
print("Todas as palavras na frase são divididas: ", frase.split());
print();

#6- Crie uma variável chamada frase e atribua a ela uma string. Use o método replace() para substituir uma palavra específica na frase por outra palavra de sua escolha. Imprima a frase modificada.

frase = "Meu professor é Gian."
print (frase);
frase = frase.replace("Gian","Diego");
print(frase);

#7 - Crie duas váriaveis, “numero1” e “numero2” e atribua valores númerico a elas, depois crie uma váriavel resultado e armazene o resultado da soma das váriaveis “numero1” e “numero2”. Ao final imprima o resultado.

numero1 = 100;
numero2 = 57;
soma = numero1 + numero2;
print("O resultado da soma: ", soma);
print();

#**Extra**

#8- Escreva um programa que solicite ao usuário que digite dois números inteiros e exiba a multiplicação desses números



number1 = int(input("First number is: "));
number2 = int(input("Second number is: "));

multiplication = number1 * number2;


print("Multiplicação resultado: ", multiplication);
print();

