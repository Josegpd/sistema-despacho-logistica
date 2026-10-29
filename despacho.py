# Definicion de la clase Pila
class Stack:

    # Crear una pila vacia
    def __init__(self):
        self.stack = []

    # Verificar si la pila esta vacia
    def empty(self):
        return len(self.stack) == 0

    # Retornar la longitud de la pila
    def size(self):
        return len(self.stack)

    # Apilar un elemento
    def push(self, item):
        self.stack.append(item)

    # Desapilar el elemento del tope
    def pop(self):
        if not self.empty():
            return self.stack.pop(-1)
        return None

    # Obtener el elemento del tope
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def __str__(self):
        return str(self.stack)

# Definicion de la clase Cola
class Queue:

    # Crear una cola vacia
    def __init__(self):
        self.queue = []

    # Verifica si la cola esta vacia
    def empty(self):
        return len(self.queue) == 0

    # Encolar al final
    def enqueue(self, item):
        self.queue.append(item)

    # Desencolar el primer elemento de la cola
    def dequeue(self):
        if not self.empty():
            self.queue.pop(0)

    # Obtener el primer elemento de la cola
    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

    # Obtener el elemento final de la cola
    def back(self):
        if not self.empty():
            return self.queue[-1]
        return None

    # Obtener la longitud de la cola
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


# Declaracion de funciones

def menu_despacho():
    print("=" * 50)
    print(f"\t SISTEMA DE DESPACHO Y ALMACÉN \t")
    print("=" * 50)
    print("1. [PILA] Apilar caja (push)")
    print("2. [PILA] Retirar caja de la cima (pop)")
    print("3. [COLA] Llega camión a la fila (enqueue)")
    print("4. [COLA] Despachar primer camión (dequeue)")
    print("5. Ver estado del almacén y camiones")
    print("6. Salir")
    print("-" * 50)
    print("Seleccione una opción (1-6): ", end=' ')

def apilar(caja):
    almacen.push(caja)
    print(f"-> Caja [{caja}] apilada con éxito.\n")


def retirar_caja():
    if not almacen.empty():
        caja_retirada = almacen.pop()
        print(f"\n-> Caja [{caja_retirada}] retirada con exito.\n")
    else: 
        print("\n[!] Error: El almacén está vacío (no hay cajas que retirar).\n")
        
def mostrar_estado():
    print("")
    print("*" * 50)
    print("ESTADO ACTUAL:")
    
    # Mostramos la pila de la cima a la base
    # Hacemos una copia invertida para no alterar la original
    pila_temp = list(reversed(almacen.stack))
    print(f"- Cajas apiladas (Cima -> Base): {pila_temp}")
    
    # Mostramos la cola del frente al fin
    print(f"- Fila de camiones (Frente -> Fin): {bahia_camiones}")
    print("*" * 50, end="\n\n")

almacen = Stack()
bahia_camiones = Queue()

while(True):
    menu_despacho()

    # Validar que la entrada sea un numero y este en el rango de opciones
    while(True):
        entrada = input()
        if entrada.isdigit() and 1 <= int(entrada) <= 6:
            opcion = int(entrada)
            break
        else:
            print("\nOpción invalida. Elija una opcion valida (1-6).\n")

    if(opcion == 1):
        caja = input("\nNombre de la caja: ")
        apilar(caja)
    elif(opcion == 2):
        retirar_caja()
    elif(opcion == 3):
        pass
    elif(opcion == 4):
        pass
    elif(opcion == 5):
        mostrar_estado()
    elif(opcion == 6):
        print("\nSaliendo...")
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
