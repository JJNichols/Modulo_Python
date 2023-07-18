#Solução orientada a objetos para um banco com a entidade "Conta"

class Conta:
    #Criar um metodo construtor
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero;
        self.titular = titular;
        self.saldo = saldo;
        
    def depositar(self, valor):
        self.saldo += valor;
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
            print("Saldo insuficiente!");
            
    def exibir_informacoes(self):
        print(f"Conta: {self.numero}");
        print(f"Titular: {self.titular}");
        print(f"Saldo: {self.saldo:,.2f}");
        
        print(f"Saldo antes da conversão para real: {self.saldo:,.2f}");
        valorEmReal = f'R${self.saldo:_.2f}';
        print();
        valorEmReal = valorEmReal.replace('.', ',').replace('_', '.');
        print(f"Saldo: {valorEmReal}");
    #Criação de uma conta e realização de operações
    
conta = Conta(123, "Jason");
conta.depositar(1000);
conta.sacar(500);
conta.exibir_informacoes();
print("----")
conta1 = Conta(321, "Guilherme", 100);
conta1.depositar(500);
conta1.sacar(250);
conta1.exibir_informacoes();
print("----")   
conta2 = Conta(132, "Zyan");
conta2.depositar(2000);
conta2.exibir_informacoes();