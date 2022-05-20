def arithmetic_arranger(problems, *args):
    ''' Proyect nº 1 '''

    problems_cant = len(problems)
    if problems_cant > 5:
        return "Error: Too many problems."

    for x in problems:
        if "+" not in x and "-" not in x:
            return "Error: Operator must be '+' or '-'."

    for x in problems:
        separado = []
        separado = x.split()
        if not separado[0].isdigit() or not separado[2].isdigit():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

    for x in problems:
        separado = []
        separado = x.split()
        if len(separado[0]) > 4 or len(separado[2]) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

    renglon_sup = ""
    renglon_inf = ""
    renglon_gui = ""
    renglon_res = ""
    for x in problems:
        separado = x.split()
        uno = len(separado[0])
        dos = len(separado[2])
        if uno < dos:
            largo = dos + 2
        else:
            largo = uno + 2

        guion = ""
        for i in range(largo):
            guion = guion + "-"

        if "+" in x:
            resultado = int(separado[0]) + int(separado[2])
        else:  # "-" in x:
            resultado = int(separado[0]) - int(separado[2])
        res_to_str = str(resultado)
        renglon_res = renglon_res + (res_to_str.rjust(largo) + "    ")

        separado[0] = separado[0].rjust(largo)
        separado[2] = separado[1] + separado[2].rjust(largo - 1)

        renglon_sup = renglon_sup + (separado[0] + "    ")
        renglon_inf = renglon_inf + (separado[2] + "    ")
        renglon_gui = renglon_gui + (guion + "    ")

    renglon_sup = renglon_sup[:-4]
    renglon_inf = renglon_inf[:-4]
    renglon_gui = renglon_gui[:-4]
    renglon_res = renglon_res[:-4]

    if args:
        arranged_problems = renglon_sup + "\n" + \
            renglon_inf + "\n" + \
            renglon_gui + "\n" + \
            renglon_res
    else:
        arranged_problems = renglon_sup + "\n" + \
            renglon_inf + "\n" + \
            renglon_gui

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
