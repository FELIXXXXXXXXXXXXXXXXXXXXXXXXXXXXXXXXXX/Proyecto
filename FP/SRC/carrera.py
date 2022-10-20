# -*- coding: utf-8 -*-
'''

Created on 12 October 2022
@author: Felix
'''

import csv
from collections import namedtuple, defaultdict, Counter 
from datetime import datetime 
from email.utils import parsedate_to_datetime
from sqlite3 import Date
from xmlrpc.client import boolean

Registro = namedtuple('Registro','id ,Venue, Date, Name, NameTag, Team, Laps, Time, self_car, cost')

#Función de lectura para el fichero auxiliar(de 297 líneas)
def lee_datos(fichero):
    lista_carreras = []
    with open (fichero, encoding='utf-8') as f:
        lector= csv.reader(f) #Saltamos a la siguiente linea
        next(lector)
        for row_id, Lugar, FechaGP, Nombre, Iniciales, Equipo, Vueltas, Tiempo, self_car, coste in lector:
            FechaGP = datetime.strptime(FechaGP,"%d-%b-%y").date()
            Tiempo =datetime.strptime(Tiempo,"%H:%M:%S.%f").time()
            tupla = Registro(int(row_id),Lugar,FechaGP,Nombre,Iniciales,Equipo,int(Vueltas),Tiempo,boolean(self_car),int(coste))
            lista_carreras.append(tupla)
    return lista_carreras

#---------------------------------------------------------------------------
#Operaciones de filtrado y conteo
#---------------------------------------------------------------------------

#Filtro: devolver una lista de tuplas con los registros que cumplen de el lugar de las carreras de F1
def filtrar_por_pais(lista_carreras,pais):
    lista_paises = []
    for r in lista_carreras:
        if r.Venue == pais:
            lista_paises.append(r)
    return lista_paises


#Suma de carreras completadas que tiene un piloto: Uso el campo Name Tag y sumo las carreras que tienen
#Existen los siguientes Name Tag--->(FAN,PAR,WAL,GON,ASC...)
#Devuelvo una tupla de dos elementos--->(NameTag, Nº de carreras)

def cantidad_carreras_completadas(ID, lista_carreras):
    carreras_completadas = 0
    for r in lista_carreras:
        if r.NameTag == ID:
            carreras_completadas += 1 
    tupla = (ID, carreras_completadas)
    return tupla




