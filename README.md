# Sistema de locadora de filmes

tema: locadora de filmes
disciplina: programação de computadores
alunos: marcelo, ana, daniel 
periodo/turma: 1 semetre - analise e desenvolvimento de 

## 1. Descrição do projeto
O projeto é sobre um sistema de locadora de filmes que roda pelo terminal. Nele dá pra cadastrar filmes, ver catálogo, reservar, alugar e devolver.
O sistema também tem um contador de movimentações que calcula o faturamento da locadora. Usamos também os conceitos de fila, pilha, dicionário, lista e tupla.

## 2. Explicação

### Fila (fifo)
A fila funciona tipo fila de lojas, quem chega primeiro vai ser atendido primeiro. No nosso sistema a gente usa a fila_de_reservas pra guardar os clientes que querem alugar o filme. Quando alguém reserva, entra no final com .append(). Na hora de processar o aluguel, a gente usa .pop(0) que tira o primeiro da fila, que é quem estava esperando há mais tempo.

```
#cliente entra no final da fila
dados.fila_de_reservas.append((filme['titulo'], cliente))

#pega o primeiro da fila pra alugar (FIFO)
titulo_filme, nome_cliente = dados.fila_de_reservas.pop(0)
```

### Pilha (lifo)
A pilha pode ser comparada com uma pilha de pratos, o último que entra é o primeiro que sai. A gente usa o historico_devolucoes pra guardar as devoluções e cada devolução é empilhada com .append(). Pra mostrar do mais recente pro mais antigo a gente usa o reversed().

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

### Dicionario
Cada filme é salvo como um dicionário que guarda os dados em formato de chave e valor. Dessa forma dá pra acessar qualquer dado do filme pelo nome, tipo filme['titulo'] ou filme['status']. Também colocamos o campo total_alugueis dentro do dicionário de cada filme pra saber quantas vezes cada título foi alugado.

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

### Lista e tupla
A lista a gente usa quando os dados precisam mudar, aí dá pra adicionar e remover itens. Já a tupla não pode mudar porque os valores são fixos. Usamos a lista pra guardar os filmes, a fila e o histórico porque esses dados mudam. Usamos tupla pra guardar os status e gêneros possíveis porque esses valores não devem mudar.

```
#tupla: nao pode alterar, valores fixos
status_possiveis = ("Disponivel", "Indisponivel")
generos_possiveis = ("Acao", "Comedia", "Drama", ...)

#lista: pode adicionar e tirar
lista_filmes = []
lista_filmes.append(novo_filme)
```

### Modularização
A gente dividiu o projeto em 4 arquivos. O dados.py é onde ficam as variáveis compartilhadas entre os arquivos, tipo a lista de filmes, a fila, a pilha, as tuplas e os contadores de faturamento. O tarefas.py tem as funções principais do sistema como cadastrar, listar, alugar, devolver e ver faturamento. O utils.py fica a parte do design, onde mostra o menu e faz a leitura das entradas do usuário. O main.py é o arquivo principal, o ponto de entrada que tem o while True do menu pra chamar as outras funções.

### 3. Como rodar
 - precisa ter o a versão python 3.10 ou mais recente
 - comando para executar: python mains.py
 - não são nescesarias blibiotecas externas 

 ## 4. Funcionalidades
- Cadastrar filme com título, gênero, ano e status
- Ver catálogo com status de cada filme
- Fila de reservas FIFO
- Pilha de devolucoes LIFO
- alugar filme (muda status pra Indisponivel)
- devolver filme (muda status pra Disponivel)
extra
- Buscar filme pelo nome
- Ver filmes disponíveis por gênero
- Histórico de devoluções com contador de posição
- Contador de movimentacoes e faturamento da locadora

## 5. Dificuldades e Aprendizados
No começo a maior dificuldade foi entender como o FIFO e o LIFO funcionavam de verdade no código. A gente sabia a teoria mas ficou confuso na hora de usar. O .pop() e o .pop(0) também causaram uma grande confusão pra gente, porque são parecidos mas fazem coisas diferentes: sem o zero tira o último elemento e com o zero tira o primeiro. Erramos isso algumas vezes antes de entender. Outra dificuldade foi separar o código em 4 arquivos sem misturar as coisas. Ficamos na dúvida várias vezes sobre onde colocar cada função, mas com o tempo foi ficando mais fácil. Aprendemos bastante sobre organizar um projeto maior do que um arquivo só, entendemos melhor quando usar lista e quando usar tupla, e a organização geral do código que no começo era bem complicada porque as funções se misturavam e ficava difícil saber o que cada uma fazia no sistema.


SISTEMA DE LOCADORA DE FILMES
==============================
```
                    [INICIO]
                       |
                       v
               +---------------+
               |    main.py    |
               |  exibe menu   |
               +---------------+
                       |
       +---------------+---------------+
       |               |               |
       v               v               v
  [FILMES]        [RESERVAS]      [DEVOLUCOES]
       |               |               |
  cadastrar        reservar         devolver
  listar           ver fila         historico
  buscar           processar
  por genero       aluguel
       |               |               |
       +-------+-------+-------+-------+
                       |
                       v
               +---------------+
               |  [RELATORIO]  |
               |  faturamento  |
               +---------------+
                       |
                       v
               usuario digitou 0?
               /               \
             nao               sim
              |                 |
              v                 v
           [MENU]            [FIM]



------------------------------------------------------
ESTRUTURA DE ARQUIVOS
------------------------------------------------------

main.py ---------> tarefas.py --> dados.py
      \                              (listas, filas,
       \-> utils.py                   pilha, constantes)
          (inputs, prints, menus)
```
