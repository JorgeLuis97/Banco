from CRUD import consulta, deposito, saque, transferencia
from banco import *


def menu():
    while True:
        print("---- MENU ----")
        print("1 - Adicionar conta\n"
              "2 - Editar Nome\n"
              "3 - Excluir Conta\n"
              "4 - Consultar conta\n"
              "5 - Listar Contas\n"
              "6 - Consultar Saldo\n"
              "7 - Depositar\n"
              "8 - Saque\n"
              "9 - Transferencia\n"
              "10 - Sair\n")
        opcao = int(input("Selecione uma opção: "))
        print("")

        if opcao == 1:
            nome = input("Nome do Cliente: ")
            saldo = float(input("Saldo do Cliente: "))
            adicionarconta(nome, saldo)
        elif opcao == 2:
            conta = int(input("Conta a ser editada: "))
            novo_nome = input("Novo Nome: ")
            editarnome(novo_nome, conta)
        elif opcao == 3:
            conta = int(input("Conta a ser excluida: "))
            deletarconta(conta)
        elif opcao == 4:
            conta = int(input("Conta a ser consultada: "))
            consultarcliente(conta)
        elif opcao == 5:
            listarcontas()
        elif opcao == 6:
            conta = int(input("Conta a ser consultada: "))
            consulta.consultarsaldo(conta)
        elif opcao == 7:
            conta = int(input("Conta: "))
            valor = float(input("Valor: "))
            deposito.depositar(conta, valor)
        elif opcao == 8:
            conta = int(input("Conta: "))
            valor = float(input("Valor: "))
            saque.saque(conta, valor)
        elif opcao == 9:
            cliente1 = int(input("Conta Origem: "))
            valor = float(input("Valor a ser transferido:"))
            cliente2 = int(input("Conta Destino: "))
            transferencia.transferencia(cliente1, valor, cliente2)
        elif opcao == 10:
            print("Saindo...")
            break


if __name__ == '__main__':
    menu()
