from swampy.Gui import *

a = Gui()
a.title('Alberto')

def boton1():
	a.bu(text='Presioname otra vez.', command=boton2)

def boton2():
	a.la(text='Buen trabajo.')

a.bu(text='Presioname.', command=boton1)

a.mainloop()              