'''
En los almacenes de Papá Noel están haciendo inventario. Hay tres almacenes (que se representa 
cada uno como un Array). En cada almacén hay regalos.

Nos han pedido que escribamos un programa que nos diga qué regalos hay que comprar para reponer en 
nuestros almacenes ahora que se acerca la Navidad. Un regalo se tiene que reponer cuando sólo hay 
stock en uno de los tres almacenes.
'''


a1 = ['bici', 'coche', 'bici', 'bici']
a2 = ['coche', 'bici', 'muñeca', 'coche']
a3 = ['bici', 'pc', 'pc']


def gifts_refill(a1, a2, a3):
    refill = []
    for i, a in enumerate([a1, a2, a3]):
        comprobacion = [a1, a2, a3]
        comprobacion.pop(i)
        for n in a:
            if n not in (comprobacion[0] or comprobacion[1]):
                refill.append(n)
    replenish = list(set(refill))
    return replenish



rellenar = gifts_refill(a1, a2, a3)

print(rellenar)

