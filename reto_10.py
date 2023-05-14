'''
Crea un programa que compruebe que el trineo de Santa Claus hace una parabola al saltar entre ciudades.
 Recibes un array de números que representan la altura en la que se encuentra el trineo en cada momento.

Para que la parabola sea correcta, el viaje del trineo debe ser ascendente al principio, llegar al punto más
alto y descender hasta el final. No puede volver a subir una vez que ha bajado, ni puede iniciar el viaje 
bajando. Veamos unos ejemplos:
'''


heights = [1, 3, 8, 5, 2]
hei_2 = [1, 7, 3, 5]


def check_jump(heights):
    max_value = max(heights)
    max_index = heights.index(max_value)
    up = heights[0 : max_index]    
    down = heights[max_index : len(heights)]
    if up == sorted(up) and down == sorted(down, reverse=True):
        return True 
    return False
    
    
print(check_jump(heights))
print(check_jump(hei_2))

