'''
Una pareja de entusiastas de la navidad ha creado una empresa de adornos navideños. El primer adorno que quieren fabricar es un cubo que se pone en los árboles.

El problema es que tienen que programar la máquina y no saben cómo hacerlo. Nos han pedido ayuda para lograrlo.

Para crear los cubos se le pasa un número con el tamaño deseado al programa y este devuelve un string con el diseño de ese tamaño. Por ejemplo, si le pasamos un 3, el programa debe devolver un cubo de 3x3x3
'''


def create_cube(size):
    figura = ''
    for n in range(size):
        alzado = (size - n) * ' ' + '/\\' * (n + 1)
        perfil = '_\\' * size + '\n'
        figura += (alzado + perfil)    
    for n in reversed(range(size)):
        alzado = (size - n) * ' ' + '\\/' * (n + 1)
        perfil = '_/' * size + '\n'
        figura += (alzado + perfil)

    return figura

mi_cubo = create_cube(7)

print(mi_cubo)
