from tkinter import *
from tkinter import ttk

#Vertana Main
root=Tk()
root.title("Login User")

#main frame
mainFrame= Frame(root)
mainFrame.pack()
mainFrame.config(width=500, height=500)#, bg="lightblue")

#Text
titulo=Label(mainFrame, text="Software Presupuestos", font=("Arial",24))
titulo.grid(column=0, row=0, padx=10, pady=10,columnspan=2)



nameLabel= Label(mainFrame,text="Nombre")
nameLabel.grid(column=0,row=1)
passLabel=Label(mainFrame,text="Password")
passLabel.grid(column=0,row=2)


#Text Entry
nameUser=StringVar()
nameUser.set("Chris")
nameEntry=Entry(mainFrame,textvariable=nameUser)
nameEntry.grid(column=1,row=1)


contraUser=StringVar()
contraUser.set("1234")
contraEntry=Entry(mainFrame,textvariable=contraUser,show="*")
contraEntry.grid(column=1,row=2)

#Botones

iniciarSesionButton=ttk.Button(mainFrame,text="Iniciar Sesion")
iniciarSesionButton.grid(column=1, row=3, ipadx=5,ipady=5, padx=10, pady=10)


registrarButton=ttk.Button(mainFrame,text="Registrar")
registrarButton.grid(column=0, row=3, ipadx=5,ipady=5, padx=10, pady=10)













root.mainloop()




