
# -*- coding: utf-8 -*-
"""
TDE 2 – Mapeamento de Memória Cache

- FIFO (First-In, First-Out)
- LRU  (Least Recently Used)
- MRU  (Most Recently Used)

Autores: Matheus Brehm, Davi Henrique

"""

from collections import deque
from typing import List, Tuple

def simular_fifo(sequencia: List[int], quadros: int) -> List[int]:
    """Simula FIFO com 'quadros' posições de memória."""
    memoria = [None] * quadros
    fila_indices = deque()  # guarda a ordem de ocupação dos slots
    for pagina in sequencia:
        if pagina in memoria:
            # acerto: nada a fazer
            continue
        # falta de página
        if None in memoria:
            pos = memoria.index(None)
            memoria[pos] = pagina
            fila_indices.append(pos)
        else:
            # remove o mais antigo (o que entrou primeiro)
            pos = fila_indices.popleft()
            memoria[pos] = pagina
            fila_indices.append(pos)
    return memoria

def simular_lru(sequencia: List[int], quadros: int) -> List[int]:
    """Simula LRU: remove quem ficou há mais tempo sem uso."""
    memoria = [None] * quadros
    ultima_vez_usado = {}  # mapeia pagina -> "tempo lógico" do último acesso
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            # acerto: apenas atualiza a "idade"
            ultima_vez_usado[pagina] = tempo
        else:
            # falta
            if None in memoria:
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                # encontra a página menos recentemente usada
                pagina_lru = min(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_lru)
                del ultima_vez_usado[pagina_lru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

def simular_mru(sequencia: List[int], quadros: int) -> List[int]:
    """
    Simula MRU: remove a página MAIS recentemente usada.
    Por que faz sentido? Em cenários onde acessos tendem a "pular" para novas regiões,
    a página usada por último tem alta chance de não ser reutilizada tão cedo.
    """
    memoria = [None] * quadros
    ultima_vez_usado = {}
    tempo = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            ultima_vez_usado[pagina] = tempo
        else:
            if None in memoria:
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                # remove a MAIS recente
                pagina_mru = max(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_mru)
                del ultima_vez_usado[pagina_mru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

def posicao_da_pagina(memoria: List[int], pagina: int) -> int:
    """Retorna o número do quadro (1..N) que contém 'pagina'. Lança ValueError se não estiver na memória."""
    pos = memoria.index(pagina)  # levanta ValueError se a página não existir
    return pos + 1

def executar_teste(sequencias, quadros: int):
    """Roda as três políticas e devolve um dicionário de resultados finais por sequência."""
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

if __name__ == "__main__":
    # Exemplo rápido: as três sequências do enunciado com 8 quadros
    seq_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
    seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
    seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,12,15,6,11]
    sequencias = {"a": seq_a, "b": seq_b, "c": seq_c}
    resultados = executar_teste(sequencias, quadros=8)
    for etiqueta, mapas in resultados.items():
        print(f"Sequência {etiqueta}:")
        for alg, mem in mapas.items():
            print(f"  {alg:>4} => {mem}")
