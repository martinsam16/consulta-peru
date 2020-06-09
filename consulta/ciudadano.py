import requests


class Ciudadano:
    def __init__(self):
        self.__URL_ESSALUD = 'https://ww1.essalud.gob.pe/sisep/postulante/postulante/postulante_obtenerDatosPostulante.htm'

    def get_essalud_informacion(self, dni):
        """
        Obtiene informacionde un dni desde essalud
        :param dni:
        :return: datos de la persona por el dni
        """
        json_res = requests.get(self.__URL_ESSALUD, params={
            'strDni': dni
        }).json()
        datos: dict = json_res['DatosPerson'][0]
        datos['apellido_paterno'] = datos.pop('ApellidoPaterno')
        datos['apellido_materno'] = datos.pop('ApellidoMaterno')
        datos['nombres'] = datos.pop('Nombres')
        datos['dni'] = datos.pop('DNI')
        datos['sexo'] = 'M' if datos.pop('Sexo') == '2' else 'F'
        datos['ultimo_digito'] = self._get_code(datos['dni'])
        datos['fecha_nacimiento'] = datos.pop('FechaNacimiento')
        return datos

    def _get_code(self, dni: str):
        """
        Obtiene l cdigo del dni ingresado
        :param dni:
        :return: codigo
        """
        if (dni != '' or dni is not None or len(dni) == 8):
            hash = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
            suma = 5
            for i in range(2, 10):
                suma += int(dni[i - 2]) * hash[i]
            entero = int(suma / 11)
            digito = 11 - (suma - entero * 11)
            if digito == 10:
                digito = 0
            elif digito == 11:
                digito = 1
            return digito
