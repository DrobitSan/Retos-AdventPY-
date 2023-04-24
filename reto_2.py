"""
Un millonario ha comprado una red social y no trae buenas noticias. Ha anunciado que cada vez que una jornada de trabajo se pierde por un día festivo, habrá que compensarlo con dos horas extra otro día de ese mismo año.

Obviamente la gente que trabaja en la empresa no le ha hecho ni pizca de gracia y están preparando un programa que les diga el número de horas extras que harían en el año si se aplicara la nueva norma.

Al ser trabajo de oficina, su horario laboral es de lunes a viernes. Así que sólo tienes que preocuparte de los días festivos que caen en esos días.

Dado un año y un array con las fechas de los días festivos, devuelve el número de horas extra que se harían ese año
"""

import datetime as dt

year = 2022
holidays = ['01/06', '04/01', '12/25'] # formato MM/DD


def count_hours(year, holidays):
    dates = []
    for n in holidays:
        dates.append(n.split('/'))

    weekdays = []
    for d in dates:
        month = int(d[0])
        day = int(d[1])
        weekday = dt.date(year, month, day).isoweekday()
        weekdays.append(weekday)

    dias = 0
    for w in weekdays:
        if (1 <= w <= 5):
            dias += 1
        horas = dias * 2

    return f'{dias} dias -> {horas} extra en total'

horas = count_hours(year, holidays)
print(horas)






