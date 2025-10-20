# -*- coding: utf-8 -*-

from collections import deque
from typing import List, Tuple

# Alunos: Davi Henrique Moreira, Matheus Brehm

def simular_fifo(sequencia: List[int], quadros: int) -> List[int]:
    memoria = [None] * quadros
    fila_indices = deque()
    for pagina in sequencia:
        if pagina in memoria:
            continue
        if None in memoria:
            pos = memoria.index(None)
            memoria[pos] = pagina
            fila_indices.append(pos)
        else:
            pos = fila_indices.popleft()
            memoria[pos] = pagina
            fila_indices.append(pos)
    return memoria

def simular_lru(sequencia: List[int], quadros: int) -> List[int]:
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
                pagina_lru = min(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_lru)
                del ultima_vez_usado[pagina_lru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

def simular_mru(sequencia: List[int], quadros: int) -> List[int]:
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
                pagina_mru = max(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_mru)
                del ultima_vez_usado[pagina_mru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria

def posicao_da_pagina(memoria: List[int], pagina: int) -> int:
    return memoria.index(pagina) + 1

def fifo_faltas(sequencia: List[int], quadros: int) -> Tuple[List[int], int]:
    memoria = [None] * quadros
    fila_indices = deque()
    faltas = 0
    for pagina in sequencia:
        if pagina in memoria:
            continue
        faltas += 1
        if None in memoria:
            pos = memoria.index(None)
            memoria[pos] = pagina
            fila_indices.append(pos)
        else:
            pos = fila_indices.popleft()
            memoria[pos] = pagina
            fila_indices.append(pos)
    return memoria, faltas

def lru_faltas(sequencia: List[int], quadros: int) -> Tuple[List[int], int]:
    memoria = [None] * quadros
    ultima_vez_usado = {}
    tempo = 0
    faltas = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            ultima_vez_usado[pagina] = tempo
        else:
            faltas += 1
            if None in memoria:
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                pagina_lru = min(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_lru)
                del ultima_vez_usado[pagina_lru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria, faltas

def mru_faltas(sequencia: List[int], quadros: int) -> Tuple[List[int], int]:
    memoria = [None] * quadros
    ultima_vez_usado = {}
    tempo = 0
    faltas = 0
    for pagina in sequencia:
        tempo += 1
        if pagina in memoria:
            ultima_vez_usado[pagina] = tempo
        else:
            faltas += 1
            if None in memoria:
                pos = memoria.index(None)
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
            else:
                pagina_mru = max(ultima_vez_usado, key=ultima_vez_usado.get)
                pos = memoria.index(pagina_mru)
                del ultima_vez_usado[pagina_mru]
                memoria[pos] = pagina
                ultima_vez_usado[pagina] = tempo
    return memoria, faltas

if __name__ == "__main__":
    seq_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
    seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
    seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,12,15,6,11]
    quadros = 8

    _, fa_fifo = fifo_faltas(seq_a, quadros)
    _, fa_lru  = lru_faltas(seq_a, quadros)
    _, fa_mru  = mru_faltas(seq_a, quadros)

    _, fb_fifo = fifo_faltas(seq_b, quadros)
    _, fb_lru  = lru_faltas(seq_b, quadros)
    _, fb_mru  = mru_faltas(seq_b, quadros)

    _, fc_fifo = fifo_faltas(seq_c, quadros)
    _, fc_lru  = lru_faltas(seq_c, quadros)
    _, fc_mru  = mru_faltas(seq_c, quadros)

    print("Faltas (seq a) -> FIFO:", fa_fifo, "LRU:", fa_lru, "MRU:", fa_mru)
    print("Faltas (seq b) -> FIFO:", fb_fifo, "LRU:", fb_lru, "MRU:", fb_mru)
    print("Faltas (seq c) -> FIFO:", fc_fifo, "LRU:", fc_lru, "MRU:", fc_mru)

    totais = {
        "FIFO": fa_fifo + fb_fifo + fc_fifo,
        "LRU":  fa_lru  + fb_lru  + fc_lru,
        "MRU":  fa_mru  + fb_mru  + fc_mru
    }
    print("Faltas (total) ->", totais)
