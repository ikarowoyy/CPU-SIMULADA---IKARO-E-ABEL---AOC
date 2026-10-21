"""
Módulo de Testes Automatizados (testes.py)
Cobre todos os 10 testes obrigatórios exigidos no enunciado (Seção 12):
1. LOAD coloca corretamente um valor no registrador.
2. STORE grava corretamente um valor na memória.
3. ADD produz resultados corretos.
4. SUB produz resultados corretos.
5. AND, OR e XOR funcionam corretamente.
6. O PC avança corretamente.
7. JMP altera o PC corretamente.
8. HALT interrompe a execução.
9. A CPU executa corretamente o programa de exemplo (MEM[15] == 13).
10. Os resultados respeitam a representação de 8 bits (overflow/underflow & 0xFF).
"""

import unittest
from ula import ULA
from cpu import CPU
from programas import PROGRAMA_EXEMPLO, PROGRAMA_PROPRIO


class TestCPUSimulada(unittest.TestCase):

    def setUp(self):
        self.cpu = CPU()

    # 1. LOAD deve colocar corretamente um valor em um registrador
    def test_01_load(self):
        self.cpu.executar_instrucao("LOAD R0, 42")
        self.assertEqual(self.cpu.registradores["R0"], 42)
        self.cpu.executar_instrucao("LOAD R1, 100")
        self.assertEqual(self.cpu.registradores["R1"], 100)

    # 2. STORE deve gravar corretamente um valor na memória
    def test_02_store(self):
        self.cpu.registradores["R2"] = 77
        self.cpu.executar_instrucao("STORE R2, 10")
        self.assertEqual(self.cpu.memoria[10], 77)

    # 3. ADD deve produzir resultados corretos
    def test_03_add(self):
        self.cpu.registradores["R0"] = 15
        self.cpu.registradores["R1"] = 25
        self.cpu.executar_instrucao("ADD R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 40)

    # 4. SUB deve produzir resultados corretos
    def test_04_sub(self):
        self.cpu.registradores["R0"] = 50
        self.cpu.registradores["R1"] = 20
        self.cpu.executar_instrucao("SUB R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 30)

    # 5. AND, OR e XOR devem funcionar corretamente
    def test_05_logicas(self):
        # AND
        self.cpu.registradores["R0"] = 0b1100
        self.cpu.registradores["R1"] = 0b1010
        self.cpu.executar_instrucao("AND R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 0b1000)

        # OR
        self.cpu.registradores["R0"] = 0b1100
        self.cpu.registradores["R1"] = 0b1010
        self.cpu.executar_instrucao("OR R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 0b1110)

        # XOR
        self.cpu.registradores["R0"] = 0b1100
        self.cpu.registradores["R1"] = 0b1010
        self.cpu.executar_instrucao("XOR R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], 0b0110)

    # 6. O PC deve avançar corretamente
    def test_06_avanco_pc(self):
        self.assertEqual(self.cpu.pc, 0)
        self.cpu.executar_instrucao("LOAD R0, 1")
        self.assertEqual(self.cpu.pc, 1)
        self.cpu.executar_instrucao("LOAD R1, 2")
        self.assertEqual(self.cpu.pc, 2)
        self.cpu.executar_instrucao("ADD R0, R1")
        self.assertEqual(self.cpu.pc, 3)

    # 7. JMP deve alterar o PC corretamente
    def test_07_jmp(self):
        self.cpu.executar_instrucao("JMP 8")
        self.assertEqual(self.cpu.pc, 8)
        self.cpu.executar_instrucao("JMP 14")
        self.assertEqual(self.cpu.pc, 14)

    # 8. HALT deve interromper a execução
    def test_08_halt(self):
        self.assertFalse(self.cpu.halted)
        self.cpu.executar_instrucao("HALT")
        self.assertTrue(self.cpu.halted)

    # 9. A CPU deve executar corretamente o programa de exemplo
    def test_09_programa_exemplo(self):
        self.cpu.carregar_programa(PROGRAMA_EXEMPLO)
        self.cpu.executar(passo_a_passo=False)
        self.assertEqual(self.cpu.memoria[15], 13)
        self.assertEqual(self.cpu.registradores["R0"], 13)
        self.assertTrue(self.cpu.halted)

    # 10. Os resultados devem respeitar a representação de 8 bits
    def test_10_limite_8bits(self):
        # Overflow no LOAD
        self.cpu.executar_instrucao("LOAD R0, 300")
        self.assertEqual(self.cpu.registradores["R0"], 300 & 0xFF)  # 44

        # Overflow na ULA (ADD)
        self.cpu.registradores["R0"] = 250
        self.cpu.registradores["R1"] = 10
        self.cpu.executar_instrucao("ADD R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], (260 & 0xFF))  # 4

        # Underflow na ULA (SUB)
        self.cpu.registradores["R0"] = 5
        self.cpu.registradores["R1"] = 10
        self.cpu.executar_instrucao("SUB R0, R1")
        self.assertEqual(self.cpu.registradores["R0"], (-5 & 0xFF))  # 251

    # Teste extra: Execução completa do Programa Próprio
    def test_11_programa_proprio(self):
        self.cpu.carregar_programa(PROGRAMA_PROPRIO)
        self.cpu.executar(passo_a_passo=False)
        # Verificando resultados:
        # MEM[14] guarda 20 + 15 = 35
        self.assertEqual(self.cpu.memoria[14], 35)
        # MEM[15] guarda (35 - 10) ^ 7 = 25 ^ 7 = 30
        self.assertEqual(self.cpu.memoria[15], 30)
        self.assertEqual(self.cpu.registradores["R0"], 30)
        self.assertTrue(self.cpu.halted)


if __name__ == "__main__":
    unittest.main()
