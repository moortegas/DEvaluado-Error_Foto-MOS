class Error(Exception):
    """Clase base para excepciones"""
    pass

# class DimensionError(Error):
#     def __init__(self, mensaje:str, dimension:int, maximo:int):
#         self.mensaje = mensaje
#         self.dimension = dimension
#         self.maximo = maximo


# Clase de excepción personalizada para errores relacionados con dimensiones
class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int = None, 
            maximo: int = None) -> None:
        # Constructor que inicializa el mensaje de error, la dimensión y el valor máximo permitido
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    # Método para devolver la representación en cadena de la excepción
    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            # Si no se proporciona ni la dimensión ni el valor máximo, devuelve la representación predeterminada en cadena
            return super().__str__()
        # Comienza a construir el mensaje de error con el mensaje proporcionado
        else:
            ret = self.mensaje

            # Agrega información de la dimensión si está disponible
            if self.dimension:
                ret += f" Se ingresó dimensión {self.dimension}."
            
            if self.maximo:
                # Agrega información del valor máximo permitido si está disponible
                ret += f" El valor máximo permitido es {self.maximo}."

            return ret