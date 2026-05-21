import machine


def hilo_principal():
    print("Hilo Principal")
    contador = 0
    while True:
        input("Ingrese comando")
        contador += 1
        if contador >= 3:
            machine.reset()