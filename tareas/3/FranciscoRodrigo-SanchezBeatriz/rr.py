from common.watcher import *
from common.mystats import *

def round_robin(procesos):
    tiempo = 1
    espera = [0]*len(procesos)
    tiempo_exe = []
    cola_espera = []

    for j in procesos:
        tiempo_exe.append(j[2])

    while proc_finalizado(procesos) != True:
        for j in procesos:
            if j[1] == tiempo-1:
                cola_espera.append(j)

        #print("Antes: "+str(cola_espera))
        if len(cola_espera) != 0:
            #disminuir el tiempo del ultimo

            # si hay mas de un proceso se incrementa el de al lado.
            if len(cola_espera) == 1:
                cola_espera[0][2] -= 1
            else :
                cola_espera[1][2] -= 1

            cola_espera.append(cola_espera[0])
            cola_espera.pop(0)

            #aumentar espera de los otros procesos en la cola
            aumentEspera_deOtros(0,espera,cola_espera,procesos)
            #print("t= "+ str(tiempo-1)+": "+ str(espera))

            # si su tiempo es cero, sacamos de la cola
            if cola_espera[0][2] <= 0 :
                del cola_espera[0]
        tiempo += 1

        #print("DESPUES: "+str(cola_espera))

    estadisticas(tiempo_exe,espera,procesos)
