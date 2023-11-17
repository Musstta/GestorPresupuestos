class User():
    
    numUsers = 0

    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 3

        User.numUsers += 1

    def conn(self):
        myPass = input("Ingrese su contrasena: ")
        if myPass == self.contra:
            print("Conectado con éxito")
            self.conectado = True
        else:
            self.intentos -= 1
            if self.intentos>0:
                print("Contraseña incorrecta")
                print("Intentos restantes:", self.intentos)
                self.conn()
            else:
                print("Error, no se pudo iniciar sesion")
                print("No te quedan intentos")
                
    def desconectar(self):
        if self.conectado:
            print("Se cerró sesión")
            self.conectado = False
        else:
            print("Error, no inició sesión")

    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"


user1 = User(input("Ingrese nombre: "), input("Ingrese contraseña: "))
print(user1)
user1.conn()