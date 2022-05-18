from arith_arranger import arithmetic_arranger
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


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

