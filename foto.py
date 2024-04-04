# Importando DimensionError desde el módulo error
from error import DimensionError

class Foto():
    # Dimensión máxima permitida para la foto
    MAX = 2500

    # Constructor que inicializa el ancho, el alto y la ruta de la foto
    def __init__(self, ancho: int, alto:int, ruta:str) -> None:
       self.__ancho = ancho
       self.__alto = alto
       ruta = ruta
 
    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho) -> None:
        # Comprueba si el ancho excede el límite máximo
        if ancho > Foto.MAX:
            raise DimensionError("Ancho no permitido.", ancho, Foto.MAX)
        # Comprueba si el ancho es menor que 1
        elif ancho < 1:
            raise DimensionError("Ancho debe ser mayor a 0.", ancho)
        else:
            # Establece el ancho
            self.__ancho = ancho

    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter    
    def ancho(self, alto) -> None:
        # Comprueba si el alto excede el límite máximo
        if alto > Foto.MAX:
            raise DimensionError("Alto no permitido.", alto, Foto.MAX)
        # Comprueba si el alto es menor que 1
        elif alto < 1:
            raise DimensionError("Alto debe ser mayor a 0.", alto)
        else:
            # Establece el alto
            self.__alto = alto
