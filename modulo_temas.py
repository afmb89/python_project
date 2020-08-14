from tkinter import colorchooser

def theme_color(self):
	global color, color_name
	color = colorchooser.askcolor(title = "Elegí tu color")
	color_name = color[1]
	return color_name


#afmb_89