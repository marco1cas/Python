def casilla(n):
    if n < 1 or n > 64:
        return ValueError("Casilla inválida. Debe estar entre 1 y 64.")
    return 2 ** (n - 1)

def totales():
    return sum(2**i for i in range(64))


n = 5  
print(f"Granos en la casilla {n}: {casilla(n)}")
print(f"Total de granos en el tablero: {totales()}")
