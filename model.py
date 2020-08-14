from tkinter import messagebox as msgb
from tkinter import simpledialog as sd
#import mysql.connector as myc
import re
from peewee import *
from observer import *
import datetime

bd = SqliteDatabase('testpython_db.db')

class test_python(Model):
	id = PrimaryKeyField()
	titulo = CharField()
	descripcion = TextField()
	fecha = DateTimeField(default=datetime.datetime.now)
	estado = BooleanField(default=True)

	def __str__(self):
		campo = 'El título es ' + str(self.titulo)
		return campo

	class Meta:
		database = bd

test_python.create_table([test_python])

class model(Observable):

	def __init__(self):
		return 
	
	def visualizar(self):
		mostrar = test_python.select()
		return mostrar

	def agregar(self,dato1,dato2):
		alta = test_python()
		alta.titulo = dato1
		alta.descripcion = dato2
		alta.save()
		self.notify("depositado")
	
	def quitar(self, consulta):
		eliminar = test_python.get(test_python.id==consulta)
		eliminar.delete_instance()
		self.notify("removido")

	def actualizar(self, consulta):
		actualizar = test_python.update(titulo=consulta[0], descripcion = consulta[1]).where(test_python.id == consulta[2])
		actualizar.execute()
		self.notify("actualizado")

	def validar(self,dato1):
		global simbolos, validacion
		self.simbolos="^[A-Za-z]+(?:[ -][A-Za-z]+)*$"
		self.validacion = not re.fullmatch(self.simbolos,dato1)
		return self.validacion == True

#afmb_89