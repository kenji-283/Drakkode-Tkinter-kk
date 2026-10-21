import tkinter as tk

class AplicacionDrakkode:
	
	def __init__(self, ventana):
		self.ventana=ventana
		
#Ajustes de la ventana en tkinter

		self.ventana.title("Drakkode: Software y Tecnologias")
		#titulo de la ventana
		self.ventana.geometry("600x750")
		#tamaño de la ventana
		self.ventana.resizable(False, False)
		#configuracion de escala de la ventana, por defecto en falso,se puede cambiar
		self.ventana.config(bg="#08102E")
		#color de la ventana, rgb hexadecimal, azul oscuro
		self.mostrar_login()
		#mostrar el login obviamente
	def mostrar_login(self):
	#Titulooooo	
		self.titulo = tk.Label(self.ventana, text="DRAKKODE", 
		font=("Arial", 24, "bold"),
		bg="#08102E", 
		fg="#2F7EF7")

		self.titulo.pack(pady=(35, 5))
		
		#Subtitulo
		self.subtitulo = tk.Label(
		self.ventana, text="SOFTWARE Y TECNOLOGIAS", 
		font=("Arial", 10, "bold"),
		bg="#08102E", 
		fg="#2F7EF7")

		self.subtitulo.pack(pady=(0, 25))
		
		#panel del formulario	
		self.form_log = tk.Frame(
		self.ventana,
		bg="#0F1D34")
		
		self.form_log.pack(padx=40, fill="x")
		#Subtitulo
		self.subtitulo3 = tk.Label(
		self.form_log, text="Iniciar sesión", 
		font=("Arial", 8, "bold"),
		bg="#08102E", 
		fg="#2F7EF7")

		self.subtitulo3.pack(pady=(0, 10))
		
		#etiquetas del usuario
		self.etiqueta1= tk.Label(self.form_log,
		text="Correo Electronico",
		font=("Arial",10, "bold"),
		bg="#0F1D34",
		fg="#FFFFFF")

		self.etiqueta1.pack(pady=(0, 5), padx=20, anchor="w")
	#entrada del usuario, entry
		self.entrada1= tk.Entry(self.form_log,
		width=30, font=("Arial", 11), bg="#162640", insertbackground="#FFFFFF", relief="flat")

		self.entrada1.pack(fill="x", padx=20, ipady=8)
		
	#etiqueta de contraseña
		self.etiqueta2= tk.Label(self.form_log,
		text="Contraseña",
		font=("Arial",10, "bold"),
		bg="#0F1D34",
		fg="#FFFFFF")

		self.etiqueta2.pack(pady=(0, 5), padx=20, anchor="w")
	#entrada del usuario, entry
		self.entrada2= tk.Entry(self.form_log,
		width=30, font=("Arial", 11), bg="#162640", insertbackground="#FFFFFF", relief="flat", show="X")

		self.entrada2.pack(fill="x", padx=20, ipady=8)
		#Mensaje de registrarse!!!
		self.mensajereg= tk.Label(self.form_log,
		text="No tienes cuenta?, Registrate!",
		bg="#08101E",
		fg="#FFFFFF")

		#boton de registrarse
		self.botonreg= tk.Button(self.form_log,
	text="Registrarse", 
	font=("Arial", 10),
	bg="#08103E",
	fg="#FFFFFF", 
	cursor="hand2", 
	command=self.pagina_reg)

		self.botonin= tk.Button(self.form_log,
	text="Iniciar Sesión",
	font=("Arial",10, "bold"),
	bg="#08103F",
	fg="#FFFFFF",
	cursor="hand2", 
	command= self.iniciar_sesion)
	#lugares donde van a estar los botones y el mensaje de registro puestos en orden de salida
		self.botonin.pack(padx=20, pady=(30, 15), ipady=8)
		self.mensajereg.pack(pady=(5, 10))
		self.botonreg.pack(pady=(0, 25), padx=20, ipady=8)
		
	#aqui termina el login, que tortura	
	
	#metodo de inicio de sesion
	def iniciar_sesion(self):
		usuario= self.entrada1.get()
		contraseña= self.entrada2.get()
	#variables de inicio de sesion
		if usuario == "" or contraseña == "":
			from tkinter import messagebox
			
			#mensaje de alerta si no se los campos estan vacios
			messagebox.showwarning("Campos vacios","Introduce tu correo y contraseña.")
			return 
		
		from tkinter import messagebox
		
		messagebox.showinfo("Drakkode","Los campos se han llenado correctamente!, la autenticación se implementara proximamente")
	
	#funcion de registro, crea una nueva ventana
	def pagina_reg(self):
		#ocultar el formulario anterior de inicio para mostrar el de registro
		self.form_log.pack_forget()
		
		
		
		#panel del formulario	
		self.form_reg = tk.Frame(
		self.ventana,
		bg="#0F1D34")
		
		self.form_reg.pack(padx=40, fill="x")
		#Subtitulo
		self.subtitulo2 = tk.Label(
		self.form_reg, text="Registrarse", 
		font=("Arial", 8, "bold"),
		bg="#08102E", 
		fg="#2F7EF7")

		self.subtitulo2.pack(pady=(0, 10))
		
		#etiquetas del usuario
		self.etiqueta22= tk.Label(self.form_reg,
		text="Correo Electronico",
		font=("Arial",10, "bold"),
		bg="#0F1D34",
		fg="#FFFFFF")

		self.etiqueta22.pack(pady=(0, 5), padx=20, anchor="w")
	#entrada del usuario, entry
		self.entrada11= tk.Entry(self.form_reg,
		width=30, font=("Arial", 11), bg="#162640", insertbackground="#FFFFFF", relief="flat")

		self.entrada11.pack(fill="x", padx=20, ipady=8)
		
	#etiqueta de contraseña
		self.etiqueta3= tk.Label(self.form_reg,
		text="Contraseña",
		font=("Arial",10, "bold"),
		bg="#0F1D34",
		fg="#FFFFFF")

		self.etiqueta3.pack(pady=(0, 5), padx=20, anchor="w")
	#entrada del usuario, entry
		self.entrada3= tk.Entry(self.form_reg,
		width=30, font=("Arial", 11), bg="#162640", insertbackground="#FFFFFF", relief="flat", show="X")

		self.entrada3.pack(fill="x", padx=20, ipady=8)
		#confirmar contrasseña
		
		#etiqueta de contraseña
		self.etiqueta3conf= tk.Label(self.form_reg,
		text="Confirma tu contraseña",
		font=("Arial",10, "bold"),
		bg="#0F1D34",
		fg="#FFFFFF")

		self.etiqueta3conf.pack(pady=(0, 5), padx=20, anchor="w")
	#entrada del usuario, entry
		self.entrada3conf= tk.Entry(self.form_reg,
		width=30, font=("Arial", 11), bg="#162640", insertbackground="#FFFFFF", relief="flat", show="X")

		self.entrada3conf.pack(fill="x", padx=20, ipady=8)
		
		#Mensaje de registrarse!!!
		self.mensajereg2= tk.Label(self.form_reg,
		text="Te has registrado, regresa para iniciar sesion!",
		bg="#08101E",
		fg="#FFFFFF")

		#boton de registrarse
		self.botonreg2= tk.Button(self.form_reg,
	text="Registrarse", 
	font=("Arial", 10),
	bg="#08103E",
	fg="#FFFFFF", 
	cursor="hand2",
	command=self.registrar_usuario)

		self.botonvolv= tk.Button(self.form_reg,
	text="Volver",
	font=("Arial",10, "bold"),
	bg="#08103F",
	fg="#FFFFFF",
	cursor="hand2",
	command=self.volver_log)
	#lugares donde van a estar los botones y el mensaje de registro puestos en orden de salida
		self.botonvolv.pack(padx=20, pady=(30, 15), ipady=8)
		self.mensajereg2.pack(pady=(5, 10))
		self.botonreg2.pack(pady=(0, 25), padx=20, ipady=8)
		
	def volver_log(self):
		
		#destruir el formulario de registro
		self.form_reg.destroy()
		#mostrar el formulario de login
		self.form_log.pack(padx=40, fill="x")
	
	def registrar_usuario(self):
		
		#definir los usuarios y las contraseñas
		usuario= self.entrada11.get()
		contraseña= self.entrada3.get()
		confirmar=self.entrada3conf.get()
	#variables de inicio de sesion
		if usuario == "" or contraseña == "" or confirmar == "":
			from tkinter import messagebox
			
			#mensaje de alerta si no se los campos estan vacios
			messagebox.showwarning("Campos vacios","Introduce tu correo y confirma tu contraseña para registrar.")
			
		if contraseña != confirmar:
			from tkinter import messagebox
			
			messagebox.showwarning("Error!","Las contraseñas no coinciden :p !!")
			
		return
		from tkinter import messagebox
		
		messagebox.showinfo("Registro completo","Los campos se han llenado correctamente!, la autenticación se implementara proximamente")
	
