"""
Tienes una caja de regalos de Navidad que Santa Claus quiere entregar a los niños. Cada regalo está representado por una cadena. Santa Claus tiene un trineo que puede llevar un peso limitado, y cada regalo dentro de la caja tiene un peso que es igual al número de letras en el nombre del regalo.

Santa Claus también tiene una lista de renos que pueden ayudarlo a entregar los regalos. Cada reno tiene un límite de peso máximo que puede llevar. El límite de peso máximo de cada reno es igual a dos veces el número de letras en su nombre.

Tu tarea es implementar una función distributeGifts(packOfGifts, reindeers) que recibe una caja de regalos y una lista de renos y devuelve el número máximo de cajas de estos regalos que Santa Claus puede entregar a los niños. Las cajas de regalos no se pueden dividir.
"""


pack_gifts = ["book", "doll", "ball"]
reindeers = ["dasher", "dancer"]

def distribute_gifts(pack_gifts, reindeers):
    weight_gift = 0
    capacity_reindeers = 0

    for n in pack_gifts:
        weight_gift += len(n)

    for i in reindeers:
        capacity_reindeers += 2 * len(i)

    print(weight_gift, capacity_reindeers)
    num_gifts = capacity_reindeers //  weight_gift 


    return num_gifts

num_gifts = distribute_gifts(pack_gifts, reindeers)

print(num_gifts)