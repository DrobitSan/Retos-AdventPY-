'''
Se han estropeado algunos trineos eléctricos y los elfos están buscando piezas de repuesto para arreglarlos,
 pero no tienen claro si las piezas que tienen sirven.

Las piezas de repuesto son cadenas de texto y el mecánico Elfon Masc ha dicho que una pieza de repuesto es
 válida si la pieza puede ser un palíndromo después de eliminar, como máximo, un carácter.

Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
'''

def check_part(entry):
    string = list(entry)
    if string == string[::-1]:
        return True
    for i, n in enumerate(string):
        string = list(entry)
        string.pop(i)
        if string == string[::-1]:
            return True
    return False


print(check_part('uwu'))
print(check_part('miidim'))
print(check_part('midu'))
