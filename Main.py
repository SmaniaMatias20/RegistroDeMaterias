import tkinter as tk
from client.GUI_app import Frame
from client.GUI_config import menu_bar

def main():
    screen = tk.Tk()
    screen.title("Registro de Materias")

    screen.resizable(0,0)

    menu_bar(screen)

    # screen.iconbitmap("ruta")
    app = Frame(screen)
    app.mainloop()

if __name__ == '__main__':
    main()  