'''
Para evitar perder datos cuando el servidor se cae, Papa Noel ha decidido hacer backups incrementales. Un 
hacker llamado S4vitelf le esta ayudando.

Por un lado, tenemos el timestamp de cuándo se hizo el último backup.

También tenemos los cambios que se han realizado en un array de arrays. Cada array interno contiene dos 
elementos: el id del archivo modificado y el timestamp de la modificación.

Tienes que crear un programa que devuelva un array con las id de los archivos que tendríamos que hacer 
backup porque han sido modificados desde el último backup y ordenados de forma ascendente. Ejemplo:
'''

last_backup = 1546300800
changes = [
  [ 3, 1546301100 ],
  [ 2, 1546300800 ],
  [ 1, 1546300800 ],
  [ 1, 1546300900 ],
  [ 1, 1546301000 ]
]

def files_backup(last_backup, changes):
    to_backup = []
    for id, time_stamp in changes:
        if time_stamp > last_backup and id not in to_backup:
            to_backup.append(id)
    return sorted(to_backup)


print(files_backup(last_backup, changes))