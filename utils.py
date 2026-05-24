#funcoes de apoio que são usadas em  varias partesdo sistema de design

def mostrar_titulo(texto):
         #mostra um titulo com borda dupla pra destacar
    largura = 50
    print("\n" + "=" *largura)
    print(" " + texto.upper().center(largura - 4))
    print("=" * largura)
def linha():
          #linha pra separar
    print("-" * 50)
def linha_dupla():
    print("=" * 50)
def pausar():
               #espera o usuario apertar enter pra continuar
    print()
    input("  [ pressione enter para continuar...]")
def cabecalho_sistema():
             #mostra o cabeçalho da locadorano topo do menu
    print()
    print("=" * 50)
    print("  LOCADORA DE FILMES  ".center(50))
    print("  sistema de gerenciamento ".center(50))
    print("=" * 50)

#leitura de dados

def ler_numero(mensagem, minimo=None, maximo=None):
          #le um numero inteiro do usuario
          #tem try/except pra não quebrar se a pessoa digitar letra
    while True:
        try:
            numero = int(input(mensagem))
            if minimo is not None and numero < minimo:
                print(" [!] numero muito pequeno, tente de novo.")
                continue
            if maximo is not None and numero > maximo:
                print(" [!] numero muito grande, tente de novo.")
                continue
            return numero
        except ValueError:
            print(" [!] isso não é um numero valido! tente de novo")

def ler_texto(mensagem):
                 #le um texto e não deixa ficar vazio
    while True:
        texto = input(mensagem)
        if len(texto) > 0:
            return texto
        print("  [!] não pode ficar vaziu!digite alguma coisa.")
def escolher_da_lista(titulo, opcoes):
       #mostra as opçoes numeradas e retorna a que o usuario escolheu
       print(titulo)
       for i in range(len(opcoes)):
           print(f"  {i+1}. {opcoes[i]}")
       escolha = ler_numero(" Escolha o número: ", minimo=1, maximo=len(opcoes))
       return opcoes[escolha-1]

#exibição de filmes

def mostrar_filme(filme):
        #mostrar as informaçoes de um filme formatadas na tela
    status_icone = "[OK]" if filme['status'] == 'Disponivel' else "[--]"
    print(f" ID: {filme['id']}  |  {status_icone}  {filme['status']}")
    print(f" Titulo :  {filme['titulo']}")
    print(f"  Gênero : {filme['genero']}  |  ano:  {filme['ano']}")
    if filme.get('total_alugueis', 0) > 0:
        print(f"  Alugado: {filme['total_alugueis']} vez(es)")
 
