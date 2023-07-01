#1
frutas = ["maça", "banana", "laranja", "abacaxi", "melancia"];
print(frutas);
print("Temos a seguinte lista de frutas: ", frutas);
print();

#2
frutas.append("uva");
print(frutas);
print("Temos uma atualização seguinte lista de frutas: ", frutas);
print();

#3
frutaRemovida = frutas.remove("banana");
print("Removemos a banana na atualização seguinte lista de frutas: ", frutas);
print(frutaRemovida);
print();

#4
fruta_selecionada = frutas[2];
print("Eu amo minha fruta selecionada é ", fruta_selecionada);
print();

#5
cores = ("vermelho", "azul", "verde", "amarelo", "roxo");
print("Essas cores que vou aceitar para pintar meu quarto são ", cores);
print();

#6
cor_selecionada = cores[2];
print("Minha cor favorita é ", cor_selecionada);
print();

#7

#AttributeError: 'tuple' object has no attribute 'append'
#cores.append("laranja");
#print();

#8

aluno = {
    'nome'   : 'Jason',
    'idade'  : 48,
    'cidade' : 'São Carlos - SP'
};
print("Meus dados simples: ", aluno)
print(aluno);
print();

#9
idade_aluno = aluno["idade"];
print("Eu tenho {idade_aluno} anos.");
print();


#10
aluno['gênero'] = "masculino";
print("Meus dados como aluno estão atulizados.");
print (aluno);
print();

#11

alunoRemovido = aluno.pop("cidade");
print(alunoRemovido);
print();
print("Meus dados como aluno estão atulizado: ", aluno);

