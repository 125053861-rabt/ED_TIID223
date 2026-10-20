from collections import deque

def ejecutar_pila():
    while True:
        pila = deque()
        
        def push(elemento):
            pila.append(elemento) 
            
        def pop_stack():
            return pila.pop()   
            
        def peek():
            return pila[-1] if pila else None
        
        while True:
            print("\n--- MENÚ PILA ---")
            print("1. Push (Insertar en pila)")
            print("2. Pop (Borrar en pila)")
            print("3. Peek / Top (Ver cima de la pila)")
            print("4. Listar pila")
            print("5. Salir")
            
            opcion = input("Seleccione una opción (1-5): ")
            
            if opcion == "1":
                try:
                    numero = int(input("Ingrese el numero a insertar en la pila: "))
                    push(numero)
                    print(f"Numero {numero} apilado")
                except ValueError:
                    print("Error: Por favor, ingresa un numero :)")
                    
            elif opcion == "2":
                if len(pila) > 0:
                    eliminado = pop_stack()
                    print(f"Elemento desapilado: {eliminado}")
                else:
                    print("La pila esta vacia")
                    
            elif opcion == "3":
                if len(pila) > 0:
                    print(f"Elemento en la cima: {peek()}")
                else:
                    print("La pila esta vacia")
                    
            elif opcion == "4":
                if len(pila) > 0:
                    print("Estado actual de la pila:", list(pila))
                else:
                    print("No hay nadotototota")
                    
            elif opcion == "5":
                print("Saliendo....")
                break
            else:
                print("Por favor, elija un número entre 1 y 5")
                
        repetir = input("\nQuieres ejecutar el codigo de nuevo? (s/n): ").strip().lower()
        if repetir != 's':
            print("BYEEEE")
            break

if __name__ == "__main__":
    ejecutar_pila()