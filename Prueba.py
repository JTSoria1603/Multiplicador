import random
import time
import tkinter as tk
from PIL import Image, ImageTk

class CalculadoraMultiplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        
        self.imagen_de_fondo = Image.open('Lastenia.png')
        self.imagen_de_fondo = self.imagen_de_fondo.resize((1200, 800), Image.BILINEAR)
        self.imagen_de_fondo = ImageTk.PhotoImage(self.imagen_de_fondo)
        
        fondo_label = tk.Label(ventana, image=self.imagen_de_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.numero1_label = tk.Label(ventana, text="Número 1: ")
        self.numero1_label.place(x=50, y=50)
        self.numero2_label = tk.Label(ventana, text="Número 2: ")
        self.numero2_label.place(x=50, y=80)
        self.resultado_label = tk.Label(ventana, text="")
        self.resultado_label.place(x=50, y=140)
        
        self.cronometro_label = tk.Label(ventana, text="Tiempo transcurrido: 0:00:00")
        self.cronometro_label.place(x=50, y=170)

        self.multiplicar_button = tk.Button(ventana, text="Multiplicacion", command=self.iniciar_cronometro)
        self.multiplicar_button.place(x=50, y=220)

        self.resultado_button = tk.Button(ventana, text="Resultado", command=self.boton_resultado)
        self.resultado_button.place(x=50, y=250)
        
        self.tiempo_inicial = 0
        

    def iniciar_cronometro(self):
        self.tiempo_inicial = time.time()
        self.actualizar_cronometro()
        self.mostrar_numeros()
    
    def detener_cronometro(self):
        self.ventana.after_cancel(self.actualizar_cronometro)
    

    def actualizar_cronometro(self):
        tiempo_transcurrido = time.time() - self.tiempo_inicial
        minutos = int(tiempo_transcurrido // 60)
        segundos = int(tiempo_transcurrido % 60)
        horas = minutos // 60
        minutos = minutos % 60
        tiempo_formateado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        self.cronometro_label.config(text=f"Tiempo transcurrido: {tiempo_formateado}")
        if tiempo_transcurrido < 20:
            self.ventana.after(1000, self.actualizar_cronometro)
        else:
            self.mostrar_resultado()

    def mostrar_numeros(self):
        numero1 = random.randint(0, 9)
        numero2 = random.randint(0, 9)
        self.numero1_label.config(text=f"Número 1: {numero1}")
        self.numero2_label.config(text=f"Número 2: {numero2}")

    def mostrar_resultado(self):
        numero1 = int(self.numero1_label.cget("text").split()[-1])
        numero2 = int(self.numero2_label.cget("text").split()[-1])
        resultado = numero1 * numero2
        self.resultado_label.config(text=f"Resultado: {resultado}")
    
    def boton_resultado(self):
        self.mostrar_resultado()
        self.detener_cronometro()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraMultiplicacion(ventana)
    ventana.mainloop()