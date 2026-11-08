import os

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ser un número entero.')

def menu(titulo, opciones):
    print(f"\n========== {titulo} ==========")
    for opcion in opciones:
        print(f"{opcion}")
    lon = len(opciones) - 1
    return input(f"Opción[0...{lon}]: ").strip().upper()

if __name__ == "__main__":
    opc = menu('Menu Principal', ['1)Pila', '2)Cola', '0)salir'])
    opc1 = menu('Menu Pila', ['1)entrar a la pila', '2)listar', '3)desapilar', '4)cargar datos de prueba'])
    opc2 = menu('Menu Cola', ['1)entrar a la cola', '2)listar', '3)desencolar', '4)cargar datos de prueba'])