from model.Materia import Materia
from .ConectionDB import ConectionDB
from tkinter import messagebox
import sqlite3

def create_table():
    conection = ConectionDB()
    
    sentence = '''
    CREATE TABLE materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NULL,
    qualification INTEGER NULL,
    state VARCHAR(100) NULL
    )
    '''

    try:
        conection.cursor.execute(sentence)
        conection.close()
        tittle = 'Crear Registro'
        message = 'Se creó la tabla en la base de datos'
        messagebox.showinfo(title = tittle, message = message)
    except:
        tittle = 'Crear Registro'
        message = 'La tabla ya ha sido creada'
        messagebox.showwarning(title = tittle, message = message)

def eliminate_table():
    conection = ConectionDB()

    sentence = '''
    DROP TABLE materias
    '''
    try:
        conection.cursor.execute(sentence)
        conection.close()
        tittle = 'Eliminar Registro'
        message = 'La tabla se elimino con exito'
        messagebox.showinfo(title = tittle, message = message)
    except:
        tittle = 'Eliminar Registro'
        message = 'No hay tabla para borrar'
        messagebox.showerror(title = tittle, message = message)


    
def save(materia: Materia):
    conection = ConectionDB()


    try: 
        if float(materia.qualification) >= 0 and float(materia.qualification) <= 10: 
            sentence = f"""
            INSERT INTO materias (name, qualification, state) VALUES ('{materia.name}', {materia.qualification}, '{materia.state}')
            """
            conection.cursor.execute(sentence)
            conection.close()
        else:
            raise ValueError       
    except ValueError:
        tittle = 'Guardar datos'
        message = 'Debe ingresar un numero entre 0 y 10 en Nota Final'
        messagebox.showwarning(title = tittle, message = message)
    except Exception:
        tittle = 'Conexion al Registro'
        message = 'No hay tabla para insertar los datos'
        messagebox.showerror(title = tittle, message = message)        

def show():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias ORDER BY qualification DESC  
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias

def edit(materia: Materia, id):
    conection = ConectionDB()

    
    sentence = f"""
    UPDATE materias
    SET name = '{materia.name}', qualification = {materia.qualification}, state = '{materia.state}' 
    WHERE id = {id}
    """

    try:
        if float(materia.qualification) >= 0 and float(materia.qualification) <= 10: 
            conection.cursor.execute(sentence)
            conection.close()
        else:
            raise ValueError
    except ValueError:
        tittle = 'Guardar datos'
        message = 'Debe ingresar un numero entre 0 y 10 en Nota Final'
        messagebox.showwarning(title = tittle, message = message)
    except Exception:
        tittle = 'Actualizar Registro'
        message = 'No se ha podido actualizar el registro'
        messagebox.showerror(title = tittle, message = message)

def eliminate(id):
    conection = ConectionDB()

    sentence = f"""
    DELETE FROM materias WHERE id = {id}
    """

    try:
        conection.cursor.execute(sentence)
        conection.close()
    except:
        tittle = 'Eliminar Registro'
        message = 'No se ha podido eliminar el registro'
        messagebox.showerror(title = tittle, message = message)


def show_approved():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias WHERE qualification >= 6 AND qualification <= 10 ORDER BY qualification DESC 
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias 

def show_disapproved():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias WHERE qualification < 4 AND qualification >= 1 ORDER BY qualification DESC  
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias 

def show_final():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias WHERE qualification < 6 AND qualification >= 4 ORDER BY qualification DESC 
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias 

def show_unrealized():
    conection = ConectionDB() 

    list_materias = []

    sentence = """
    SELECT * FROM materias WHERE qualification == 0
    """

    try:
        conection.cursor.execute(sentence)
        list_materias = conection.cursor.fetchall()
        conection.close()
    except:
        tittle = 'Obtener Registros'
        message = 'No hay tabla para obtener los datos'
        messagebox.showwarning(title = tittle, message = message)
        
    return list_materias 
