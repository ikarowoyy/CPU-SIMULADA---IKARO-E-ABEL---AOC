"""
Módulo CPU
Implementa a arquitetura didática de 8 bits:
- 4 registradores gerais: R0, R1, R2, R3
- 1 Contador de Programa (PC)
- Memória principal com 16 posições
- Ciclo de instrução: Busca (Fetch) -> Decodificação (Decode) -> Execução (Execute)
"""

from ula import ULA


class CPU:
    def __init__(self):
        # Registradores gerais de 8 bits
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }
        # Memória com 16 posições (índices 0 a 15)
        self.memoria = [0] * 16
        # Contador de Programa (Program Counter)
        self.pc = 0
        # Indicador de término de execução
        self.halted = False

    def limitar_8bits(self, valor: int) -> int:
        """Garante a representação estrita de 8 bits (0 a 255)."""
        return ULA.limitar_8bits(valor)

    def ula(self, operacao: str, a: int, b: int) -> int:
        """Encaminha o cálculo para a Unidade Lógica e Aritmética."""
        return ULA.operar(operacao, a, b)

    def reset(self):
        """Reinicia o estado da CPU."""
        for reg in self.registradores:
            self.registradores[reg] = 0
        self.memoria = [0] * 16
        self.pc = 0
        self.halted = False

    def carregar_programa(self, programa: list):
        """Carrega uma lista de instruções na memória a partir da posição 0."""
        if len(programa) > 16:
            raise ValueError("O programa excede o tamanho da memória (máximo 16 posições).")
        for i, instrucao in enumerate(programa):
            self.memoria[i] = instrucao

    def executar_instrucao(self, instrucao: str):
        """
        Etapa de Decode e Execute.
        Interpreta a instrução e executa a operação correspondente.
        """
        # Normalização removendo vírgulas e separando partes
        partes = instrucao.replace(",", "").split()
        if not partes:
            return

        operacao = partes[0].upper()

        # --------------------------------------------------
        # LOAD: Carrega um valor imediato de 8 bits no registrador
        # Exemplo: LOAD R0, 5
        # --------------------------------------------------
        if operacao == "LOAD":
            registrador = partes[1].upper()
            valor = int(partes[2])
            if registrador not in self.registradores:
                raise ValueError(f"Registrador inválido: {registrador}")
            self.registradores[registrador] = self.limitar_8bits(valor)
            self.pc += 1

        # --------------------------------------------------
        # STORE: Grava o valor de um registrador na memória
        # Exemplo: STORE R0, 15
        # --------------------------------------------------
        elif operacao == "STORE":
            registrador = partes[1].upper()
            endereco = int(partes[2])
            if registrador not in self.registradores:
                raise ValueError(f"Registrador inválido: {registrador}")
            if not (0 <= endereco < 16):
                raise IndexError(f"Endereço de memória fora dos limites (0-15): {endereco}")
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        # --------------------------------------------------
        # Operações da ULA: ADD, SUB, AND, OR, XOR
        # Exemplo: ADD R0, R1 -> R0 <- R0 + R1
        # --------------------------------------------------
        elif operacao in ["ADD", "SUB", "AND", "OR", "XOR"]:
            reg_dest = partes[1].upper()
            reg_orig = partes[2].upper()
            if reg_dest not in self.registradores or reg_orig not in self.registradores:
                raise ValueError(f"Registradores inválidos: {reg_dest}, {reg_orig}")
            val_a = self.registradores[reg_dest]
            val_b = self.registradores[reg_orig]
            self.registradores[reg_dest] = self.ula(operacao, val_a, val_b)
            self.pc += 1

        # --------------------------------------------------
        # JMP: Desvio incondicional
        # Exemplo: JMP 8 -> PC recebe 8
        # --------------------------------------------------
        elif operacao == "JMP":
            endereco = int(partes[1])
            if not (0 <= endereco < 16):
                raise IndexError(f"Endereço de salto inválido (0-15): {endereco}")
            self.pc = endereco

        # --------------------------------------------------
        # HALT: Encerra a execução da CPU
        # --------------------------------------------------
        elif operacao == "HALT":
            self.halted = True
            self.pc += 1

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    def ciclo(self, exibir_passos: bool = True):
        """
        Executa um ciclo completo de instrução:
        1. Fetch (Busca)
        2. Decode & Execute (Decodificação e Execução)
        """
        if self.pc >= 16:
            self.halted = True
            return

        # FETCH: Busca a instrução na posição indicada pelo PC
        instrucao = self.memoria[self.pc]

        if exibir_passos:
            print("\n-----------------------------")
            print(f"PC: {self.pc:02d}")
            print(f"Instrução: {instrucao}")

        # Se encontrar posição com dados ou vazia que não seja instrução válida
        if not isinstance(instrucao, str):
            raise TypeError(f"Posição de memória {self.pc} não contém uma instrução válida.")

        # DECODE + EXECUTE
        self.executar_instrucao(instrucao)

        # Mostrar estado dos registradores
        if exibir_passos:
            self.mostrar_estado()

    def executar(self, passo_a_passo: bool = True):
        """Executa o programa até que a instrução HALT seja encontrada."""
        while not self.halted:
            self.ciclo(exibir_passos=passo_a_passo)

    def mostrar_estado(self):
        """Exibe o conteúdo atual de todos os registradores."""
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")
