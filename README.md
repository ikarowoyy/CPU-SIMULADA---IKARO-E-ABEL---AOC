# CPU Simulada de 8 Bits em Python

Projeto prático da disciplina de **Arquitetura e Organização de Computadores (AOC)**  
**Universidade Federal do Ceará (UFC) – Campus Sobral**  
**Docente:** Prof. Wendley S. Silva

---

## 1. Visão Geral da Arquitetura

O projeto consiste na implementação de uma CPU didática de 8 bits em Python, integrando em um único modelo funcional os conceitos de **Unidade Lógica e Aritmética (ULA)**, **Registradores**, **Memória Principal**, **Instruções** e o ciclo fundamental de processamento **Busca (Fetch) → Decodificação (Decode) → Execução (Execute)**.

### Especificações Técnicas:
- **Tamanho dos Dados:** 8 bits (valores delimitados estritamente na faixa `0` a `255` via máscara `& 0xFF`).
- **Registradores Gerais:** 4 registradores de 8 bits (`R0`, `R1`, `R2`, `R3`).
- **Contador de Programa (PC):** Registrador que indica o endereço de memória da próxima instrução a ser buscada.
- **Memória Principal:** 16 posições indexadas de `0` a `15` (suportando instruções e dados).
- **Unidade de Controle:** Responsável por decodificar as instruções e orquestrar as transições de estado da máquina.
- **ULA (Unidade Lógica e Aritmética):** Executa operações aritméticas e lógicas:
  - `ADD`: Adição ($R_d \leftarrow R_d + R_s$)
  - `SUB`: Subtração ($R_d \leftarrow R_d - R_s$)
  - `AND`: Operação lógica E bit a bit ($R_d \leftarrow R_d \ \& \ R_s$)
  - `OR`: Operação lógica OU bit a bit ($R_d \leftarrow R_d \ | \ R_s$)
  - `XOR`: Operação lógica OU-Exclusivo bit a bit ($R_d \leftarrow R_d \ \oplus \ R_s$)

---

## 2. Conjunto de Instruções

| Instrução | Formato / Sintaxe | Descrição / Efeito |
|---|---|---|
| **LOAD** | `LOAD Rd, valor` | Carrega o valor imediato de 8 bits no registrador `Rd`. Incrementa o PC em 1. |
| **STORE** | `STORE Rd, endereco` | Grava o valor armazenado em `Rd` na posição `endereco` (0-15) da memória. Incrementa o PC em 1. |
| **ADD** | `ADD Rd, Rs` | $Rd \leftarrow (Rd + Rs) \pmod{256}$. Incrementa o PC em 1. |
| **SUB** | `SUB Rd, Rs` | $Rd \leftarrow (Rd - Rs) \pmod{256}$. Incrementa o PC em 1. |
| **AND** | `AND Rd, Rs` | $Rd \leftarrow (Rd \ \& \ Rs)$. Incrementa o PC em 1. |
| **OR** | `OR Rd, Rs` | $Rd \leftarrow (Rd \ \| \ Rs)$. Incrementa o PC em 1. |
| **XOR** | `XOR Rd, Rs` | $Rd \leftarrow (Rd \ \oplus \ Rs)$. Incrementa o PC em 1. |
| **JMP** | `JMP endereco` | Desvio incondicional: $PC \leftarrow endereco$. |
| **HALT** | `HALT` | Sinaliza o término da execução da CPU (`halted = True`). |

---

## 3. Ciclo de Instrução (Fetch → Decode → Execute)

A cada ciclo:
1. **Fetch (Busca):** A CPU busca a instrução na memória na posição apontada pelo registrador `PC` (`instrucao = memoria[PC]`).
2. **Decode (Decodificação):** O mnemônico da operação e seus operandos são isolados e validados.
3. **Execute (Execução):** A operação correspondente é processada na ULA ou na Unidade de Controle, atualizando os registradores, a memória ou o `PC`.

---

## 4. Programas Implementados

### 4.1. Programa de Exemplo (Seção 7 do Enunciado)
Calcula a soma $5 + 8$ e salva o resultado na posição 15 da memória:
```assembly
[00] LOAD R0, 5     ; R0 = 5
[01] LOAD R1, 8     ; R1 = 8
[02] ADD R0, R1     ; R0 = 5 + 8 = 13 (0x0D)
[03] STORE R0, 15   ; MEM[15] = 13
[04] HALT           ; Encerra
```
**Resultado Esperado:** `MEM[15] = 13`.

### 4.2. Programa Próprio (Seção 11 do Enunciado)
Calcula a expressão multietapas $((A + B) - C) \oplus D$, com $A=20$, $B=15$, $C=10$ e $D=7$, utilizando 10 instruções (superior ao mínimo de 8 exigido), com instruções `LOAD`, `STORE` e três operações de ULA (`ADD`, `SUB`, `XOR`):
```assembly
[00] LOAD R0, 20    ; R0 = 20
[01] LOAD R1, 15    ; R1 = 15
[02] ADD R0, R1     ; R0 = 20 + 15 = 35 (0x23)
[03] STORE R0, 14   ; MEM[14] = 35 (salva resultado intermediário)
[04] LOAD R2, 10    ; R2 = 10
[05] SUB R0, R2     ; R0 = 35 - 10 = 25 (0x19)
[06] LOAD R3, 7     ; R3 = 7
[07] XOR R0, R3     ; R0 = 25 ^ 7 = 30 (0x1E)
[08] STORE R0, 15   ; MEM[15] = 30 (salva resultado final)
[09] HALT           ; Encerra execução
```
**Resultados Finais:** `MEM[14] = 35`, `MEM[15] = 30`, `R0 = 30`.

---

## 5. Estrutura dos Arquivos

```text
├── ula.py          # Operações aritméticas e lógicas e limitação de 8 bits
├── cpu.py          # Classe principal da CPU, registradores, memória e ciclo
├── programas.py    # Definição dos programas de teste em Assembly simplificado
├── testes.py       # Bateria de testes automatizados (unittest)
├── main.py         # Demonstração visual passo a passo dos programas
└── README.md       # Documentação completa da arquitetura e instruções
```

---

## 6. Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Executando a Demonstração Passo a Passo:
```bash
python3 main.py
```

### Executando os Testes Automatizados:
```bash
python3 testes.py
```
Todos os 11 testes unitários cobrem integralmente os 10 requisitos da Seção 12 do enunciado.
