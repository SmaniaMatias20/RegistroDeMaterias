from model.Data import create_table, eliminate_table
import tkinter as tk



def menu_bar(screen):
    bar = tk.Menu(screen)
    screen.config(menu = bar, width = 300, height = 300)
    
    menu_init = tk.Menu(bar, tearoff = 0)
    menu_mate = tk.Menu(bar, tearoff = 0)



    bar.add_cascade(label = 'Inicio', menu = menu_init)
    menu_init.add_command(label = 'Crear una tabla en DB', command = create_table)
    menu_init.add_command(label = 'Eliminar una tabla en DB', command = eliminate_table)
    menu_init.add_command(label = 'Salir', command = screen.destroy)

    bar.add_cascade(label = 'Materias', menu = menu_mate)
    menu_mate.add_command(label = 'Aprobadas')
    menu_mate.add_command(label = 'Desaprobadas')

def approved_quantity(list_materias):
    count = 0
    amount = 0

    for m in list_materias:
        amount += 1 
        is_float = sanitize_float(m[2])
        is_int = sanitize_int(m[2])


        if is_float or is_int:
            if float(m[2]) >= 6 and float(m[2]) <= 10:
                count += 1
    
    percentaje = calculate_percentage(count, amount) 

    return count, amount, percentaje

def calculate_percentage(count, amount):
    try:
        percentage = (count * 100) / amount
    except ZeroDivisionError:
        percentage = 0

    return int(percentage)


def sanitize_float(str):
    try:
        num = float(str)
        return True
    except ValueError:
        return False

def sanitize_int(str):
    try:
        num = int(str)
        return True
    except ValueError:
        return False