import os

def clear_console():
    """
    PARA LIMPIAR LA PANTALLA DE LA CONSOLA
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clear_console()

#
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

def cambio_meridiano(meridiano):
    """
    para cambiar de AM a PM y viceversa
    """
    if meridiano == "AM":
        meridiano = "PM"
        suma_dias = 0
    else:  # merid == "PM"
        meridiano = "AM"
        suma_dias = 1

    return meridiano, suma_dias


def add_time(start, duration, *start_day):
    """
    TOMA UNA FECHA Y LE SUMA LAS HORAS Y
    MINUTOS QUE INGRESE. ADEMAS SI SE INDICA
    UN DIA DE LA SEMANA DE DONDE INICIA
    TAMBIEN LO TIENE EN CUENTA PARA EL CALCULO
    """

    semana = ["Monday", "Tuesday", "Wednesday",
              "Thursday", "Friday", "Saturday", "Sunday"]
    horas = int(start[:start.find(":")])
    minutos = int(start[-5:-2])
    merid = start[-2:].strip()
    hors_d = int(duration[:duration.find(":")])
    mins_d = int(duration[-2:])
    mas_dias = 0

    if minutos + mins_d >= 60:
        minutos_tot = minutos + mins_d - 60
        mas_horas_x_min = 1
    else:
        minutos_tot = minutos + mins_d
        mas_horas_x_min = 0

    horas_totales = hors_d + mas_horas_x_min

    if horas_totales > 12:
        if horas_totales % 24:
            medios_dias = int((horas + hors_d + mas_horas_x_min) / 12)
            mas_dias = int(medios_dias / 2)
            horas_totales = horas
            # esta linea ASI funciona para todo el resto de las pruebas
            # horas_resto = (horas + hors_d + mas_horas_x_min) % 12

            horas_resto = (hors_d + mas_horas_x_min) % 12


            if not medios_dias % 2 and medios_dias != 2:
                nvo_merid = cambio_meridiano(merid)
                merid = nvo_merid[0]
                mas_dias = mas_dias + nvo_merid[1]

            if not horas_resto == 0:
                # esta linea ASI funciona para todo el resto de las pruebas
                # horas_totales = horas + horas_totales + horas_resto
                horas_totales = horas_totales + horas_resto

                if horas_totales >= 12:
                    horas_totales = horas_totales - 12
                    if horas_totales == 0:
                        horas_totales = 12

                    nvo_merid = cambio_meridiano(merid)
                    merid = nvo_merid[0]
                    mas_dias = mas_dias + nvo_merid[1]

            if medios_dias % 2 and horas_resto == 0:
                nvo_merid = cambio_meridiano(merid)
                merid = nvo_merid[0]
                mas_dias = mas_dias + nvo_merid[1]
                horas_totales = horas_totales + mas_horas_x_min
        else:
            mas_dias = int(horas_totales / 24)
            horas_totales = horas

    else:
        horas_totales = horas_totales + horas
        if horas_totales > 12:
            horas_totales = horas_totales - 12
            nvo_merid = cambio_meridiano(merid)
            merid = nvo_merid[0]
            if merid == "AM":
                mas_dias += 1

        if horas_totales == 12 and minutos_tot >= 0 and merid == "AM":
            merid = "PM"

    if not start_day:
        str_day = ""

    else:
        dia_d = (start_day[0]).lower().capitalize()

        # print("dia_d", dia_d)

        dias_resto = mas_dias % 7
        nuevo_dia = semana.index(dia_d) + dias_resto

        if nuevo_dia > 6:
            nuevo_dia = nuevo_dia - 7

        # print("nuevo_dia", nuevo_dia)

        str_day = ", " + semana[nuevo_dia]

    # print("horas, minutos, merid", horas, minutos, merid)
    # print("horsD, minsD", hors_d, mins_d)
    # print("masHorasxMin", mas_horas_x_min)
    # print("horasTotales", horas_totales)
    # print("minutosTot", minutos_tot)
    # print("horas_resto", horas_resto)
    # print("mediosDias", medios_dias)
    # print("masDias", mas_dias)
    # print("nvo_merid", nvo_merid)
    # print("meridiano", merid)

    if mas_dias == 0:
        new_time = str(horas_totales) + ":" + \
            str(minutos_tot).zfill(2) + " " + merid + str_day
    else:
        if mas_dias == 1:
            new_time = str(horas_totales) + ":" + str(minutos_tot).zfill(2) + \
                " " + merid + str_day + " (next day)"
        else:
            new_time = str(horas_totales) + ":" + str(minutos_tot).zfill(2) + \
                " " + merid + str_day + " (" + str(mas_dias) + " days later)"

    return new_time


# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 PM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))
# print(add_time("2:59 AM", "72:00"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("8:16 PM", "466:02", "tuesday"))

# errores
print(add_time("11:59 PM", "24:05"))
