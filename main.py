""" Programa para apoyar al marinero Seijo
    Yenifer Barco Castrillón
    Mayo 3-2021 """

import utilidades as util

def probar_funciones():
    """ 
    Parameters
    ----------

    Returns
    -------
    criatura:string
        nombre de la criatura a gritar
    direccion:string
        Direccion en la que aparece la criatura
    """ 
    criatura= util.aparecer_criatura()
    direccion=util.aparecer_direccion()
    print(criatura, direccion)
    return criatura,direccion

def formar_frase(criatura,direccion):
    """ 
    Parameters
    ----------
    criatura:string
        nombre de la criatura a gritar
    direccion:string
        Direccion en la que aparece la criatura
    Returns
    -------

    """ 
    articulo_criatura=""
    articulo_direccion=""
    saludo="Ahoy! capitán,"

    #Encontrar arcticulo de la criatura correcto
    if criatura.find("ken")>=0 or criatura.find("po")>=0:
        articulo_criatura="un"
    elif criatura.find("nas")>=0:
        articulo_criatura="unas"
    elif criatura.find("ena")>=0 or criatura.find("ono")>=0:
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
    
    print(saludo,articulo_criatura,criatura,articulo_direccion,direccion,"\n")


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento
indice = int(input("Por favor ingrese un numero: "))
contador=0
while contador<indice:
    criatura,direccion = probar_funciones()
    formar_frase(criatura,direccion)
    contador+=1