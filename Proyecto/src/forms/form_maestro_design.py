import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import ImageTk, Image


#Crear la clase main para generar la ventana
class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.logo = util_img.leer_imagen("./src/imagenes/logoFondo.png", (500, 500))
        self.perfil = util_img.leer_imagen("./src/imagenes/logoPantera.png", (150, 150))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Sistema Presupuestos')
        self.iconbitmap("./src/imagenes/money.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Sistema de Gestion")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.imagenMenu = Image.open("./src/imagenes/money.ico").resize((30, 30), Image.BICUBIC)
        self.imagenMenu_tk = ImageTk.PhotoImage(self.imagenMenu)

        self.buttonMenuLateral = tk.Button(self.barra_superior, font=font_awesome,
        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white",
        image=self.imagenMenu_tk)
        self.buttonMenuLateral.pack(side=tk.LEFT)


        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="El mejor en Presupuestos")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de foto de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        
        self.buttonCentroCostos = tk.Button(self.menu_lateral)        
        self.buttonComprasGastos = tk.Button(self.menu_lateral)        
        self.buttonLiquidacion = tk.Button(self.menu_lateral)
        self.buttonModificaciones = tk.Button(self.menu_lateral)        
        self.buttonPermisos = tk.Button(self.menu_lateral)
        self.buttonPresupuesto = tk.Button(self.menu_lateral)
        self.buttonRubro = tk.Button(self.menu_lateral)
        self.buttonUsuario = tk.Button(self.menu_lateral)

        #Imagenes para los botones
        # Imágenes para los botones

        
        imagen_cc = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_cg = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_liquidacion = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_modificaciones = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_permisos = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_presupuesto = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_rubro = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)
        imagen_usuario = Image.open("./src/icons/key.png").resize((30, 30), Image.BICUBIC)

        imagen_cc_tk = tk.PhotoImage(imagen_cc)
        imagen_cg_tk = tk.PhotoImage(imagen_cg)
        imagen_liquidacion_tk = tk.PhotoImage(imagen_liquidacion)
        imagen_modificaciones_tk = tk.PhotoImage(imagen_modificaciones)
        imagen_permisos_tk = tk.PhotoImage(imagen_permisos)
        imagen_presupuesto_tk = tk.PhotoImage(imagen_presupuesto)
        imagen_rubro_tk = tk.PhotoImage(imagen_rubro)
        imagen_usuario_tk = tk.PhotoImage(imagen_usuario)

        #Informacion de los botones en una tupla
        buttons_info = [
            ("Centro de Costos",  "\uf109", self.buttonCentroCostos),
            ("Compras Gastos",  "\uf109", self.buttonComprasGastos),
            ("Liquidacion",  "\uf109", self.buttonLiquidacion),
            ("Modificaciones",  "\uf109", self.buttonModificaciones),
            ("Permisos",  "\uf109", self.buttonPermisos),
            ("Presupuestos", "\uf109", self.buttonPresupuesto),
            ("Rubros", "\uf109", self.buttonRubro),
            ("Usuarios", "\uf109", self.buttonUsuario),
        ]

        # Se recorre y se llena la tupla
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')