PESO_MINIMO = 1
PESO_MAXIMO = 10_000

FAIXAS = (
    (1_000, 10),
    (5_000, 20),
)
FRETE_ACIMA_DAS_FAIXAS = 30


def calcular_frete(peso_gramas: int) -> int:
    """Calcula o frete, em reais inteiros, a partir do peso em gramas."""
    if peso_gramas < PESO_MINIMO:
        raise ValueError("Peso deve ser positivo")
    if peso_gramas > PESO_MAXIMO:
        raise ValueError("Peso acima do limite")
    for limite, valor in FAIXAS:
        if peso_gramas <= limite:
            return valor
    return FRETE_ACIMA_DAS_FAIXAS
