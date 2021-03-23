import random

#beta del juego mastermind

#######################
##BLOQUE DE FUNCIONES##
#######################

#funcion que arma el codigo de colores del primer jugador aleatoriamente
#entrada: nada
#Saldia: lista de strings, codigo de colores armado
def codigo_secreto(): 
    colores = ["rojo", "azul", "verde", "amarillo", "naranjo", "morado", "burdeo", "cafe", "rosado"]
    codigo_jugador1 = random.sample(colores, 4)
    return codigo_jugador1


def encontrar_codigo(jugador1, colores): 
    print("opciones de colores a ingresar: rojo, azul, verde, amarillo, naranjo, morado, burdeo, cafe, rosado\n")
    i = 0
    jugador2 = []
    pistas = []
    #el siguiente bucle es para armar la lista del segundo jugador 
    while(i < colores):
        color = input("ingrese un color de los mencionados: ")
        jugador2.append(color)
        i = i + 1
    jugador2.reverse
    #bucle para encontrar las coincidencias entre los dos codigos
    j = 0
    while(j < colores):
        #condicion para las pistas negras
        if jugador2[j] == jugador1[j]:
            pistas.append(1)
        #condicion para las pistas blancas
        elif jugador2[j] in jugador1:
            pistas.append(0)
        #condicion para niguna de las anteriores
        else:
            pistas.append("null")
        j = j + 1
    intentos_jugador2 = pistas + jugador2
    return intentos_jugador2

        
def vidas(dificultad, jugador1, colores):
    if dificultad == "facil":
        i = 0
        while(i < 10):
            jugador2 = encontrar_codigo(jugador1, colores)
            print("eleccion jugador 2", jugador2)
            if jugador2[4:] == jugador1:
                print("has adivinado el codigo del jugador 1")
                break
            else:
                i = i + 1
                    
    if dificultad == "dificil":
        i = 0
        while(i < 6):
            jugador2 = encontrar_codigo(jugador1, colores)
            print("eleccion jugador 2", jugador2)
            if jugador2[4:] == jugador1:
                print("has adivinado el codigo del jugador 1")
                break
            else:
                i = i + 1
    
        
    
#######################
##BLOQUE DEFINICIONES##
#######################

#Entrada

cantidad_colores = 4
print("debes elegir dificultad, facil son 10 intentos y dificil son 6\n")
dificultad = input("ingrese la dificultad del jjuego, facil o dificil: ")
codigo = codigo_secreto()

#Procesamiento

vidas(dificultad, codigo, cantidad_colores)

#Salida

print("fin del juego")
