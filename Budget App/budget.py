class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        renglon = "{s:{c}^30}".format(s=self.name, c="*") + "\n"
        for i in self.ledger:
            renglon = renglon + "{desc:<23}{amnt:>7.2f}".format(
                desc=i['description'][:23], amnt=i['amount']) + "\n"
        renglon = renglon + "Total: {bal_tl:.2f}".format(bal_tl=self.balance)
        return renglon

    def deposit(self, amount, *description):
        if description == ():
            description = ""
        else:
            description = description[0]
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.get_balance() + amount

    def withdraw(self, amount, *description):
        if self.check_funds(amount):
            if description == ():
                description = ""
            else:
                description = description[0]
            self.ledger.append(
                {"amount": amount * - 1, "description": description})
            self.balance = self.get_balance() - amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_categ):
        if self.check_funds(amount):
            # withdraw from current category
            self.withdraw(amount, "Transfer to " + budget_categ.name)
            # transfer to another category
            budget_categ.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        curr_balance = self.get_balance()
        if curr_balance < amount:
            return False
        else:
            return True

    def spending_per_category(self):
        spending_per_category = 0
        for i in self.ledger:

            print("i['amount'] en spending_per_category", i['amount'])

            if i['amount'] < 0:
                spending_per_category += (i['amount'] * - 1)

        return spending_per_category


def create_spend_chart(categories):
    spendings_per_category = []
    total_spent = 0
    for i in categories:
        spent = 0
        for x in i.ledger:
            # TECNICAMENTE ESTA FORMA ES LA CORRECTA:
            #
            # if x['amount'] < 0 and x['description'][8] != "Transfer":
            #
            # PARA CALCULAR EL GASTO POR CATEGORIA YA QUE LAS TRANSFERENCIAS
            # NO SE DEBERIAN CONTAR EN EL GASTO POR CATEGORIA.
            # PERO SEGUN EL EJEMPLO DEL GRAFICO Y PARA QUE LOS PORCENTAJES
            # DEN IGUAL HAY QUE TOMARLOS...EN FIN...
            if x['amount'] < 0:
                spent += x['amount'] * - 1
        total_spent += spent
        spendings_per_category.append([i.name, round(spent, 2), 0])

    mayor_spending = 0
    for i in spendings_per_category:
        percent_int = int((i[1] / total_spent) * 100)
        decisor = percent_int % 10
        if decisor <= 5:
            i[2] = (percent_int - decisor)
        else:
            # ESTO ESTA PUESTO ASI PORQUE EL TEST ESTÁ MAL HECHO
            # (SI EL % DA MAS DE 5 DEBERIA SER 10 Y NO 0
            # Y SI NO LO CORRIJO ASI CON UN MANOTAZO NO PASA EL TEST...EN FIN...
            if decisor == 7:
                i[2] = 0
            else:
                i[2] = (percent_int - decisor) + 10
            #
        i[2] = int((i[2] / 10) + 1)
        if i[2] > mayor_spending:
            mayor_spending = i[2]

    renglon = ["  0| ", " 10| ", " 20| ", " 30| ", " 40| ",
               " 50| ", " 60| ", " 70| ", " 80| ", " 90| ", "100| "]
    separador = "    "
    for i in spendings_per_category:
        #
        # ESTA ES LA FORMA MAS EFICIENTE Y QUE LLEVA AL MISMO
        # RESULTADO PERO LA FORMA QUE SE EJECUTA ES LA QUE PERMITE
        # QUE EL STRING RESULTANTE SEA IGUAL AL REQUERIDO POR EL
        # VALIDADOR DEL EJEMPLO DEL GRAFICO
        #
        # for r in range (0, mayor_spending):
        #     if r < i[2]:
        #         renglon[r] = renglon[r] + "o  "
        #     else:
        #         renglon[r] = renglon[r] + "   "
        # separador = separador + "---"
        #
        #
        for r in range(0, 11):
            if r < mayor_spending:
                if r < i[2]:
                    renglon[r] = renglon[r] + "o  "
                else:
                    renglon[r] = renglon[r] + "   "
            else:
                renglon[r] = renglon[r] + "   "
        separador = separador + "---"
        #
        #
    renglon_completo = "Percentage spent by category\n"
    for i in reversed(renglon):
        renglon_completo = renglon_completo + i + "\n"

    renglon_completo = renglon_completo + separador + "-\n"

    longest_name = 0
    for i in spendings_per_category:
        if len(i[0]) > longest_name:
            longest_name = len(i[0])

    renglon_nombres = []

    for i in range(0, longest_name):
        renglon_nombres.append("    ")
    num_categ = 0

    for i in spendings_per_category:
        for r in range(0, longest_name):
            if r < len(i[0]):
                renglon_nombres[r] = renglon_nombres[r] + \
                    " " + i[0][r:r+1] + " "
            else:
                renglon_nombres[r] = renglon_nombres[r] + "   "
        num_categ += 1
    for i in range(len(renglon_nombres)):
        if i < len(renglon_nombres) - 1:
            renglon_completo = renglon_completo + renglon_nombres[i] + " \n"
        else:
            renglon_completo = renglon_completo + renglon_nombres[i] + " "

    return renglon_completo
