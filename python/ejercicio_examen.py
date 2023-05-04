#se desea calcular cuanto gna en total un trabajador con las siguientes tarigas la hora normal tiene un valor de 10 soles y la hora extra tiene un valor de 15

def pago(horas):

    if horas>40:
        remuneracion=40*10+(horas-40)*15
    elif horas<=40:
        remuneracion = horas*10
        print(remuneracion)

    pago(20)

