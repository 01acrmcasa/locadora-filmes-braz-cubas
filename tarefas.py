##aqui ficam as funcoes principais do sistema da locadora
import dados
import utils #importa as funçoes e informaçoes do util e dados

#cadastrar filme
#-----------------------
'''
Ela pega as informaçoes do filme pelo o que  usuario digita, verifica se ja existe antes de cadastrar pra nao duplicar
monta um discionario com os dados
e insere na lista de filmes, ja com o contador de IDs 

'''
def cadastrar_filme():
    #funcao pra adicionar um novo filme no sistema
    utils.mostrar_titulo("Cadastrar Novo Filme")

    titulo = utils.ler_texto("  Nome do filme: ")

    #verifica se ja tem um filme com esse nome antes de cadastrar, evita ter o mesmo filme duas vezes
    for f in dados.lista_filmes:
        if f['titulo'].lower() == titulo.lower():
            print("\n  [!] Esse filme ja esta cadastrado!")
            utils.pausar()
            return   #sai da função sem precisar cadastrar
          
    genero = utils.escolher_da_lista("\n  Qual o gênero?", dados.generos_possiveis)  #importa do utils
    ano = utils.ler_numero("\n  Ano do filme: ", minimo=1888, maximo=2100)
    #cria o dicionario com as informaçoes do filme que o usario vai colocar
    novo_filme = {
        'id': dados.contador_id,
        'titulo': titulo,
        'genero': genero,
        'ano': ano,
        'status': dados.status_possiveis[0],  #comeca como Disponivel
        'total_alugueis': 0                   #contador de movimentacoes do filme
    }
    #adiciona na lista principal
    dados.lista_filmes.append(novo_filme)
    #atualiza o contador de id
    dados.contador_id += 1
    print(f"\n  [OK] Filme '{titulo}' cadastrado com sucesso!")
    utils.pausar()

#listar filmes
#--------------------------------
'''
Mostra todos os filmes e um resumo no final
com o total de filmes, quantos estão disponiveis e quantos estão alugados
'''
def listar_filmes():
    #mostra todos os filmes cadastrados com o status de cada um
    utils.mostrar_titulo("Catalogo de Filmes") #importa função do utils para mostrar função do tirulo do menu

    if len(dados.lista_filmes) == 0:   #caso a lista tenha 0 filmes mostra a mensagem e retorna sem fazer mais nada
        print("  Ainda não tem nenhum filme cadastrado.")
        utils.pausar()
        return

    disponiveis = 0
    indisponiveis = 0

    for i in range(len(dados.lista_filmes)): #vai ficar rodando de 0 ate a quantidade total de filmes
        utils.mostrar_filme(dados.lista_filmes[i]) #importa função do ults e mostra o filme da posição i
        utils.linha()
        if dados.lista_filmes[i]['status'] == "Disponivel": 
            disponiveis += 1   #este vai contar quantos filmes tem disponiveis
        else:
            indisponiveis += 1 #conta os alugados

    print(f"  Total: {len(dados.lista_filmes)} filme(s)  |  "      #exibe as informaçoes
          f"Disponiveis: {disponiveis}  |  Alugados: {indisponiveis}")
    utils.pausar()

#pesquisa por titulo 
#-------------------------------------------
'''
Ela recebe um trecho do filme que o usuario coloca, e procura na lista um filme que tenha o trecho que foi digitado
e mostra a mensagem caso encontrar ou não
'''
def buscar_filme():
    #busca filmes pelo titulo, nao precisa digitar o nome completo
    utils.mostrar_titulo("Buscar Filme")
    busca = utils.ler_texto("  Digite parte do nome: ")

    encontrou = False
    for f in dados.lista_filmes:
        if busca.lower() in f['titulo'].lower():  #lower() transforma tudo em minusculo antes de comparar
            utils.linha()                         #"in" verifica se o que o usuario sigitou esta contido dentro do tirulo
            utils.mostrar_filme(f)                
            encontrou = True
    if not encontrou:
        print(f"\n  [!] Nenhum filme encontrado com '{busca}'.")
    utils.pausar()

#lista por genero 
#----------------------------------
'''
Usuario escolhe um genero e so aparece os filmes daquele genero
e so mostra os disponiveis
'''
def listar_por_genero():
    #filtra os filmes disponiveis por genero PROCURA POR GENERO
    utils.mostrar_titulo("Filmes por gênero")
    genero = utils.escolher_da_lista("\n  Escolha o gênero:", dados.generos_possiveis)
    print()

    encontrou = False
    for f in dados.lista_filmes:
        if f['genero'] == genero and f['status'] == "Disponivel":
            utils.mostrar_filme(f)
            utils.linha()
            encontrou = True
    if not encontrou:
        print(f"  Nenhum filme disponivel no gênero '{genero}'.")
    utils.pausar()

#reservar filme - fila
#-------------------------------------------
'''
Coloca o cliente no final da fila do filme que ela quer, e pega o primeiro da fila e tenta efetivar o aluguel
se não tiver disponivel, devolve para a fila
'''
def reservar_filme():
    #adiciona o cliente no final da fila de reservas
    #fifo é quem reservou primeiro, aluga primeiro
    utils.mostrar_titulo("Reservar Filme")

    if len(dados.lista_filmes) == 0:
        print("  Nao tem nenhum filme cadastrado ainda.")
        utils.pausar()
        return            #verifica se tem algum filme cadastrado.

    titulo = utils.ler_texto("  Nome do filme que quer reservar: ")
    filme = pegar_filme_por_titulo(titulo)   #pede o nome do filme 

    if filme is None:
        print("\n  [!] Filme nao encontrado.")
        utils.pausar()        #se não achou nada ela devolve none, ai avisa e sai
        return
    print()
    utils.mostrar_filme(filme)
    utils.linha()
    cliente = utils.ler_texto("  Nome do cliente: ")
    #.append() coloca no final da fila 
    dados.fila_de_reservas.append((filme['titulo'], cliente))     #o append coloca no final da fila, guarda titulo e cliente juntos

    print(f"\n  [OK] {cliente} entrou na fila para '{filme['titulo']}'!")
    print(f"  Posicao na fila: {len(dados.fila_de_reservas)}")  #mostra resposta pra o usuario
    utils.pausar()

def processar_aluguel():
    #pega o primeiro da fila e registra o aluguel
    #.pop(0) retira o primeiro, no caso é o fifo funcionando
    utils.mostrar_titulo("Processar Aluguel")

    if len(dados.fila_de_reservas) == 0:  #se a lista tiver vazia mostra a mensagem
        print("  A fila de reservas esta vazia.")
        utils.pausar()
        return
    #retira o primeiro da fila 
    titulo_filme, nome_cliente = dados.fila_de_reservas.pop(0)
    filme = pegar_filme_por_titulo(titulo_filme)

    if filme is not None:
        if filme['status'] == "Indisponivel":
            print(f"\n  [!] O filme '{titulo_filme}' ainda esta alugado.")
            print(f"  A reserva de {nome_cliente} foi mantida na fila.")
                #coloca de volta no inicio da fila
            dados.fila_de_reservas.insert(0, (titulo_filme, nome_cliente))
        else:
            filme['status'] = "Indisponivel"
                  #incrementa o contador de alugueis do filme
            filme['total_alugueis'] += 1

            #incrementa o contador geral de alugueis (faturamento)
            dados.total_alugueis += 1
               #multiplica quantos alugueis foram feitos pelo valor de cada um pra calcular o total ganho 
            faturamento_atual = dados.total_alugueis * dados.VALOR_ALUGUEL

            print(f"\n  [OK] Aluguel realizado com sucesso!")
            utils.linha()
            print(f"  Filme  : {titulo_filme}")
            print(f"  Cliente: {nome_cliente}")
            print(f"  Valor  : R$ {dados.VALOR_ALUGUEL:.2f}")
            utils.linha()
            print(f"  Total de alugueis hoje: {dados.total_alugueis}")
            print(f"  Faturamento acumulado : R$ {faturamento_atual:.2f}")
    utils.pausar()

def ver_fila():
    #mostra quem esta na fila de reservas
    utils.mostrar_titulo("Fila de Reservas")
    if len(dados.fila_de_reservas) == 0:
        print("  A fila esta vazia no momento.")
        utils.pausar()
        return

    print("  Ordem de atendimento:\n")
    posicao = 1
    for titulo, cliente in dados.fila_de_reservas:  #percorre a fila do inicio ate o fim, ai cada volta imprime a posição e soma 1 na posição pra proxima volta
        print(f"  {posicao}. {cliente} -> '{titulo}'")
        posicao += 1
    utils.linha()
    print(f"  Total na fila: {len(dados.fila_de_reservas)} reserva(s)")
    utils.pausar()

#devolução - usa a pilha
#--------------------------------------
'''
Registra a devolucao, muda o status pra disponivel
e empilha no historico
'''
def devolver_filme():
    #registra a devolucao de um filme
    #empilha no historico com .append() que é o mesmo esquema da seresvar_filme()
    utils.mostrar_titulo("Registrar Devolucao")
    titulo = utils.ler_texto("  Nome do filme devolvido: ")
    filme = pegar_filme_por_titulo(titulo) 

    if filme is None:
        print("\n  [!] Filme nao encontrado no sistema.")
        utils.pausar()    #se não achou o filme avisa e sai
        return
    if filme['status'] == "Disponivel":
        print("\n  [!] Esse filme ja esta como disponivel.")
        utils.pausar()    #aqui verifica se o filme esta disponivel, se estiver então ninguem alugou ele
        return
    
    filme['status'] = "Disponivel" #aqui é como se o filme tivese voltado pra pratileira contando diponivel
    cliente = utils.ler_texto("  Nome do cliente que devolveu: ")
    #.append() empilha no topo (lifo)
    dados.historico_devolucoes.append({
        'titulo': filme['titulo'],
        'cliente': cliente,
        'numero': len(dados.historico_devolucoes) + 1
    })
    print(f"\n  [OK] Devolucao registrada!")
    print(f"  '{filme['titulo']}' esta disponivel de novo.")
    utils.pausar()

def ver_historico():
    #mostra o historico de devolucoes do mais recente pro mais antigo
    #reversed() le a pilha de cima pra baixo (a lifo)
    utils.mostrar_titulo("Historico de Devolucoes")

    if len(dados.historico_devolucoes) == 0:   # a leitura é: se a pilha tiver vazia, avisa e sai
        print("  Ainda não houve nenhuma devolucão.")
        utils.pausar()
        return
    print("  Os mais recentes: \n")
    #reversed() percorre do ultimo pro primeiro (do topo da pilha pra baixo)
    contador = 1
    for registro in reversed(dados.historico_devolucoes):
        print(f"  {contador}. '{registro['titulo']}' devolvido por {registro['cliente']}")
        contador += 1

    utils.linha()
    print(f"  Total de devolucoes: {len(dados.historico_devolucoes)}")
    utils.pausar()

#faturamento
#------------------------------------------------
'''
Aqui mostra o total de alugueis feitos, o valor de um só é o total acumulado
também mostra os filmes que ja foram alugados pelo menos uma vez e os que não sairam ainda 
é o painel de controle da locadora
'''
def ver_faturamento():
    #mostra o resumo de movimentacoes e faturamento da locadora
    utils.mostrar_titulo("Resumo de Faturamento")

    print(f"  Total de alugueis realizados : {dados.total_alugueis}")
    print(f"  Valor por aluguel            : R$ {dados.VALOR_ALUGUEL:.2f}")  # o :.2f serve pra mostrar com duas casas decimais
    print(f"  Faturamento total            : R$ {dados.total_alugueis * dados.VALOR_ALUGUEL:.2f}")
    utils.linha()

    if len(dados.lista_filmes) == 0:
        print("  Nenhum filme cadastrado ainda.")
        utils.pausar()
        return
    print("  Filmes mais alugados:\n")
    posicao = 1
    nunca_alugados = 0               #começa zerado
    for f in dados.lista_filmes:
        if f['total_alugueis'] > 0:
            print(f"  {posicao}. {f['titulo']} — {f['total_alugueis']} aluguel(is)")
            posicao += 1
        else:
            nunca_alugados += 1    #conta os que nunca foram alugados

    if posicao == 1:
        print("  Nenhum filme foi alugado ainda.")
    elif nunca_alugados > 0:                  #só aparece se tiver algum
        print(f"\n  ({nunca_alugados} filme(s) nunca foram alugados)")
    utils.pausar()

#função de suporte
#-------------------------------------------
'''
ele usa a lista de filmes para procurar um que tenha aquele titulo (ignorando letras maiusculas ou minusculas)
 e retorna com o dicionario completo do filme se achar ou None se não achar
'''
def pegar_filme_por_titulo(titulo):                    #procura um filme pelo titulo e retorna o dicionario dele
    for filme in dados.lista_filmes:                      #retorna None se nao achar
        if filme['titulo'].lower() == titulo.lower():
            return filme
    return None
