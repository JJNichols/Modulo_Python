#Estruturas condicionais

#Verificação de idade para entrada em clube noturo
idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Bem vindo(a)(e), você pode entrar na festa!");
else:
    print("Descuple, você não tem idade suficiente para entrar no festa");
print();
    
#Verificar se um número está dentro de um intervalo entre 10 e 20;
numero = 15;

if numero >= 10 and numero <= 20:
    print("O número está dentro do intervalo");
else:
    print("O número está fora do intervalo");
print();    

numero = 21;

if (numero >= 10 ) and (numero <= 20):
    print("O número está dentro do intervalo");
else:
    print("O número está fora do intervalo");
print();  

#Comprar o tamanho de duas listas
lista1 = [1,2,3,4,5];
lista2 = [5,4,3,2,'a']

if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista2");
elif len(lista2) > len(lista1):
    print("A lista 2 é maior que a 1");
else:
    print("As listas tem o mesmo tamanho");
print();

#Verficação de acesso um sistema
senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Usario logado com sucesso");
else:
    print("A senha informada está errada!");
print();
    
#Vertifição de acesso um sistema com login e senha

usuario = input("Digite o seu usuário: ");
senha   = input("Digite sua senha: ");

usuarioCorreto ="admin";
senhaCorreta   ="admin";

if usuario == usuarioCorreto and senha == senhaCorreta:
    print("Login bem-sucedido");
else:
    print("Usuário ou senha incorreto!");
    
    
if(usuario != usuarioCorreto and senha != senhaCorreta):
    print("Usuário e senha incorretos!");48
if usuario != usuarioCorreto:
    print("O usuário está incorreto!");
elif not (senha == senhaCorreta):
    print("A senha está incorreta!");
elif usuario == usuarioCorreto and senha == senhaCorreta:
    print("Login bem suceido");
else:
    print("Usuário ou senha incorreto!");
    
    
#Verifica de multiplas condições com "and" ou "or"

numero = 10;

if(numero > 0 and numero < 5) or (numero > 10 and numero < 15):
    print("O número atende aos critérios");
else:
    print("O número não atende os critérios");
    
#Verificação de uma condições negada
#Carteira de motorista

idade = 20;
possuiCarteira = False;

if idade >= 18 and not possuiCarteira:
    print("Você está apto a dirigir");
else:
     print("Você precisa de ter a carteira de motorista!");
    
#MATCH CASE
comando = "Olá, Mundo!"

match comando:
    case "Olá Mundo!":
        print("Olá para voce também");
    case "Adeus, Mundo":
        print("Adeus!");
    case _:
        print("Sem resultado");