import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from client.GUI_config import approved_quantity
from model.Data import edit, eliminate, show
from model.Data import Materia, save

class Frame(tk.Frame):
    def __init__(self, screen = None):
        super().__init__(screen, width = 800, height = 500)
        self.screen = screen
        self.pack()
        self.id = None
        self.name_var = tk.StringVar()
        self.state_var = tk.StringVar()
        self.qualification_var = tk.StringVar()

        self.update()
        self.disable_fields()


        # self.config(bg = 'black')

    def update(self):
        self.update_table()
        self.fields()

    def fields(self):

        self.create_labels()

        self.create_entrys()
        
        self.create_botons()
        

    def create_labels(self):

        self.label_name = tk.Label(self, text = "Nombre de la Materia")
        self.label_name.config(font = ('Arial Black', 12), padx = 10, pady = 10)
        self.label_name.grid(row = 0, column = 0, columnspan = 2)

        self.label_qualification = tk.Label(self, text = "Nota final")
        self.label_qualification.config(font = ('Arial Black', 12), padx = 10, pady = 10)
        self.label_qualification.grid(row = 2, column = 0, columnspan = 2)

        self.label_state = tk.Label(self, text = "Estado")
        self.label_state.config(font = ('Arial Black', 12), padx = 10, pady = 10)
        self.label_state.grid(row = 4, column = 0, columnspan = 2)

        self.label_quantity = tk.Label(self, text = "Aprobadas")
        self.label_quantity.config(font = ('Arial Black', 20), padx = 10, pady = 10)
        self.label_quantity.grid(row = 1, column = 2)

        self.label_quantity = tk.Label(self, text = f"{self.count[0]}/{self.count[1]}")
        self.label_quantity.config(font = ('Arial Black', 20), padx = 10, pady = 10)
        self.label_quantity.grid(row = 2, column = 2)

        self.label_quantity = tk.Label(self, text = "Porcentaje")
        self.label_quantity.config(font = ('Arial Black', 20), padx = 10, pady = 10)
        self.label_quantity.grid(row = 3, column = 2)

        self.label_quantity = tk.Label(self, text = f" {self.count[2]}% ")
        self.label_quantity.config(font = ('Arial Black', 20), padx = 10, pady = 10)
        self.label_quantity.grid(row = 4, column = 2)
    
    def create_entrys(self):
        self.entry_name = tk.Entry(self, textvariable = self.name_var)
        self.entry_name.config(width = 50, font = ('Arial', 12))
        self.entry_name.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 2)

        self.entry_qualification = tk.Entry(self, textvariable = self.qualification_var)
        self.entry_qualification.config(width = 50, font = ('Arial', 12))
        self.entry_qualification.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 2)

        
        self.entry_state = tk.Entry(self, textvariable = self.state_var)
        self.entry_state.config(width = 50, font = ('Arial', 12))
        self.entry_state.grid(row = 5, column = 0, padx = 10, pady = 10, columnspan = 2)

    def create_botons(self):
        self.btn_new = tk.Button(self, text = 'Nuevo', command = self.enable_fields)
        self.btn_new.config(width = 20, font = ('Arial Black', 12), fg = 'white', bg = '#158645', cursor = 'hand2', activebackground = '#158645')
        self.btn_new.grid(row = 6, column = 0, padx = 10, pady = 10)

        self.btn_save = tk.Button(self, text = 'Guardar', command = self.save_data)
        self.btn_save.config(width = 20, font = ('Arial Black', 12), fg = 'white', bg = '#1658A2', cursor = 'hand2', activebackground = '#1658A2')
        self.btn_save.grid(row = 6, column = 1, padx = 10, pady = 10)

        self.btn_cancel = tk.Button(self, text = 'Cancelar', command = self.disable_fields)
        self.btn_cancel.config(width = 20, font = ('Arial Black', 12), fg = 'white', bg = '#BD152E', cursor = 'hand2', activebackground = '#BD152E')
        self.btn_cancel.grid(row = 6, column = 2, padx = 10, pady = 10)

        self.btn_edit = tk.Button(self, text = 'Editar', command = self.edit_data)
        self.btn_edit.config(width = 20, font = ('Arial Black', 12), fg = 'white', bg = '#158645', cursor = 'hand2', activebackground = '#158645')
        self.btn_edit.grid(row = 8, column = 0, padx = 10, pady = 10)

        self.btn_eliminate = tk.Button(self, text = 'Eliminar', command = self.eliminate_data)
        self.btn_eliminate.config(width = 20, font = ('Arial Black', 12), fg = 'white', bg = '#BD152E', cursor = 'hand2', activebackground = '#BD152E')
        self.btn_eliminate.grid(row = 8, column = 1, padx = 10, pady = 10)

    def create_table(self):
        self.table = ttk.Treeview(self, column = ('ID', 'Nombre', 'Nota Final'))
        self.table.grid(row = 7, column = 0, columnspan = 3, sticky = 'nse', padx = 20)

        self.scroll = ttk.Scrollbar(self, orient = 'vertical', command = self.table.yview)
        self.scroll.grid(row = 7, column = 4, sticky = 'nse')
        self.table.configure(yscrollcommand = self.scroll.set)


    def enable_fields(self):
        self.state_var.set('')
        self.name_var.set('')
        self.qualification_var.set('')
        
        self.entry_name.config(state = 'normal')
        self.entry_qualification.config(state = 'normal')
        self.entry_state.config(state = 'normal')

        self.btn_save.config(state = 'normal')
        self.btn_cancel.config(state = 'normal')

    def disable_fields(self):
        self.id = None
        self.state_var.set('')
        self.name_var.set('')
        self.qualification_var.set('')

        self.entry_name.config(state = 'disabled')
        self.entry_qualification.config(state = 'disabled')
        self.entry_state.config(state = 'disabled')

        self.btn_save.config(state = 'disabled')
        self.btn_cancel.config(state = 'disabled')

    def save_data(self):
        materia = Materia(self.name_var.get(), self.qualification_var.get(), self.state_var.get())
        
        if self.id == None:
            save(materia)
        else:
            edit(materia, self.id)

        self.update()

        self.disable_fields()
    
        
    
    def update_table(self):
        self.list_materias = show()
        self.list_materias.reverse()
        self.count = approved_quantity(self.list_materias)

        self.create_table()

        self.table.heading('#0', text = 'ID')
        self.table.heading('#1', text = 'NOMBRE')
        self.table.heading('#2', text = 'NOTA FINAL')
        self.table.heading('#3', text = 'ESTADO')
        
        for m in self.list_materias:
            self.table.insert('', 0, text = m[0], values = (m[1], m[2], m[3]))


    def edit_data(self):
        try:
            self.id = self.table.item(self.table.selection())['text']
            self.name = self.table.item(self.table.selection())['values'][0]
            self.qualification = self.table.item(self.table.selection())['values'][1]
            self.state = self.table.item(self.table.selection())['values'][2]

            self.enable_fields()

            self.entry_name.insert(0, self.name)
            self.entry_qualification.insert(0, self.qualification)
            self.entry_state.insert(0, self.state)
        except:
            tittle = 'Edicion de Registro'
            message = 'No ha seleccionado ningun registro'
            messagebox.showwarning(title = tittle, message = message)
    
    def eliminate_data(self):
        try:
            self.id = self.table.item(self.table.selection())['text']
            eliminate(self.id)

            # Update table
            self.update()
            self.id = None
        except:
            tittle = 'Eliminacion de Registro'
            message = 'No ha seleccionado ningun registro'
            messagebox.showwarning(title = tittle, message = message)
            



