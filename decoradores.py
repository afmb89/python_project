def alta_decorador(funcion):

	def inner_function(*args,**kwargs):

		funcion(*args)

		print("Se agregó un nuevo registro")

	return inner_function

def baja_decorador(funcion):

	def inner_function(*args,**kwargs):

		funcion(*args)

		print("Se eliminó un registro")

	return inner_function

def actualizar_decorador(funcion):

	def inner_function(*args,**kwargs):

		funcion(*args)

		print("Se modificó un registro")

	return inner_function

#afmb_89