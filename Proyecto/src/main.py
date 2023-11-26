from forms.form_maestro_design import FormularioMaestroDesign

#Abrir la ventana principal
app = FormularioMaestroDesign()
#Adaptar la geometria de la ventana para que se abra por completo
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))

app.mainloop()