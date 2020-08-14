#_*_ coding: utf-8 _*_
from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox as msgb
from model import model
from view import view
from observer import *


class controller():

	def __init__(self, root):
		self.root = root
		self.programa = view(self.root)
		self.administradora = model()
		self.programa.mostrar_row_button.config(command=self.mostrar)
		self.programa.alta_button.config(command=self.agregar_info)
		self.programa.eliminar_button.config(command=self.eliminar)
		self.programa.modificar_button.config(command=self.modificar)
		self.observador = Watcher(self.administradora)

	# limpiar y cursor de los entrys
	def limpiar(self):
		self.programa.variables[0].delete(0, END)
		self.programa.variables[1].delete(0, END)
		self.programa.variables[0].focus()

	# mostrar registros
	def mostrar(self):		
		records = self.programa.show_info.get_children()
		for element in records:
			self.programa.show_info.delete(element)

		get_filas = self.administradora.visualizar()
		for get_fila in get_filas:
			self.programa.show_info.insert('',0,text=get_fila.id,values=(get_fila.titulo,get_fila.fecha.strftime("%Y-%m-%d %H:%M:%S"),get_fila.descripcion,get_fila.estado, get_fila))

	# insert registro	
	def agregar_info(self):
		if self.administradora.validar(self.programa.variables[0].get()) == True:
			msgb.showwarning("Cuidado", "Completaste en Título?")
			self.programa.variables[0].focus()
		else:
			self.administradora.agregar(self.programa.variables[0].get(), self.programa.variables[1].get())
			self.mostrar()
			self.limpiar()		

	# delete registros	
	def eliminar(self):
		if not self.programa.show_info.item(self.programa.show_info.selection())['text']:
			msgb.showwarning("Cuidado","No elegiste nada")
		else:
			fila_id = (str(self.programa.show_info.item(self.programa.show_info.selection())['text']), )
			self.administradora.quitar(fila_id)
			self.mostrar()
		

	# update registro	
	def modificar(self):
		global titulo_nuevo, descripcion_nueva, id_fila

		if not self.programa.show_info.item(self.programa.show_info.selection())['text']:
			msgb.showwarning("Cuidado","No elegiste nada")
		else:
			self.id_fila = self.programa.show_info.item(self.programa.show_info.selection())['text']
			self.titulo_viejo = self.programa.show_info.item(self.programa.show_info.selection())['values'][0]
			self.descripcion_viejo = self.programa.show_info.item(self.programa.show_info.selection())['values'][2]
			self.edit_wind = Toplevel()
			self.edit_wind.geometry("300x200")
			self.edit_wind.title('Modificar información')
			Label(self.edit_wind).grid(row=0)
			Label(self.edit_wind, text='Título: ').grid(row=1,column=1,sticky=W)
			Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value=self.titulo_viejo), state='readonly').grid(row=1,column=2,sticky=W)
			Label(self.edit_wind, text='Nuevo Título: ').grid(row=2,column=1,sticky=W)
			self.titulo_nuevo = Entry(self.edit_wind)
			self.titulo_nuevo.grid(row=2, column=2)
			Label(self.edit_wind, text='Descripción: ').grid(row=4,column=1,sticky=W)
			Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value=self.descripcion_viejo), state='readonly').grid(row=4,column=2,sticky=W)
			Label(self.edit_wind, text='Nueva Descripción: ').grid(row=5,column=1,sticky=W)
			self.descripcion_nueva = Entry(self.edit_wind)
			self.descripcion_nueva.grid(row=5, column=2)
			Label(self.edit_wind).grid(row=6)		
			self.actualizar_button = Button(self.edit_wind, text="Actualizar", command=lambda:self.actualizar(self.titulo_nuevo.get(), self.descripcion_nueva.get(), self.id_fila))
			self.actualizar_button.grid(row=7, column=2,sticky=W)

	def actualizar(self,titulo_nuevo, descripcion_nueva, id_fila):
		update_parameters = (str(self.titulo_nuevo.get()), str(self.descripcion_nueva.get()), str(self.id_fila))
		self.administradora.actualizar(update_parameters)
		self.mostrar()
		self.edit_wind.destroy()
		msgb.showinfo('Alta', 'Modificaste:' + '\n-Título: ' + str(self.titulo_viejo) + '\n-Descripción: ' + str(self.descripcion_viejo) + '\n\nPor' + '\n-Título: ' + update_parameters[0] + '\n-Descripción: ' + update_parameters[1])
		

#afmb_89