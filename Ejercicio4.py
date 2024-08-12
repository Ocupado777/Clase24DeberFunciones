Z = 20 
def mi_func():
    Z = 10
    print(f"Variable local x dentro de la función: {Z}")
    mi_func()
    print(f"Variable global x fuera de la función: {Z}")