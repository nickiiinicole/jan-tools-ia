import math
from fastmcp import FastMCP

# Se crea la instancia del servidor [cite: 28]
mcp = FastMCP("Calculadora_Avanzada")

@mcp.tool()
def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

@mcp.tool()
def restar(a: float, b: float) -> float:
    """Resta el segundo número al primero (a - b)."""
    return a - b

@mcp.tool()
def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

@mcp.tool()
def raiz_cuadrada(a: float) -> float:
    """Calcula la raíz cuadrada de un número. El número debe ser positivo."""
    if a < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo")
    return math.sqrt(a)

if __name__ == "__main__":
    # Esto lanza el servidor en modo stdio [cite: 41, 42]
    mcp.run()