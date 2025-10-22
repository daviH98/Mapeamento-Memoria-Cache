# -*- coding: utf-8 -*-
"""
TDE 2 – Mapeamento de Memória Cache
Autores: Matheus Brehm, Davi Henrique

Este programa simula três políticas de substituição de páginas:
- FIFO: a primeira que entra é a primeira que sai.
- LRU: remove a página que ficou mais tempo sem ser usada.
- MRU: remove a página usada mais recentemente.
"""

from collections import deque
from typing import List

# Simulação do algoritmo FIFO
def simular_fifo(sequencia: List[int], quadros: int) -> List[int]:
    # Cria a memória com o número de quadros desejado
    memoria = [None] * quadros
    fila_indices = deque()  # Guarda a ordem das páginas que entraram
    for pagina in sequencia:
        if pagina in memoria:
            # Se a página já está na memória, não faz nada
            continue
        if None in memoria:
            # Se ainda há espaço vazio, adiciona a página
            pos = memoria.index(None)
            memoria[pos] = pagina
            fila_indices.append(pos)
        else:
            # Se não há espaço, remove a mais antiga e coloca a nova
            pos = fila_indices.popleft()
            memoria[pos] = pagina
            fila_indices.append(pos)
    return memoria

# Simulação do algoritmo LRU
def simular_lru(sequencia: List[int], quadros: int) -> List[int]:
    memoria = [None] * quadros
    ultima_vez_usado = {}  # Guarda o "tempo" da última vez que cada página foi usada
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            # Atualiza o tempo de uso da página
            ultima_vez_usado[pagina] = tempo
        else:
            if None in memoria:
                # Coloca a página em um espaço livre
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                # Encontra a página que está há mais tempo sem ser usada
                pagina_lru = min(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_lru)
                del ultima_vez_usado[pagina_lru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

# Simulação do algoritmo MRU
def simular_mru(sequencia: List[int], quadros: int) -> List[int]:
    memoria = [None] * quadros
    ultima_vez_usado = {}
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            # Atualiza o tempo da página mais recente
            ultima_vez_usado[pagina] = tempo
        else:
            if None in memoria:
                # Adiciona página se ainda há espaço
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                # Remove a página usada mais recentemente
                pagina_mru = max(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_mru)
                del ultima_vez_usado[pagina_mru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

# Função que retorna o número do quadro onde está a página procurada
def posicao_da_pagina(memoria: List[int], pagina: int) -> int:
    pos = memoria.index(pagina)
    return pos + 1  # +1 para o quadro começar a contar do 1 e não do 0

# Executa os testes com as três políticas
def executar_teste(sequencias, quadros: int):
    resultados = {}
    for etiqueta, seq in sequencias.items():
        memoria_fifo = simular_fifo(seq, quadros)
        memoria_lru  = simular_lru(seq, quadros)
        memoria_mru  = simular_mru(seq, quadros)
        resultados[etiqueta] = {
            "FIFO": memoria_fifo,
            "LRU":  memoria_lru,
            "MRU":  memoria_mru,
        }
    return resultados

# Parte principal do programa
if __name__ == "__main__":
    # As três sequências pedidas na atividade
    seq_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
    seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
    seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
    sequencias = {"a": seq_a, "b": seq_b, "c": seq_c}

    resultados = executar_teste(sequencias, quadros=8)

    for etiqueta, mapas in resultados.items():
        print(f"\nSequência {etiqueta}:")
        for alg, mem in mapas.items():
            print(f"  {alg:>4} => {mem}")
            if etiqueta == "a":
                pagina = 7
            elif etiqueta == "b":
                pagina = 11
            else:
                pagina = 11
            try:
                quadro = posicao_da_pagina(mem, pagina)
                print(f"     Página {pagina} está no quadro {quadro}")
            except ValueError:
                print(f"     Página {pagina} não está na memória")

    print("\nMelhor política: normalmente a LRU, pois mantém as páginas mais usadas recentemente.")
