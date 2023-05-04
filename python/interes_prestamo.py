#calcular el intenres de un prestamos capital final= capital(1+interes/100*tiempo)
def deuda_total(capital,interes,tiempo):
    print("El capital total a pagar es: ")
    print(capital*(1+interes/100*tiempo))

deuda_total(100,10,5)