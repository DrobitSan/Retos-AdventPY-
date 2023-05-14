'''
Papa Noél tiene nuevos trineos eléctricos pero debe controlar el consumo eléctrico ya que sólo tiene una 
batería de 20W.

Nos dan un array de trineos, de peor a mejor, con sus respectivos consumos. Cada trineo es un objeto con dos 
propiedades: name y consumption.

El campo consumption es un número que representa la cantidad de vatios (W) que consume el trineo para cada 
unidad de distancia. El campo name es una cadena de texto que representa el nombre del trineo.

Crea un programa que nos devuelva el nombre del mejor trineo disponible que nos permita cubrir la distancia.
'''

distance = 30
sleighs = [
  { 'name': "Dasher", 'consumption': 0.3 },
  { 'name': "Dancer", 'consumption': 0.5 },
  { 'name': "Rudolph", 'consumption': 0.7 },
  { 'name': "Midu", 'consumption': 1 }
]
battery = 20

def select_sleight(distance, sleighs):
    consumptions = []
    for sleigh in sleighs:
        consumption = sleigh['consumption'] * distance
        if consumption < battery:
          consumptions.append(consumption)
    best = max(consumptions)
    best_index = consumptions.index(best)
    name = sleighs[best_index]['name']
    return f'{name} is the best sleigh consuming only {best} WKm for a distance of {distance} Km'

print(select_sleight(distance, sleighs))


