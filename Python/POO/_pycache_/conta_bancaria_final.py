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
            self.exibir_retorno();
            
        def exibir_retorno(self):
            print(f"Saldo insuficiente, você poosui {self.saldo } disponsivel para saaque");
            
    def exibir_informacoes(self):
        print(f"Conta: {self.numero}");
        print(f"Titular: {self.titular}");
        print(f"Saldo: {self.saldo:,.2f}");
        
        print(f"Saldo antes da conversão para real: {self.saldo:,.2f}");
        valorEmReal = f'R${self.saldo:_.2f}';
        print();
        valorEmReal = valorEmReal.replace('.', ',').replace('_', '.');
        print(f"Saldo: {valorEmReal}");