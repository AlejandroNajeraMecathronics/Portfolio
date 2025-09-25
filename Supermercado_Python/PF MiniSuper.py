import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import serial
import time

# Clase Principal donde se trabajara
class MiniSuperApp:

    # Inicializa el objeto con sus valores iniciales
    def __init__(self, root):
        self.root = root
        self.root.title("MiniSuper 🛒")
        self.root.geometry("1250x700")
        self.root.configure(bg="#F5F5F5")

        self.carrito = []
        self.todos_los_productos = [
            {"nombre": "Pan", "precio": 15.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Pan.png"},
            {"nombre": "Leche", "precio": 22.5, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Leche.png"},
            {"nombre": "Shampoo", "precio": 48.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Shampoo.png"},
            {"nombre": "Jabón", "precio": 12.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Jabon.png"},
            {"nombre": "Cereal", "precio": 35.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Cereal.png"},
            {"nombre": "Huevos", "precio": 42.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Huevos.png"},
            {"nombre": "Pasta Dental", "precio": 25.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Pasta dental.png"},
            {"nombre": "Arroz", "precio": 18.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Arroz.png"},
            {"nombre": "Frijoles", "precio": 20.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Frijoles.png"},
            {"nombre": "Refresco", "precio": 19.5, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Refresco.png"},
            {"nombre": "Galletas", "precio": 24.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Galletas.png"},
            {"nombre": "Yogur", "precio": 14.5, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Yogurt.png"},
            {"nombre": "Aceite", "precio": 55.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Aceite.png"},
            {"nombre": "Jugo", "precio": 16.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Jugo.png"},
            {"nombre": "Papel Higiénico", "precio": 33.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Papel higienico.png"},
            {"nombre": "Detergente", "precio": 40.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Detergente.png"},
            {"nombre": "Queso", "precio": 38.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Queso.png"},
            {"nombre": "Salchichas", "precio": 36.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Salchichas.png"},
            {"nombre": "Harina", "precio": 17.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Harina.png"},
            {"nombre": "Sopa Instantánea", "precio": 10.0, "imagen": r"C:\Users\OscAl\OneDrive\Documentos\Python projects\Proyecto Final Diseño Interfaces\Imagenes\Sopa Instantanea.png"},
        ]

        # Colores de la interfaz
        self.COLOR_BARRA_SUPERIOR = "#1736B8"
        self.COLOR_FONDO_GENERAL = "#EBEBEB"
        self.COLOR_MENU = "#D6D6D6"
        self.COLOR_TEXTO = "#333333"
        self.COLOR_TARJETA = "#FFF4F4"
        self.COLOR_BOTON = "#2196F3"
        self.COLOR_VERDE = "#008f39"

        # Le pasa la lista de productos completa a la interfaz
        self.crear_interfaz(self.todos_los_productos)

    # Arma toda la interfaz visual
    def crear_interfaz(self, lista_productos):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Barra de título
        barra = tk.Frame(self.root, bg=self.COLOR_BARRA_SUPERIOR, height=60)
        barra.pack(fill="x")
        titulo = tk.Label(barra, text="MiniSuper 🛒", fg="white", bg=self.COLOR_BARRA_SUPERIOR, font=("Helvetica", 40, "bold"))
        titulo.pack(pady=10)

        # Menú superior
        menu = tk.Frame(self.root, bg=self.COLOR_MENU, height=40)
        menu.pack(fill="x")

        opciones = [
            ("☰ Todo", lambda: self.crear_interfaz(self.todos_los_productos)),
            ("Lo Más Vendido", lambda: self.crear_interfaz(self.todos_los_productos[:5])),
            ("Promociones", lambda: self.crear_interfaz([p for p in self.todos_los_productos if p["precio"] < 20])),
            ("Servicio al Cliente", self.abrir_servicio),
            ("🛒 Ver Carrito", self.abrir_carrito),
        ]

        for texto, accion in opciones:
            lbl = tk.Label(menu, text=texto, bg=self.COLOR_MENU, fg=self.COLOR_TEXTO, font=("Helvetica", 14, "bold" if texto in ["☰ Todo", "🛒 Ver Carrito"] else "normal"), cursor="hand2")
            lbl.pack(side="left", padx=60, pady=5)
            lbl.bind("<Button-1>", lambda e, a=accion: a())

        # Scroll
        contenedor = tk.Frame(self.root)
        contenedor.pack(fill="both", expand=True)

        canvas = tk.Canvas(contenedor, bg=self.COLOR_FONDO_GENERAL)
        scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        frame_productos = tk.Frame(canvas, bg=self.COLOR_FONDO_GENERAL)
        canvas.create_window((0, 0), window=frame_productos, anchor="nw")

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame_productos.bind("<Configure>", on_frame_configure)
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # Tarjetas
        for i, p in enumerate(lista_productos):
            fila = i // 4
            columna = i % 4

            tarjeta = tk.Frame(frame_productos, bg=self.COLOR_TARJETA, relief="solid", width=220, height=240)
            tarjeta.grid(row=fila, column=columna, padx=42, pady=30)
            tarjeta.grid_propagate(False)

            # Cargar imagen
            imagen_original = Image.open(p["imagen"])
            imagen_redimensionada = imagen_original.resize((220, 250)) 
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

            # Guardar referencia para que no se elimine
            if not hasattr(self, 'imagenes'):
                self.imagenes = []  # lista para mantener referencias vivas
            self.imagenes.append(imagen_tk)

            # Mostrar imagen
            label_imagen = tk.Label(tarjeta, image=imagen_tk, bg=self.COLOR_TARJETA)
            label_imagen.pack(pady=5)

            info = tk.Frame(tarjeta, bg="white")
            info.pack(fill="x", pady=(5, 0))
            tk.Label(info, text=p["nombre"], bg="white", fg=self.COLOR_TEXTO, font=("Helvetica", 13, "bold")).pack()
            tk.Label(info, text=f"${p['precio']:.2f}", bg="white", fg=self.COLOR_VERDE, font=("Helvetica", 12, "bold")).pack()

            tk.Button(tarjeta, text="+ Agregar", bg=self.COLOR_BOTON, fg="white", font=("Helvetica", 13, "bold"), command=lambda prod=p: self.agregar_al_carrito(prod)).pack(pady=5)

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        messagebox.showinfo("Carrito", f"Agregado {producto['nombre']} al carrito 🛒")
        mensaje = f"Producto:|{producto['nombre']} ${producto['precio']:.2f}"
        self.enviar_a_arduino(mensaje)

    def abrir_carrito(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Carrito de Compras 🛒")
        ventana.geometry("400x400")
        ventana.configure(bg="#FFFFFF")

        tk.Label(ventana, text="Productos en tu carrito:", font=("Helvetica", 14, "bold"), bg="#FFFFFF").pack(pady=10)
        total = 0
        for index, item in enumerate(self.carrito):
            frame_item = tk.Frame(ventana, bg="#FFFFFF")
            frame_item.pack(fill="x", padx=20, pady=2)

            tk.Label(frame_item, text=f"{item['nombre']} - ${item['precio']:.2f}", bg="#FFFFFF", font=("Helvetica", 10)).pack(side="left")

            btn_eliminar = tk.Button(frame_item, text="X", bg="#D32F2F", fg="white", font=("Helvetica", 8, "bold"),
                                     command=lambda i=index: self.eliminar_del_carrito(i, ventana))
            btn_eliminar.pack(side="right")

            total += item["precio"]

        tk.Label(ventana, text=f"\nTotal: ${total:.2f}", font=("Helvetica", 12, "bold"), bg="#FFFFFF", fg="#4CAF50").pack(pady=10)
        tk.Button(ventana, text="Pagar", bg="#388E3C", fg="white", font=("Helvetica", 10, "bold"),
                  command=lambda: self.finalizar_compra(ventana)).pack(pady=5)

    def eliminar_del_carrito(self, index, ventana_carrito):
        producto_eliminado = self.carrito.pop(index)
        messagebox.showinfo("Eliminado", f"{producto_eliminado['nombre']} fue eliminado del carrito.")
        ventana_carrito.destroy()
        self.abrir_carrito()  # Volver a abrir el carrito actualizado

    def finalizar_compra(self, ventana):
        messagebox.showinfo("Compra Exitosa", "Gracias por tu compra 🧳✅")

        if not self.carrito:
            messagebox.showinfo("Ticket", "El carrito está vacío.")
            return

        total = sum(p['precio'] for p in self.carrito)
        ticket_texto = "----- TICKET DE COMPRA -----\n"
        for p in self.carrito:
            ticket_texto += f"{p['nombre']} - ${p['precio']:.2f}\n"
        ticket_texto += "-----------------------------\n"
        ticket_texto += f"TOTAL: ${total:.2f}\n"

        ventana_ticket = tk.Toplevel(self.root)
        ventana_ticket.title("Ticket de Compra")
        tk.Label(ventana_ticket, text=ticket_texto, font=("Courier", 11), justify="left").pack(padx=10, pady=10)

        self.enviar_a_arduino(f"Total: ${total:.2f}|Gracias por su compra")

        self.carrito.clear()
        ventana.destroy()

    def abrir_servicio(self):
        messagebox.showinfo("Servicio al Cliente", "¿Necesitas ayuda?\n\n📞 Teléfono: 656-123-4567\n📧 Correo: contacto@minisuper.com")

    def enviar_a_arduino(self, texto):
        try:
            arduino = serial.Serial('COM3', 9600, timeout=1)
            time.sleep(2.5)
            
            arduino.write((texto + "\n").encode())
            time.sleep(0.5)
            
            arduino.close()
        except Exception as e:
            print("Error al enviar a Arduino:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniSuperApp(root)
    root.mainloop()

