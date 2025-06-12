class trabajador:
    __apellido : str
    __nombre: str
    __dni : str
    __correo : str
    __legajo : int
    __horas: int
    __funcion : str
    
    def __init__(self, apellido, nombre, dni, correo, legajo, horas, funcion):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__correo = correo
        self.__legajo = legajo
        self.__horas = horas
        self.__funcion = funcion
        
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__apellido
    
    def get__dni(self):
        return self.__dni
    
    def get_correo(self):
        return self.__correo
    
    def get_legajo(self):
        return self.__legajo
    
    def get_horas(self):
        return self.__horas
    
    def get_funcion(self):
        return self.__funcion
    
    