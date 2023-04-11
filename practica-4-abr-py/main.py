'''
    Practica POO3 4 Abril 2023

    1.a.
    Vamos a modelar a nuestra queridísima golondrina, Pepita.

    Sabemos que Pepita, como toda ave, sabe volar una cierta cantidad de
    kilómetros y comer una cantidad de gramos de comida.

    Cada vez que come, pepita repone energía (a razón de una unidad por
    gramo ingerido) y cada vez que vuela, gasta energía (a razón de 3
    unidades por cada kilómetro recorrido).

    Además, cuando un ave nace, es bien sabido que inicia su ciclo de
    vida con 2 unidades de energía.

    Lo que queremos es un programa donde hagamos comer a pepita 5 gramos
    de comida, luego la hagamos volar 1 kilómetro, y después la hagamos
    comer 20 gramos y volar otros 2 kilómetros.

    Pepita debe saber decirnos cuánta energía tiene al final del día.

    1.b
    Nuestro modelo es simple, pero hay restricciones obvias que tal vez
    no hayamos tenido en cuenta.
    Sí un ave quiere volar pero no tiene energía, entonces no debería
    hacer nada.

    1.c
    Como otras golondrinas, Pepita gusta de pescar. Cuando atrapa un pez,
    se lo come, y aumenta su energía en 10.

    Sin embargo, solo atrapa un pez una de cada 10 veces que intenta pescar,
    por lo que no siempre es una tarea fructífera.

    Cada vez que intenta pescar, consume dos unidades de energía. Pepón,
    otra golondrina, es el mejor pescador, y solo le cuesta una unidad de
    energía por cada vez que pesca.

    1.d
    Bombón es una paloma. las palomas, también son aves, y por tanto vuelan y
    comen.
    Pero además les gusta defecar en cualquier estatua, busto o monumento que
    encuentren en la ciudad. Cada vez que va al baño, la paloma decrementa su
    energía en 1.

    1.e
    Queremos agregar a la aplicación un logger, que vaya dándonos información
    acerca de cada evento que ocurre en la misma. El logger es el mismo para
    todo el sistema, y simplemente debería saber responder a “showInfo”,
    “showWarn” y “showError”, en donde muestra en pantalla un mensaje que
    comienza con “INFO: “, “WARN: “ o “ERROR: “ según corresponda.

    1.f
    El logger debería poder ser configurado al arranque en uno de tres modos,
    INFO, WARN o ERROR. Sí está configurado como INFO, todo mensaje debe ser
    mostrado, sí está configurado como WARN, solo los mensajes de show_warn y
    show_error deberían mostrarse, y sí está configurado como ERROR, solo los
    mensajes de show_error deberían mostrarse.
'''
import sys
import random
from enum import Enum


class LoggerLevel(Enum):
    '''
        Clase Enum para los niveles de notificación en el Logger
    '''
    INFO = 1
    WARN = 2
    ERROR = 3


class Logger:
    '''
        Clase Logger para mensajes de log.
    '''
    level: LoggerLevel

    stream_out: object

    def __init__(self):
        pass

    @staticmethod
    def config(level: LoggerLevel, stream_out) -> None:
        '''
            Método estático para configurar el Logger.
        '''
        Logger.level = level
        Logger.stream_out = stream_out

    @staticmethod
    def __show_msg_with_header(header: str, msg: str) -> None:
        '''
            Método privado para mostrar mensaje con encabezado correspondiente 
            en la salida configurada.
        '''
        Logger.stream_out.write(header + ": " + msg + "\n")

    @staticmethod
    def show_info(msg: str) -> None:
        '''
            Método estático para mostrar informaciones.
        '''
        if (Logger.level.value <= LoggerLevel.INFO.value):
            Logger.__show_msg_with_header(LoggerLevel.INFO.name, msg)

    @staticmethod
    def show_warn(msg: str) -> None:
        '''
            Método estático para mostrar advertencias.
        '''
        if (Logger.level.value <= LoggerLevel.WARN.value):
            Logger.__show_msg_with_header(LoggerLevel.WARN.name, msg)

    @staticmethod
    def show_error(msg: str) -> None:
        '''
            Método estático para mostrar errores.
        '''
        if (Logger.level.value <= LoggerLevel.ERROR.value):
            Logger.__show_msg_with_header(LoggerLevel.ERROR.name, msg)


class Ave:
    """
    Clase base Ave
    """

    def __init__(self) -> None:
        self.energia = 2

    def get_energia(self) -> int:
        '''
            Getter de energía.
        '''
        return self.energia

    def __set_energia(self, energia: int) -> None:
        '''
            Setter privado de energía.
        '''
        self.energia = energia

    def _inc_energia(self, cantidad: int) -> None:
        ''' 
            Método protegido que incrementa la energía de la Ave en la 
            *cantidad* determinada.
        '''
        self.__set_energia(self.get_energia() + cantidad)

    def _dec_energia(self, cantidad: int) -> None:
        ''' 
            Método protegido que decrementa la energía de la Ave en la 
            cantidad determinada si hay disponible, sino no hace nada.
        '''
        if self.__hay_energia_para(cantidad):
            self.__set_energia(self.get_energia() - cantidad)
            Logger.show_info(
                "En la clase Ave, se decremento la energía, quedando: " + str(self.get_energia()))

    def comer(self, gramos: int) -> None:
        '''
            Come una cantidad de *gramos* determinado incrementando la energía 
            de la Ave.
        '''
        self._inc_energia(gramos)

    def volar(self, kms: int) -> None:
        '''
            Vuela una cantidad de *kms* decrementando la energía necesaria.
        '''
        self._dec_energia(kms*3)

    def __hay_energia_para(self, cantidad: int) -> bool:
        '''
            Verifica si existe energía suficiente para gastar *cantidad*.
        '''
        return self.energia >= cantidad


class Golondrina(Ave):
    '''
        Clase Golondrina que heredad de Ave.
    '''

    def __init__(self, costo_pesca: int) -> None:
        super().__init__()
        self.costo_pesca = costo_pesca
        self.habilidad = 1

    def puede_pescar(self) -> bool:
        '''
            Verifica si existe energía suficiente para pescar
        '''
        return self.get_energia() >= 2

    def __tuvo_suerte_pescando(self) -> bool:
        '''
            Verifica si tuvo suerte pescando en función de la habilidad de la Golondrina.
        '''
        rand = random.random()
        return rand < (10.0/self.habilidad)

    def pescar(self) -> None:
        '''
            Pesca la Golondrina, decrementando la energía necesaria y comiendo pez si tuvo suerte.
        '''
        self._dec_energia(self.costo_pesca)
        Logger.show_info("En la clase Golondrina, alguna intento pescar un pez")
        if self.__tuvo_suerte_pescando():
            self.__comer_pez()

    def __comer_pez(self) -> None:
        '''
            Come la cantidad de gramos determinado por el pez incrementando la energía de la Ave.
        '''
        self.comer(10)


class Paloma(Ave):
    '''
        Clase Paloma que hereda de Ave.
    '''

    def defecar(self) -> None:
        '''
            Defeca la Paloma, restando la energía necesaria para hacerlo.
        '''
        self._dec_energia(1)
        Logger.show_error("En clase Paloma, alguna defeco!")


if __name__ == '__main__':
    Logger.config(LoggerLevel.INFO, sys.stdout)
    Logger.show_info("Una información 1.")
    Logger.show_warn("Un warning 1.")
    Logger.show_error("Un error 1.")
    pepita: Golondrina = Golondrina(1)
    pepon: Golondrina = Golondrina(2)
    bombon: Paloma = Paloma()
    bombon.defecar()
    pepita.comer(5)
    Logger.show_info("Una información 2.")
    Logger.show_warn("Un warning 2.")
    Logger.show_error("Un error 2.")
    pepita.volar(1)
    pepita.comer(20)
    pepita.volar(2)
    pepon.pescar()
    Logger.show_info("La energía de pepita es " + str(pepita.get_energia()))
    Logger.show_warn("La energía de bombón es " + str(bombon.get_energia()))
    Logger.show_error("La energía de pepón es " + str(pepon.get_energia()))
