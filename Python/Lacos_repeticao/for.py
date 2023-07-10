#Exemplo 1: Impressão números 1 a 10

for numero in range(1, 11):
    print(numero);
    
#Exemplo 2: Impressão de frutas de uma lista de frutas

frutas = ["maça", "laranja", "uva"];

for fruta in frutas:
    print(fruta);
    
#Exemplo 2.1

for fruta in frutas:
    if fruta != "laranja":
        print(fruta);
        continue;
    print(fruta);
    
#Exemplo 2.2

for fruta in frutas:
    if(fruta == "laranja"):
        print("Encontrou laranja!");
        break;
    print(fruta);
    
#Exemplo 3: Cálculo da média de uma lista de notas

notas = [7.5, 8.0, 6.5, 9.0, 7.0];

soma = 0;

for nota in notas:
    soma += nota;

media = soma / len(notas);
print("A média é: ", media);

#Exemplo 4: Contando as vogals de uma string

palavra = "Python";
vogais  = 0

for letra in palavra:
    if letra in "aeiou":
        vogais += 1;
        
print(f"A palavra {palavra} possui {vogais} vogal");

#Ineração sobre os itens de uma lista

lista = ["a", "b","c", "d", "e"];

for indice in range(len(lista)):
    if indice == 0:
        lista[indice] ="z";
    print(f"O elemento no índice {indice} é {lista[indice]}");
    
#Iteração sobre um elemento número com incremento

for numero in range(2, 11, 2):
    print(numero);

