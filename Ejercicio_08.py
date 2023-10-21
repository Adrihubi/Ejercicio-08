MaxTamC = 0
A = [10] * MaxTamC
frente = 0
final = 0
contador = 0

frente = 0
final = 0
respuesta = input("¿Desea agregar elementos a la cola? (s/n): ").lower()

while respuesta == 's' and contador < 10:
    if (final + 1) % MaxTamC == frente:
        print("Desboramiento de la cola")
        exit(1)
        
    elemento = int (int(input("Ingrese elemento para la cola: ")))
    final = (final + 1) % MaxTamC
    A[final] = elemento
    
    contador += 1
    print(f"Elemento {contador} agregado a la cola: {elemento}")
    
    if contador < 10:
        respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ").lower()