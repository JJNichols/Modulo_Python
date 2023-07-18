from conta_bancaria_inical import Conta

conta = input("Informe o número da conta: ");
titular = input("Informe o titular da conta: ");
saldo = float(input("Informe o saldo da conta: "));

#Crinado uma instância da classe
minhaConta = Conta(conta, titular, saldo);

#Realizando operações na conta

depositar = float(input("Informe o valor para deposito: "));
sacar     = float(input("Informe o valor de saque: "));

minhaConta.depositar(depositar);
minhaConta.sacar(sacar);

#Exibindo as inforações
minhaConta = Conta(conta, titular, saldo);