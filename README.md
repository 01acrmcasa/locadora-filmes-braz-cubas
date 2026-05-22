# sistema de locadora de filmes

tema: locadora de filmes
disciplina: programação de computadores
alunos: marcelo, ana clara, daniel - grupo 4
periodo/turma: 1 semetre - analise e desenvolvimento de sistemas 

## 1. descrição do projeto
o projeto é sobre um sistema de locadora de filmes que roda pelo terminal, nele da pra cadastrar filmes, ver catálogo, reservar, alugar e devolver.
o sistema tambem tem um contador de movimentações que calcula o faturamento da da locadora, usamos tambem o os conceitos de fila, pilha, discionario, lista e tupla

## 2. explicação

### fila (fifo)
a fila funciona tipo fila de lojas, quem chega primeiro vai ser atendido primeiro, no nosso sistema a gente usa a 'fila_de_reservas' pra guardar os clientes que querem alugar o filme, quando alguém reserva ai entra no final com '.append().'. ai na hora de processar o aluguel, a gente usa .pop(0) que tira o primeiro da fila, que é quem estava esperando a mais tempo

```
#cliente entra no final da fila
dados.fila_de_reservas.append((filme['titulo'], cliente))

#pega o primeiro da fila pra alugar (FIFO)
titulo_filme, nome_cliente = dados.fila_de_reservas.pop(0)
```

### pilha (lifo)
a pilha pode comparar com uma pilha de pratos, o ultimo que entra é o primeiro que sai, a gente usa o 'historico_devolucoes' pra guardar as devoluçoes e cada devolução é empilhada com '.append()'. pra mostrar do mais recente pro mais antigo a gente usa o 'reversed()'

```
#empilha a devolucao no topo
dados.historico_devolucoes.append({
    'titulo': filme['titulo'],
    'cliente': cliente,
    'numero': len(dados.historico_devolucoes) + 1
})

#le do topo pra baixo com reversed() (LIFO)
for registro in reversed(dados.historico_devolucoes):
    print(f"  '{registro['titulo']}' devolvido por {registro['cliente']}")
```

### discionario
cadas filme é salvo como um dicionário que guarda os dados em formato de chave ou valor, e desse jeito da pra acessar qualquer dados do filme pelo nome, tipo  'filme['titulo']` ou `filme['status']`, tambem colocamos o campos 'total_alugueis' dentro do dicionário de cada filme pra saber quantas vezes cada titulo foi alugado

```
novo_filme = {
    'id': dados.contador_id,
    'titulo': titulo,
    'genero': genero,
    'ano': ano,
    'status': 'Disponivel',
    'total_alugueis': 0
}
```

### lista e tupla
a lista a gente usa quando os dados precisa mudar que ai da pra adicionar e remover os itens, ja a tupla não pode mudar por que são fixos, nos usamos a lista pra guardar os filmes, a fila e o histórico por que esses dados mudam, usamos tupla pra guardar os status e gêneros possiveis por que esses valores não devem mudar

```
#tupla: nao pode alterar, valores fixos
status_possiveis = ("Disponivel", "Indisponivel")
generos_possiveis = ("Acao", "Comedia", "Drama", ...)

#lista: pode adicionar e tirar
lista_filmes = []
lista_filmes.append(novo_filme)
```

### modularização
a gente dividiu o projeto em 4 arquivos: o dados,py é onde fica as variaveis compartilhadas entre os arquivos, tipo a lista de filmes e os contadores, a fila, a pilha, as tuplas e os contadores de faturamento, o tarefas.py tem as funçoes principais do sistema como cadastrar, listar, alugar, devolver e ver faturamento, o utils.py fica a parte do design onde mostra o menu, leitura de dados e ler as entradas do usuario, o main.py e o arquivo principal tipo o ponto de entrada que tem o while True do menu pra chamar as outras funcoes

### 3. como rodar
 - precisa ter o a versão python 3.10 ou mais recente
 - comando para executar: python main.py
 - não são nescesarias blibiotecas externas 

 ## 4. funcionalidades
 - Cadastrar filme com titulo, gênero, ano e status
- ver catalogo com status de cada filme
- Fila de reservas FIFO
- Pilha de devolucoes LIFO
- alugar filme (muda status pra Indisponivel)
- devolver filme (muda status pra Disponivel)
extra
- Buscar filme pelo nome
- ver filmes disponiveis por genero
- Historico de devolucoes com contador de posicao
- Contador de movimentacoes e faturamento da locadora

## 5. Dificuldades e Aprendizados
No começo a maior dificuldade foi entender como o fifo e o lifo funcionavam de verdade no código, a gente sabia a teoria mas ficou confuso na hora de usar, o `.pop()` e o `.pop(0)` tambem causou uma grande confusão pra nós, porque são parecidos mas fazem coisas diferentes, sem o zero tira o ultimo elemento e com o zero tira o primeiro, erramos isso algumas vezes antes de entender, outra dificuldade foi separar o codigo em 4 arquivos sem misturar as coisas, ficamos na duvida varias vezes sobre onde colocar cada função, ai com o tempo foi ficando mais facil de entender, Aprendemos bastante sobre organizar um projeto maior do que um arquivo so e também entendemos melhor quando usar lista e quando usar tupla, e tambem a dificuldade na organização do codigo foi bem complicada pois as linhas se misturavam e nos não conseguimos separar as funções, tipo o que aquela função faz no sistema, acabava tambem misturando então foi a nossa maior dificuldade


SISTEMA DE LOCADORA DE FILMES
==============================

                          [INICIO]
                              |
                              v
                      +--------------+
                      | main.py      |
                      | exibe menu   |
                      +--------------+
                              |
          .-------------------+-------------------.
          |          |          |         |        |
          v          v          v         v        v
      [FILMES]   [RESERVAS] [ALUGUEIS] [DEVOLUC] [RELAT]
          |          |          |         |        |
     cadastrar   reservar   processar  devolver  faturamento
      listar      ver fila   aluguel   historico
      buscar
      genero
          |          |          |         |        |
          '-------------------+-------------------'
                              |
                              v
                    usuario digitou 0?
                      |           |
                     nao          sim
                      |           |
                      v           v
                  [MENU]        [FIM]


------------------------------------------------------
ESTRUTURA DE ARQUIVOS
------------------------------------------------------

  main.py ---------> tarefas.py --> dados.py
      \                              (listas, filas,
       \-> utils.py                   pilha, constantes)
          (inputs, prints, menus)
