from time_calculator import add_time
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


print(add_time("11:59 PM", "24:05"))