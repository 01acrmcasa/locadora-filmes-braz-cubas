#ponto de entrada do sistema
#grupo: marcelo, ana, daniel - 1 semestre de ads

import utils #imposrta as funções e informações do util e tarefas 
import tarefas 

#função que vai mostrar o menu com todas as opções na tela
'''
exibe as opçoes organizadas na tela
da o boas vindas ao sistema e fica esperando o usuario digitar a opção
'''
def mostrar_menu():
    utils.cabecalho_sistema()
    print()
    print("----filmes----")
    print("1-Registrar filme")
    print("2-Ver todos os filmes")
    print("3-Pesquisar filme")
    print("4-Ver filmes disponiveis por gênero")
    print()
    print("----reserva e alugueis----")
    print("5-Reservar filme")
    print("6-Processar aluguel")
    print("7-Ver fila de reservas")
    print()
    print("----devoluçoes----")
    print("8-Devolver filme")
    print("9-Ver historico de devoluçoes")
    print()
    print("----relatorio-----")
    print("10-Ver faturamento e movimentações")
    print()
    print("0-Sair do sistema")
    utils.linha_dupla() #importa função do utils

    #cabeçalho do menu, mostra o nome do sistea e duas linhas parav destacar
def main():
    print()
    print("=" * 50)
    print("  Bem Vindo a Locadora de Filmes!  ")
    print("=" * 50)
    print()
    input(" Clique enter para começar... ")

    #este é o loop principal do sistema, so vai sair quando o usuario digitar 0
    while True:
        mostrar_menu()
        opcao = utils.ler_numero(" digite a opção: ", minimo=0, maximo=10)
        if opcao == 1:
            tarefas.cadastrar_filme()
        elif opcao == 2:
            tarefas.listar_filmes()
        elif opcao == 3:
            tarefas.buscar_filme()
        elif opcao == 4:
            tarefas.listar_por_genero()
        elif opcao == 5:
            tarefas.reservar_filme()
        elif opcao == 6:
            tarefas.processar_aluguel()
        elif opcao == 7:
            tarefas.ver_fila()
        elif opcao == 8:
            tarefas.devolver_filme()
        elif opcao == 9:
            tarefas.ver_historico()
        elif opcao == 10:
            tarefas.ver_faturamento()
        elif opcao == 0:
            print("\n encerramento o sistema... ate mais!\n")
            break #termina o while true, enquanto seja verdadeiro
main()

