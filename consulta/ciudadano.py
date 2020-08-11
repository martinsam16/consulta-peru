import requests


class Ciudadano:
    def __init__(self):
        self.__URL_ESSALUD = 'https://ww1.essalud.gob.pe/sisep/postulante/postulante/postulante_obtenerDatosPostulante.htm'
        self.__URL_SUNAT = 'http://www.facturacionsunat.com/vfpsws/vfpsconsbsapi.php'
        self.__URL_RENIEC = 'https://api.reniec.cloud/dni/{dni}'

    def get_reniec_informacion(self, dni):
        """
        Obtiene informacion de un dni desde la reniec
        :param dni: datos de la persona por el dni
        :return:
        """
        json_res: dict = requests.get(url=self.__URL_RENIEC.format(dni=dni)).json()
        return self.set_datos_persona(
            paterno=json_res.pop('apellido_paterno'),
            materno=json_res.pop('apellido_materno'),
            nombres=json_res.pop('nombres'),
            dni=json_res.pop('dni')
        )

    def get_sunat_informacion(self, dni):
        """
        Obtiene informacion de un dni desde la sunat
        :param dni: datos de la persona por el dni
        :return:
        """
        json_res: dict = requests.get(self.__URL_SUNAT, params={
            'dni': dni,
            'token': '87290E49D50B519',
            'format': 'json'
        }).json()
        return self.set_datos_persona(
            paterno=json_res.pop('ape_paterno'),
            materno=json_res.pop('ape_materno'),
            nombres=json_res.pop('nombres'),
            dni=json_res.pop('dni'),
            nacimiento=json_res.pop('feNacimiento'),
            domicilio=json_res.pop('domicilio'),
            telefono=json_res.pop('telefono')
        )

    def get_essalud_informacion(self, dni):
        """
        Obtiene informacion de un dni desde essalud
        :param dni:
        :return: datos de la persona por el dni
        """
        json_res = requests.get(self.__URL_ESSALUD, params={
            'strDni': dni
        }).json()
        datos: dict = json_res['DatosPerson'][0]
        return self.set_datos_persona(paterno=datos.pop('ApellidoPaterno'),
                                      materno=datos.pop('ApellidoMaterno'),
                                      nombres=datos.pop('Nombres'),
                                      dni=datos.pop('DNI'),
                                      sexo='M' if datos.pop('Sexo') == '2' else 'F',
                                      nacimiento=datos.pop('FechaNacimiento'))

    def set_datos_persona(self, paterno, materno, nombres, dni, nacimiento='-', domicilio='-', sexo='-', telefono='-'):
        return {
            'apellido_paterno': paterno,
            'apellido_materno': materno,
            'nombres': nombres,
            'dni': dni,
            'sexo': sexo,
            'ultimo_digito': self._get_code(dni),
            'fecha_nacimiento': nacimiento,
            'domicilio': domicilio,
            'telefono': telefono
        }

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
