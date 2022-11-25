from statistics import mean
def elegir():
    x=input('1.tupla , 2.list , 3. set, 4.diccionario, ELIJA UNA OPCION: ')
    match x:
        case '1':
            print('no es mutable y ordenada')
        case '2':
            print('es mutable y ordenada')
        case '3':
            print('es mutable y desordenada')
        case '4':
            print('es mutable y contiene valor y de cada atributo o elemento')
        case _:
            elegir()


lista=[10, 'juan' , 9.95 ,False , "madrid" , 15]
for n in lista:
    print(n)

lista.append(25.95)
#for n in sorted(lista):
    #print(n)
#el elemento se añade al final de la lista

#tupla=(10, 'juan' , 9.95 ,False , "madrid" , 15)
#for n in tupla:
 #   print(n)

#tupla.add(25.95) no se puede para añadir un elemento a una tupla hay que hacer otra tupla y sumarlas
#for n in sorted(tupla):
    #print(n)

#no se pueden ordenar ya que son distintos tipos de elementos

cuiudade={'madrid','sevilla','jaen','cordoba','barcelona'}
print(sorted(cuiudade))

#nos da un set ordenado en caso de no ordenarlo saldra siempre aleatorio

diccionario={'Lunes' : 7,
'Martes' : 8.5,
'Miércoles' : 6,
'Jueves' : 7,
'Viernes' : 9}

print(diccionario.values())
print(sum(diccionario.values()))
print(mean(diccionario.values()))