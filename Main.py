import tkinter as tk
from client.GUI_app import Frame
from client.GUI_app import *

def main():
    screen = tk.Tk()
    screen.title("Registro de Materias")

    screen.resizable(0,0)
    screen.config(bg = 'black')

    # screen.iconbitmap("ruta")
    app = Frame(screen)

    app.mainloop()


if __name__ == '__main__':
    main()  