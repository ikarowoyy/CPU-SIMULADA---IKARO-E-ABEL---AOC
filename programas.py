"""
Módulo Programas
Contém os programas em Assembly simplificado para a CPU simulada de 8 bits.
"""

# ==============================================================================
# PROGRAMA 1: Programa de Exemplo (Seção 7 do Enunciado)
# Objetivo: Calcular 5 + 8 e armazenar o resultado 13 na posição 15 da memória.
# ==============================================================================
PROGRAMA_EXEMPLO = [
    "LOAD R0, 5",      # [00] R0 <- 5
    "LOAD R1, 8",      # [01] R1 <- 8
    "ADD R0, R1",      # [02] R0 <- R0 + R1 (5 + 8 = 13)
    "STORE R0, 15",    # [03] MEM[15] <- R0 (13)
    "HALT"             # [04] Encerra execução
]

# ==============================================================================
# PROGRAMA 2: Programa Próprio (Seção 11 do Enunciado)
# Requisitos:
# - Pelo menos 8 instruções (possui 10 instruções).
# - Utilização obrigatória de LOAD e STORE.
# - Utilização de pelo menos duas operações da ULA (utiliza ADD, SUB e XOR).
#
# Descrição:
# Realiza o cálculo da expressão: ((A + B) - C) XOR D
# com A = 20, B = 15, C = 10, D = 7.
# 1. Carrega A (20) em R0 e B (15) em R1.
# 2. Soma R0 e R1 (20 + 15 = 35) e salva o resultado intermediário em MEM[14].
# 3. Carrega C (10) em R2 e subtrai de R0 (35 - 10 = 25).
# 4. Carrega D (7) em R3 e aplica a operação lógica XOR com R0 (25 ^ 7 = 30).
# 5. Salva o resultado final (30) em MEM[15] e finaliza.
# ==============================================================================
PROGRAMA_PROPRIO = [
    "LOAD R0, 20",     # [00] Carrega o valor imediato 20 em R0
    "LOAD R1, 15",     # [01] Carrega o valor imediato 15 em R1
    "ADD R0, R1",      # [02] R0 <- R0 + R1 (20 + 15 = 35)
    "STORE R0, 14",    # [03] Grava o resultado intermediário (35) em MEM[14]
    "LOAD R2, 10",     # [04] Carrega o valor imediato 10 em R2
    "SUB R0, R2",      # [05] R0 <- R0 - R2 (35 - 10 = 25)
    "LOAD R3, 7",      # [06] Carrega a máscara lógica 7 em R3
    "XOR R0, R3",      # [07] R0 <- R0 ^ R3 (25 ^ 7 = 30)
    "STORE R0, 15",    # [08] Grava o resultado final (30) em MEM[15]
    "HALT"             # [09] Encerra o processamento
]
