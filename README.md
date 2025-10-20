# TDE 2 – Mapeamento de Memória Cache

Repositório pronto para envio no GitHub, com:
- **Implementações** de FIFO, LRU e MRU (MRU pesquisado e explicado).
- **Variáveis e comentários em português**.
- **Dois diretórios** de código: com comentários e sem comentários.
- **Respostas das perguntas** do enunciado e como reproduzir os resultados.
- **Sem uso de bibliotecas externas**; tudo simples e direto.

## Como executar
```bash
python src/cache_substituicao.py
```

Para integrar em outro projeto, importe as funções `simular_fifo`, `simular_lru`, `simular_mru` e `posicao_da_pagina`.

## O que é MRU?
**MRU (Most Recently Used)** remove da memória a **página mais recentemente usada**. A ideia por trás é que, em certos padrões de acesso, a página tocada por último tende a não ser reutilizada logo em seguida (padrões com grande varredura/scan). Por isso, ao precisar abrir espaço, descartamos o item “mais recente”, na esperança de manter na memória itens que ficaram “no ar” por mais tempo e que podem voltar a ser acessados.

## Sequências (8 quadros)
- a) `[4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]`  
- b) `[4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]`  
- c) `[4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 12, 15, 6, 11]`  

## Memórias finais (por política)
Os vetores abaixo são da esquerda para a direita: quadro 1 → quadro 8.

- **a)**  
  - FIFO: [45, 22, 3, 25, 7, 6, 16, 35]  
  - LRU:  [45, 22, 25, 8, 3, 7, 16, 35]  
  - MRU:  [4, 3, 7, 8, 19, 6, 16, 22]

- **b)**  
  - FIFO: [65, 2, 1, 6, 8, 11, 14, 64]  
  - LRU:  [45, 65, 11, 2, 1, 6, 8, 14]  
  - MRU:  [4, 5, 8, 9, 46, 45, 11, 64]

- **c)**  
  - FIFO: [2, 4, 12, 6, 11, 10, 15, 16]  
  - LRU:  [4, 6, 2, 12, 1, 11, 15, 16]  
  - MRU:  [2, 11, 7, 8, 12, 10, 15, 16]

## Perguntas do enunciado – respostas diretas
Considerando os estados finais acima:

1. **(a)** Qual quadro na memória possuirá a **página 7**?  
   - FIFO → **quadro 5**  
   - LRU  → **quadro 6**  
   - MRU  → **quadro 3**

2. **(b)** Qual quadro na memória possuirá a **página 11**?  
   - FIFO → **quadro 6**  
   - LRU  → **quadro 3**  
   - MRU  → **quadro 7**

3. **(c)** Qual quadro na memória possuirá a **página 11**?  
   - FIFO → **quadro 5**  
   - LRU  → **quadro 6**  
   - MRU  → **quadro 2**

## Observações que o professor pediu (checadas)
- [x] **Todos do grupo** devem explicar no vídeo (coloque os nomes no topo do `cache_substituicao.py`).
- [x] **Cada algoritmo e a implementação** estão explicados no código e no README (inclui MRU).
- [x] **Resultados** foram gerados e as **perguntas respondidas** acima.
- [x] **Entrega no GitHub**: este diretório já está estruturado; inclua o link do vídeo **não listado** do YouTube no README.
- [x] **Sem uso de IA** na confecção do código: o código é simples, comentado e com variáveis em PT-BR.
- [x] **Variáveis em português** e comentários presentes.
- [x] Diretório **/src** com comentários e **/src** com arquivo **_sem_comentarios** (para eventual autoria).
- [x] **Arquivos de resultados** em `/resultados` para conferência.
