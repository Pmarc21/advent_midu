# Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve mágica ❄️. 
# Esta nieve tiene una propiedad especial: si dos montículos de nieve idénticos y adyacentes se encuentran, desaparecen automáticamente.

# Tu tarea es escribir una función que ayude a los elfos a simular este proceso. 
# El camino se representa por una cadena de texto y cada montículo de nieve un carácter.

# Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales hasta que no queden más movimientos posibles.

# El resultado debe ser el camino final después de haber eliminado todos los montículos duplicados:

def remove_snow(s: str) -> str:
    cleared_snow = False
    list_s = list(s)
    list_aux = list_s[:]

    while cleared_snow != True:
        for i in range(len(list_s) - 1):
            if list_s[i] == list_s[i+1]:
                list_aux.pop(i+1)
                list_aux.pop(i)
                list_s = list_aux[:]
                break
        else:
            cleared_snow = True
    return ''.join(list_s)
        
s = 'zxxzoz'
print(remove_snow(s))