import random

#Como gerar um número aleatório

palpite_intervalo = 10;
resposta = random.randint(1, palpite_intervalo);
palipities_permitidos = 10;

print("Bem vindo ao jogo de adivinhação de numeros!");
print("");
usariodoEntrada = input("Adivinhe um número entre 1 e " + str(palpite_intervalo) + ": ");
adivinhacao = int(usariodoEntrada);



#Como mudar a dificuldade do jogo

print("Bem-vindo ao jogo de adivhação de números (nivel)");
print("");
while True:
    nivel = input("Selecione o nível de dificuldade(fácil, médio, difícul): ").lower();

    if nivel in ["fácil", "médio", "difícul"]:
        break
  
    else:
        print("Entrada inválida.  Selecione 'facíl, 'médio' ou 'difícul.");
    
if nivel == "fácil":
  palpite_intervalo = 10;
  palpites_permitidos = 5;
elif nivel == "medium":
  palpite_intervalo = 20;
  palpites_permitidos = 10;
else:
  palpite_intervalo = 30;
  palipities_permitidos = 15;

resposta = random.randint(1, palpite_intervalo);

#Como verificar se o usuário adivinhou o número correto

adivinhacao = "";
while adivinhacao != resposta:
    usariodoEntrada = input("Adivinhe um número entre 1 e " + str(palpite_intervalo) + ": ");
    adivinhacao = int(usariodoEntrada);
    
print ("Parábens!  Você adivinhou o número correto. Você ganha!");

#Como adicionar um número limitado de palpites

for i in range(palpites_permitidos):
    usariodoEntrada = input("Adivinhe um número entre 1 e " + str(palpite_intervalo) + ": ");
    adivinhacao = int(usariodoEntrada);
    
    if adivinhacao == resposta:
        print("Parabéns! Você adivinhou o número correto. Você ganha!");
        break

    if (i == palpites_permitidos -1):
        print("Desculpe, você ficou sem palpites. Você perdeu!");
 
#Como adicionar dicas ao jogo
 
    if adivinhacao == resposta:
        print ("Parábens!  Você adivinhou o número correto. Você ganha!");
        break
    elif adivinhacao < resposta:
        print("O número é maior.");
    else:
        print("O número é menor.");

    if abs(adivinhacao - resposta) <= 10:
        print("Você está quente!");
    elif abs(adivinhacao - resposta) <= 20:
        print("Você está ficando mais quente.");
    elif abs(adivinhacao - resposta) <= 30:
        print("Você é frio.");
    else:
        print("Você está congelando.");

    print("fim do jogo!");
