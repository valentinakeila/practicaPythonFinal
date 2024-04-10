class Usuario:
    def __init__(self, nombre: str,apellido:str,email:str,password:str) -> None:
        self.__nombre =  nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def  apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido1):
        self.__apellido = apellido1


    @property
    def  email(self):
        return self.__email
    
    @email.setter
    def email(self, email1):
        self.__email = email1

    @property
    def  password(self):
        return self.__password
    
    @password.setter
    def password(self, password1):
        self.__password = password1

    def validar_credenciales(self, email:str, password:str):
        if self.__email == email and self.__password == password:
            return True
        else:
            return f"Incorrecto"
        
    def __str__(self) -> str:
        return f"{self.__nombre}{self.__apellido}{self.__email}"

    