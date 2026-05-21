#aqui fica as variaveis que o sistema usa

#lista com todos os filmes cadastrados
lista_filmes = []
#fila de reservas-primeiro a reservar, primeiro a alugar
fila_de_reservas = []

#pilha de devoluçoes, ultima devolução aparece primeiro
historico_devolucoes = []
#opçoes disponiveis no sistema
status_possiveis = ("Disponivel", "Indisponivel")
generos_possiveis = ("Acao", "Comedia", "Drama", "Terror", "Ficcao Cientifica", "Romance", "Animacao", "Documentario", "Outro")

#contador pra gerar p id de cada filme
contador_id = 1

#contador de movimentação (alugueis feitos) para faturamento
total_alugueis = 0

#valor do aluguel por filme
VALOR_ALUGUEL = 8.50    