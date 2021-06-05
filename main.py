""" Programa para apoyar al marinero Seijo
    Yenifer Barco Castrillón
    Mayo 3-2021 """

import utilidades as util

def probar_funciones():
    criatura= util.aparecer_criatura()
    direccion=util.aparecer_direccion()
    print(criatura, direccion)
    return criatura,direccion

def formar_frase(criatura,direccion):
    articulo_criatura=""
    articulo_direccion=""
    saludo="Ahoy! capitán,"

    #Encontrar arcticulo correcto
    if criatura.find("ken")>=0 or criatura.find("po")>=0:
        articulo_criatura="un"
    elif criatura.find("nas")>=0:
        articulo_criatura="unas"
    elif criatura.find("ena")>=0 and criatura.find("ono")>=0:
        articulo_criatura="una"
    elif criatura.find("nes")>=0:
        articulo_criatura="unos"
    else:
        articulo_criatura="Unas"
    
    #Encontrar articulo de la direccion
    if direccion.find("or")>=0:
        articulo_direccion="a"
    elif direccion=="proa" or direccion=="popa":
        articulo_direccion="por la"
    
    print(saludo,articulo_criatura,criatura,articulo_direccion,direccion)


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento

criatura,direccion = probar_funciones()
formar_frase(criatura,direccion)





