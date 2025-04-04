import random
from multiprocessing.connection import Client
conn=Client(('172.20.10.4', 12345), authkey=b'2444666666')
while True:
    try:
        # Recibir mensaje cifrado del comandante
        mensaje_cifrado = conn.recv()

        print(f"Espía recibió:\n{mensaje_cifrado}")
        probabilidad = random.random()
        # Simular un 20% de probabilidad de manipulación
        if probabilidad < 0.2:
            # Simular manipulación del mensaje
            desplazamiento = random.randint(2, 3)
        else:
            desplazamiento = 3  # Desplazamiento para el cifrado César (puedes cambiarlo según sea necesario)        
        cifrado = ""
        for char in mensaje_cifrado:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                cifrado += chr((ord(char) - offset -desplazamiento) % 26 + offset)
            else:
                cifrado += char
        conn.send(cifrado)

    except EOFError:
        print("Conexión cerrada por el comandante. Espía saliendo...")
        break
