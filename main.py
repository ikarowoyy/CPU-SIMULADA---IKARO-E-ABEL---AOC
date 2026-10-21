"""
Módulo Principal (main.py)
Permite executar os programas na CPU Simulada com visualização passo a passo.
"""

from cpu import CPU
from programas import PROGRAMA_EXEMPLO, PROGRAMA_PROPRIO


def executar_com_destaque(nome_programa: str, programa: list):
    print("=" * 50)
    print(f"       EXECUTANDO: {nome_programa}")
    print("=" * 50)
    print("Código carregado na memória:")
    for idx, instr in enumerate(programa):
        print(f"  [{idx:02d}] {instr}")
    print("-" * 50)

    cpu = CPU()
    cpu.carregar_programa(programa)
    cpu.executar(passo_a_passo=True)

    print("\n" + "=" * 50)
    print("       ESTADO FINAL DA MEMÓRIA E CPU")
    print("=" * 50)
    print(f"PC Final: {cpu.pc}")
    print(f"Halted: {cpu.halted}")
    print("Registradores finais:")
    for reg, val in cpu.registradores.items():
        print(f"  {reg}: {val:02X}h ({val})")
    print("\nPosições de Memória modificadas / relevantes:")
    for addr in range(len(cpu.memoria)):
        if isinstance(cpu.memoria[addr], int) and cpu.memoria[addr] != 0:
            print(f"  MEM[{addr:02d}] = {cpu.memoria[addr]} (0x{cpu.memoria[addr]:02X})")
    print("=" * 50 + "\n")


def main():
    print("**************************************************")
    print("    UNIVERSIDADE FEDERAL DO CEARÁ - UFC SOBRAL")
    print("    ARQUITETURA DE COMPUTADORES - CPU SIMULADA")
    print("**************************************************\n")

    # 1. Execução do Programa de Exemplo (Seção 7)
    executar_com_destaque("1. Programa de Exemplo (5 + 8)", PROGRAMA_EXEMPLO)

    # 2. Execução do Programa Próprio (Seção 11)
    executar_com_destaque("2. Programa Próprio (Cálculo Multietapas)", PROGRAMA_PROPRIO)


if __name__ == "__main__":
    main()
