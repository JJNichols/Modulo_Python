listaNumeros = [1,2,3,4,5];
listaStrings = ['a','b','c','d'];
listaMista = [1, 'a', 3.14, True];
print(listaNumeros);
print(listaStrings);
print(listaMista);

frutas = ["maça", "banana", "morango"];

print(frutas[1])

frutas[1] = "laranja";
frutas.append("Abacaxi");
print(frutas)

print("Tamanho 2: ", len(frutas))

listaNova = [1, ["a", "b]"]];
print(listaNova[1][0]);

lista1 = [1,2,3];
lista2 = [4,5,6];

listaConcatenada = lista1 + lista2;
print(listaConcatenada)

listaRepetida = [0]* 4;
print(listaRepetida);

numeros = [1,2,3,4];
sublista = numeros[1:4];
print(sublista);

letras = ["a", "b","c", "d",]
sublista = letras[1:4];
print(sublista);

frutas = ["maça", "banana", "laranja"];
frutas.append("morango", "abacaxi");
print(frutas);

frutas.insert(1, "abacaxi");
print(frutas);
print();
frutaRemovida = frutas.remove("banana");
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);

frutas.sort();

print("Embaralhado: ", frutas);




