TDE 2 – Mapeamento de Memória Cache
Alunos: Davi Henrique Moreira e Matheus B.

## O que é MRU?
**MRU (Most Recently Used)** remove da memória a **página mais recentemente usada**. A ideia por trás é que, em certos padrões de acesso, a página tocada por último tende a não ser reutilizada logo em seguida (padrões com grande varredura/scan). Por isso, ao precisar abrir espaço, descartamos o item “mais recente”, na esperança de manter na memória itens que ficaram “no ar” por mais tempo e que podem voltar a ser acessados.


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
