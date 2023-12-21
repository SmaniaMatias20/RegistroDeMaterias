
def get_statistics(list_materias):
    count = 0
    amount = 0
    accumulator = 0
    coursed = 0

    for m in list_materias:
        amount += 1 

        if m[2] >= 6 and m[2] <= 10:
            count += 1

        if m[2] >= 1 and m[2] <= 10:
            coursed += 1 
            accumulator += m[2]
            

    average = get_average(accumulator, coursed)
    percentaje = get_percentage(count, amount) 

    return count, amount, percentaje, average

def get_percentage(count, amount):
    try:
        percentage = (count * 100) / amount
    except ZeroDivisionError:
        percentage = 0

    return int(percentage)

def get_average(acumulator, amount):

    try:
        average = acumulator / amount
    except ZeroDivisionError:
        average = 0

    return round(average, 2)

# def sanitize_float(str):
#     try:
#         num = float(str)
#         return True
#     except ValueError:
#         return False

# def sanitize_int(str):
#     try:
#         num = int(str)
#         return True
#     except ValueError:
#         return False