"""
Módulo ULA (Unidade Lógica e Aritmética)
Implementa operações aritméticas e lógicas de 8 bits.
"""

class ULA:
    @staticmethod
    def limitar_8bits(valor: int) -> int:
        """Garante que o valor permaneça na faixa de 8 bits (0 a 255)."""
        return valor & 0xFF

    @classmethod
    def operar(cls, operacao: str, a: int, b: int) -> int:
        """
        Executa a operação aritmética ou lógica solicitada sobre os operandos a e b.
        Operações suportadas: ADD, SUB, AND, OR, XOR.
        """
        if operacao == "ADD":
            resultado = a + b
        elif operacao == "SUB":
            resultado = a - b
        elif operacao == "AND":
            resultado = a & b
        elif operacao == "OR":
            resultado = a | b
        elif operacao == "XOR":
            resultado = a ^ b
        else:
            raise ValueError(f"Operação da ULA inválida: {operacao}")

        return cls.limitar_8bits(resultado)
