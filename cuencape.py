import tkinter as tk
from tkinter import ttk, messagebox

def mostrar_animacion(seleccion):
    if seleccion == "Brunchpe":
        messagebox.showinfo("Animación", "Animación de desayuno")
    elif seleccion == "Almuerzope":
        messagebox.showinfo("Animación", "Animación de dos personas almorzando")
    elif seleccion == "Museo":
        messagebox.showinfo("Animación", "Animación relacionada a un museo")
    elif seleccion == "cenape":
        messagebox.showinfo("Animación", "Animación de una cena romántica")
    elif seleccion == "Nadape":
        messagebox.showinfo("Animación", "Animación de un gato triste")

def actualizar_opciones_lugar():
    lugares_combobox['values'] = obtener_lugares()

def seleccionar_actividad(*args):
    actividad_seleccionada = actividad_var.get()
    actualizar_opciones_lugar()

    if actividad_seleccionada == "Brunchpe" or actividad_seleccionada == "Almuerzope" or actividad_seleccionada == "cenape" or actividad_seleccionada == "Museo":
        lugares_label.grid(row=2, column=0, pady=10)
        lugares_combobox.grid(row=2, column=1, pady=10)
    else:
        lugares_label.grid_forget()
        lugares_combobox.grid_forget()

def mostrar_lugar_seleccionado():
    lugar_seleccionado = lugares_var.get()
    messagebox.showinfo("Lugar Seleccionado", f"Has seleccionado: {lugar_seleccionado}")

def obtener_lugares():
    actividad_seleccionada = actividad_var.get()
    if actividad_seleccionada == "Brunchpe":
        return ["La croissanteria", "dos chorreras", "la jolie","simple","cafe de la sucre", "sorpresape en el cajas"]
    elif actividad_seleccionada == "Almuerzope":
        return ["la maria", "tartar", "la plazita", "la plazita", "bodega xe"]
    elif actividad_seleccionada == "Museo":
        return ["remigio crespo", "Museo de arte moderno", "pumapungo", "museo municipal"]
    elif actividad_seleccionada == "cenape":
        return ["negroni", "la guarida", "zielo", "madame", "santa lucia"]
    elif actividad_seleccionada == "Nadape":
        return ["Lugar A", "Lugar B", "Lugar C"]
    else:
        return []

def finalizar_seleccion():
    actividad_seleccionada = actividad_var.get()
    lugar_seleccionado = lugares_var.get()
    dia_actual = dia_var.get()
    historial_text.config(state=tk.NORMAL)
    historial_text.insert(tk.END, f"Día {dia_actual}: Actividad - {actividad_seleccionada}, Lugar - {lugar_seleccionado}\n")
    historial_text.config(state=tk.DISABLED)
    reiniciar_interfaz()

def generar_cronograma():
    historial = historial_text.get("1.0", tk.END).strip()

    if not historial:
        messagebox.showwarning("Advertencia", "No hay selecciones en el historial.")
        return

    # Procesar los datos del historial y generar el cronograma
    cronograma = {}

    # Separar el historial en líneas
    lineas = historial.split("\n")

    # Organizar los datos por día, actividad y lugar
    for linea in lineas:
        if linea.startswith("Día"):
            _, dia, restante = linea.split(" ", 2)
            cronograma[dia] = []
            _, actividad, lugar = restante.split(" - ")
            cronograma[dia].append((actividad, lugar))

    # Crear el texto del cronograma
    schedule_lines = ["Cronograma:"]

    for dia in dias_semana:
        schedule_lines.append(f"\n{dia}:")
        if dia in cronograma:
            for actividad, lugar in cronograma[dia]:
                schedule_lines.append(f"   {actividad}: {lugar}")

    # Unir las líneas para formar el texto del cronograma
    schedule = "\n".join(schedule_lines)

    # Crear una nueva ventana para mostrar el cronograma
    cronograma_ventana = tk.Toplevel(ventana)
    cronograma_ventana.title("Cronograma")

    # Ajustar el estilo para el cronograma
    cronograma_text = tk.Text(cronograma_ventana, height=10, width=40, font=("Times New Roman", 12))
    cronograma_text.insert(tk.END, schedule)
    cronograma_text.pack(padx=20, pady=20)
    cronograma_text.config(state=tk.DISABLED)
    cronograma_text.config(bg="black", fg="white")

def reiniciar_interfaz():
    actividad_var.set("")
    lugares_var.set("")
    lugares_label.grid_forget()
    lugares_combobox.grid_forget()
    dia_var.set("Jueves")
    actividad_combobox.focus_set()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Planificación de Actividades")

# Tamaño y posición de la ventana
ancho_ventana = 600
alto_ventana = 400
x_pantalla = (ventana.winfo_screenwidth() - ancho_ventana) // 2
y_pantalla = (ventana.winfo_screenheight() - alto_ventana) // 2

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pantalla}+{y_pantalla}")

# Variables para almacenar la selección
actividad_var = tk.StringVar()
lugares_var = tk.StringVar()
dia_var = tk.StringVar(value="Jueves")
dias_semana = ["Jueves", "Viernes", "Sábado", "Domingo"]

# Crear widgets
actividad_label = tk.Label(ventana, text=f"¿Qué hacemopes?")
actividad_combobox = ttk.Combobox(ventana, values=["Brunchpe", "Almuerzope", "Museo", "cenape", "Nadape"], textvariable=actividad_var)
actividad_combobox.bind("<<ComboboxSelected>>", seleccionar_actividad)

lugares_label = tk.Label(ventana, text="en que lugarpe:")
lugares_combobox = ttk.Combobox(ventana, values=[], textvariable=lugares_var)

dia_label = tk.Label(ventana, text="que diape:")
dia_combobox = ttk.Combobox(ventana, values=dias_semana, textvariable=dia_var)

boton_finalizar_seleccion = tk.Button(ventana, text="Finalizar Selección", command=finalizar_seleccion)
boton_generar_cronograma = tk.Button(ventana, text="Generar Cronograma", command=generar_cronograma)

historial_label = tk.Label(ventana, text="Historial de Selecciones:")
historial_text = tk.Text(ventana, height=5, width=40, state=tk.DISABLED)

# Ubicar los widgets en la ventana
actividad_label.grid(row=0, column=0, pady=10)
actividad_combobox.grid(row=0, column=1, pady=10)
dia_label.grid(row=1, column=0, pady=10)
dia_combobox.grid(row=1, column=1, pady=10)
boton_finalizar_seleccion.grid(row=3, column=0, pady=10)
boton_generar_cronograma.grid(row=3, column=1, pady=10)
historial_label.grid(row=4, column=0, pady=10)
historial_text.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()


