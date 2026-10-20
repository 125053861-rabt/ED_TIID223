from collections import deque

def ejecutar_cola():
    while True:
        cola = deque()
        
        def enqueue(elemento):
            cola.append(elemento)
            
        def dequeue():
            return cola.popleft() 
            
        def front():
            return cola[0] if cola else None
        
        while True:
            print("\n--- MENÚ COLA ---")
            print("1. Enqueue (Insertar en cola)")
            print("2. Dequeue (Borrar en cola)")
            print("3. Front (Ver frente de la cola)")
            print("4. Listar cola")
            print("5. Salir")
            
            opcion = input("Seleccione una opción (1-5): ")
            
            if opcion == "1":
                try:
                    numero = int(input("Ingrese el numero a insertar en la cola: "))
                    enqueue(numero)
                    print(f"Numero {numero} encolado")
                except ValueError:
                    print("Error: Por favor, ingresa un numero :)")
                    
            elif opcion == "2":
                if len(cola) > 0:
                    eliminado = dequeue()
                    print(f"Elemento desencolado: {eliminado}")
                else:
                    print("La cola esta vacia")
                    
            elif opcion == "3":
                if len(cola) > 0:
                    print(f"Elemento al frente: {front()}")
                else:
                    print("La cola esta vacia")
                    
            elif opcion == "4":
                if len(cola) > 0:
                    print("Estado actual de la cola:", list(cola))
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
    ejecutar_cola()