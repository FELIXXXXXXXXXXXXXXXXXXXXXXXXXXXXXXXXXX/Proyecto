'''
Created on 9 dic. 2020

@author: Felix
'''

from carrera import *

def test_lectura_datos(): #Test de lectura del fichero auxiliar de 297 lineas
    print('---LECTURA DEL FICHERO--- ')
    lista_carreras = lee_datos('./data/F180.csv')
    print('Los 3 primeros registros:', lista_carreras[:3])
    print('Los 3 últimos registros;', lista_carreras[-3:])


def test_filtro_pais(lista_carreras):
    print('--- CARRERAS EN (PAIS)---')
    lista_pais = filtrar_por_pais(lista_carreras,'France') 
    print('5 primeras líneas:', lista_pais)

def test_carreras(lista_carreras):
    print('---CARRERAS CIMPLETADAS---')
    NameTag ='FIT'
    lista = cantidad_carreras_completadas(NameTag, lista_carreras)
    print('(NameTag, nºCarreras completadas):',lista) 

#-----------------------------------------------------------------------

if __name__ == '__main__':
    

    test_lectura_datos()
    lista_carreras = lee_datos('./data/F180.csv')

    #test_filtro_pais(lista_carreras) #En este caso Uso 'France' como filtro
    #test_carreras(lista_carreras)

    
   
    