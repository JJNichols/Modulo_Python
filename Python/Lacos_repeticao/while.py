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

#Exemplo: Implementção de menu opções.

opcao = 0;

while opcao != 4:
    print("Menu:");
    print("1. Opção 1");
    print("2. Opção 2");
    print("3. Opção 3");
    print("4. Sair");
    
    
    opcao = int(input("Informe a opcao escolhida: "));
    if opcao == 1:
        print("Opção 1 selecionada!");
    elif opcao == 2:
        print("Opção 2 selecionada!");
    elif opcao == 3:
        print("Opção 3 selecionada!");
    elif opcao == 4:
        print("Saindo....");
        break;
    else:
        print("Opção inválida, tente novamente");
    
#EMULANDO DO WHILE

palavraSecret = "python";
counter = 0;

while True:
    palavra = input("Informe a palavra secreta").lower();
    contador += 1;
    
    if palavra == palavraSecret:
        print("Você acertou a palavra secreta!");
        break;
    
    if palavra != palavraSecret:
        tentivas = 7 - contador;
        print(f"Palavra errada! Você possui {tentivas}de um total de 7 tentativas");
        
    if(palavra != palavraSecret and contador > 7):
        print("Você atingiu o limite de tentativas!");


    


