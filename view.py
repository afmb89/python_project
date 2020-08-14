#_*_ coding: utf-8 _*_
from tkinter import *
from tkinter import messagebox as msgb
from tkinter import ttk
from modulo_temas import theme_color

class view():
	
	def __init__(self, window):

		self.wind = window

		self.wind.title('Registration')

		#cambiar color
		def eleccionTema():
			color_fondo = theme_color(self)
			frame_left.config(bg=color_fondo)
			frame_right.config(bg=color_fondo)
			return

		ingrese_datos_label=Label(self.wind, width=80, height=1, bg="Purple", text="Ingrese sus datos", fg="white")
		ingrese_datos_label.grid(row=0, column=0)

		titulo_label = Label(self.wind, text="Título")
		description_label = Label(self.wind, text="Descripción")
		titulo_label.grid(row=1, column=0,sticky=W)
		description_label.grid(row=2, column=0,sticky=W)
		
		self.variables = []
		#crear variables
		for y in range(1,3):
			x = str(y)
			self.variables.append('e'+x)
		
		def ingresar_datos(valor, columna, ancho, fila):
			dato = Entry(valor, width=ancho)
			dato.grid(row=fila, column=columna)
			return dato

		entrada = 0 
		rows = 1
		while entrada < 2:
			self.variables[entrada] = ingresar_datos(self.wind, 0, 20, rows)
			entrada+=1
			rows+=1

		espacio2 = Label(self.wind).grid(row=5)
		espacio3 = Label(self.wind).grid(row=7)
		
		#boton alta_row_tabla
		self.alta_button = Button(self.wind, text="Alta")
		self.alta_button.grid(row=4, column=0,sticky=W, padx=75)
		#alta_button.config(command=self.agregar_info)

		#boton mostrar_row/s_tabla
		self.mostrar_row_button = Button(self.wind, text="Mostrar registros exitentes",width=74)
		self.mostrar_row_button.grid(row=3, column=0)
		#mostrar_row_button.config(command=self.mostrar)

		#boton baja_row
		self.eliminar_button = Button(self.wind, text="Baja")
		self.eliminar_button.grid(row=4, column=0,sticky=E, padx=280)
		#eliminar_button.config(command=self.eliminar)

		#boton modificar_row/s_tabla
		self.modificar_button = Button(self.wind, text="Modificar")
		self.modificar_button.grid(row=4, column=0,sticky=E, padx=75)
		#modificar_button.config(command=self.modificar)

		#tabla container
		self.show_info = ttk.Treeview(self.wind, height=15,selectmode='extended')
		self.show_info.grid(row=6,column=0, columnspan=2, sticky="nsew")
		self.vsb = ttk.Scrollbar(self.wind, orient="vertical", command=self.show_info.yview)
		self.vsb.grid(row=6, column=2, sticky="nsew")
		self.show_info.configure(yscrollcommand=self.vsb.set)
		self.show_info["columns"]=("#1","#2","#3","#4","#5")
		self.show_info.column("#0", width=100)
		self.show_info.column("#1", width=100)
		self.show_info.column("#2", width=100)
		self.show_info.column("#3", width=100)
		self.show_info.column("#4", width=100)
		self.show_info.column("#5", width=100)
		self.show_info.heading("#0",text="Id", anchor=CENTER)
		self.show_info.heading("#1",text="Título", anchor=CENTER)
		self.show_info.heading("#2", text="Fecha", anchor=CENTER)
		self.show_info.heading("#3", text="Descripción", anchor=CENTER)
		self.show_info.heading("#4", text="Estado", anchor=CENTER)
		self.show_info.heading("#5", text="Objeto", anchor=CENTER)

		color_label=Label(self.wind, width=80, height=1, bg="Black", text="Temas", fg="red")
		color_label.grid(row=8, column=0)

		var = IntVar()

		tema1=Radiobutton(self.wind, text="Tema 1", variable=var , value =1, command=eleccionTema, fg="red", bg="black")
		tema1.grid(row=9, sticky=N)
		tema2=Radiobutton(self.wind, text="Tema 2", variable=var , value=2, command=eleccionTema, fg="red", bg="black")
		tema2.grid(row=9)
		tema3=Radiobutton(self.wind, text="Tema 3", variable=var , value=3, command=eleccionTema, fg="red", bg="black")
		tema3.grid(row=9, sticky=S)

		frame_left = Frame(self.wind, width="250", height="100")
		frame_left.grid(row=9,sticky=W)

		frame_right = Frame(self.wind, width="250", height="100")
		frame_right.grid(row=9,sticky=E)

#afmb_89