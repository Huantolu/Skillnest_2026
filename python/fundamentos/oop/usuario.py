class Usuario:
    def __int__(self, nombre, password):
        self.nombre = nombre
        self.contraseña = password
        self.activo = True

    def login(self):
        self.activo = True
        return f'{self.nombre} Esta logeado'

    def logout(self):
        self.activo = False
        return f'{self.nombre} Esta deslogeado'

class Administrador(Usuario):
    def __init__(self, nombre, password, nivel_acceso="parcial"):
        super().__init__(nombre, password)
        #Nivel de acceso: total, parcial
        self.nivel_acceso = nivel_acceso

    def Eliminar_usuario(self, usuario):
        return f"{self.nombre} ha eliminado al usuario {usuario.nombre}"

    def login(self):
        super().login()
        #El retorno será distinto porque quiero que este método sea POLIMORFICO
        return f'Ha ingresado el usuario {self.nombre}, administrador con nivel de acceso {self.nivel_acceso}'


#DESAFIO
class Influencer(Usuario):
    def __init__(self, nombre, password, seguidores):
        super().__init__(self, nombre, password)
        self.seguidores = seguidores
    
    def publish(self, post):
        self.post = post
        return f'El influencer {self.nombre} ha posteado {self.post}'
    
i1 = Influencer("Huantolu", "a1234567", "0")
print(i1.publish("Hola chavalones"))