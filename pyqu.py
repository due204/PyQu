from qrcode import QRCode
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Spinbox
from tkinter import messagebox


class Pyqrdue:
    def __init__(self, parent):
        # Vista principal
        self.parent = parent
        self.parent.title("PyQu")
        vent_x = self.parent.winfo_screenwidth() // 2 - 200 // 2
        vent_y = self.parent.winfo_screenheight() // 2 - 150 // 2
        tam_y_pos = "350x" + "200+" + str(vent_x) + "+" + str(vent_y)
        self.parent.geometry(tam_y_pos)  # Ancho, largo y posicion
        self.parent.resizable(False, False)
        self.parent.bind("<KeyPress-Escape>", self.salir)
        # Variasbles de control
        self.entra = StringVar()
        self.versi = IntVar()
        self.taman = IntVar()
        self.borde = IntVar()
        # Seteamos las variables
        self.versi.set(3)
        self.taman.set(20)
        self.borde.set(2)
        self.vista()

    # widgets
    def vista(self):
        self.label_texto_entrada = Label(root, text="Ingrese el texto")
        self.label_texto_entrada.place(x=120, y=0)

        self.entry_texto_entrada = Entry(
            root,
            width=40,
            textvariable=self.entra,
        )
        self.entry_texto_entrada.place(x=10, y=20)

        self.label_texto_version = Label(root, text="Version QR")
        self.label_texto_version.place(x=10, y=60)
        self.spinbox_version = Spinbox(
            root,
            from_=1,
            to=5,
            textvariable=self.versi,
        )
        self.spinbox_version.place(x=20, y=100, width=40)

        self.label_texto_size = Label(root, text="Tamaño")
        self.label_texto_size.place(x=140, y=60)
        self.spinbox_size = Spinbox(
            root,
            from_=10,
            to=50,
            textvariable=self.taman,
        )
        self.spinbox_size.place(x=140, y=100, width=50)

        self.label_texto_bordes = Label(root, text="Bordes")
        self.label_texto_bordes.place(x=260, y=60)
        self.spinbox_bordes = Spinbox(
            root,
            from_=1,
            to=15,
            textvariable=self.borde,
        )
        self.spinbox_bordes.place(x=260, y=100, width=50)

        self.boton = Button(root, text="Crear", command=self.crear)
        self.boton.place(x=260, y=150)

    def crear(self):
        self.tex = self.entra.get()
        self.ver = self.versi.get()
        self.tam = self.taman.get()
        self.bor = self.borde.get()

        if not self.tex:
            messagebox.showinfo(
                title="Campos incompletos",
                message="Debes ingresar un texto.",
            )
        else:
            qr = QRCode(version=self.ver, box_size=self.tam, border=self.bor)

            qr.add_data(self.tex)
            qr.make(fit=True)

            imagen = qr.make_image(fill="black", back_color="white")
            imagen.save("pyqu_imagen.png")
            messagebox.showinfo(
                title="Exito",
                message="Imagen QR generada exitosamente.",
            )
            self.salir()

    def salir(self, *args):
        self.parent.destroy()
        self.parent.quit()
        print("Saliendo del programa")


if __name__ == "__main__":
    root = Tk()
    Pyqrdue(root)
    root.mainloop()
