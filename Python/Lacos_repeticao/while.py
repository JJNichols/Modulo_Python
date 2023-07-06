#exemplo 1: Contagem regressa de 10 a 1

contador = 10;

while contador >= 1:
    print(contador);
    contador -= 1;
    
#Exemplo 2: Leitura de alunos até que uma nota negativa seja inserida

notas =[];
nota = float(input("Digite uma nota (-1 para sair): "));

while nota >= 0:
    notas.append(nota);
    nota = float(input("Digite uma nota(-1 para sair): "));
    
print(notas);
    
#Exemplo 3: Verificação de senha correta

senha = input("Informe uma senha: ");
senhaBloqueada = False;

while senha != '123456':
    print("Senha incorreta");
    contador += 1;
    if(contador ==5):
        print("Sua senha foi bloqueada!");
        senhaBloqueada = True;
        break;
    senha = input("Digite a senha: ");

if(senhaBloqueada):
    print("Sua senha foi bloqueada!");
else:
    print("Senha correta!");
    
#Exemplo 4: Impressão dos primeiros N numeros pares

quantidade = int(input("Informe a quantidade de numeros a serem impressos: "));
contador = 1;
while quantidade > 0:
    if contador % 2 == 0:
        print(contador);
        quantidade -= 1;
    contador += 1;
    
#Joga da adivinhação

numeroSecreto = 42
palpite = int(input("Digite um número: "));

while palpite != numeroSecreto:
    print("Você errou!  Tente novamente");
    palpite = int(input("Digite um número: "));
    
print("Parabéns! Você acertou o palpite!");

#Exemplo 6:  Impressão de uma sequência de caracteres até que a palavra "sair" seja digitada

palavra = input("Digite uma palavra ('sair' para encerrar)");
palavra = palavra.lower();

while palavra != 'sair':
    print(palavra);
    palavra = input("Digite uma palavra ('sair' para encerrar)");
    palavra = palavra.lower();    


