import requests
from pyquery import PyQuery as pq


class BolsaValoresLima:

    def __init__(self):
        self.__URL = 'https://www.bvl.com.pe/jsp/cotizacion.jsp'
        # TODO listar empresas
        # https://www.bvl.com.pe/includes/empresas_a.dat

    def get_historico(self, nemonico: str, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene la tendencia en bolsa de un nemonico dado dependiendo del periodo
        :param nemonico: nemonico de la empresa en bolsa
        :param fecha_inicio: fecha inicio traer
        :param fecha_fin: fecha fin traer
        :return: datos del periodo del nemonico
        """
        HTML = requests.get(url=self.__URL, params={
            'fec_inicio': fecha_inicio,
            'fec_fin': fecha_fin,
            'nemonico': nemonico
        }, verify=False).text
        jquery = pq(HTML)
        tabla = jquery.find('table').children()
        lista_datos = list()
        tabla.map(lambda i, e: self.__mapear(i, e, lista_datos))
        return lista_datos

    def __mapear(self, indice, elemento, lista_datos):
        if indice > 4:
            columna = pq(elemento).children()
            datos = columna.text().split()
            try:
                lista_datos.append({
                    'fecha': datos[0:1][0],
                    'apertura': datos[1:2][0],
                    'cierre': datos[2:3][0],
                    'maxima': datos[3:4][0],
                    'minima': datos[4:5][0],
                    'promedio': datos[5:6][0],
                    'cantidad_negociada': datos[6:7][0],
                    'monto_negociado': datos[7:8][0],
                    'fecha_anterior': datos[8:9][0],
                    'cierre_anterior': datos[9:10][0]
                })
            except Exception:
                pass


if __name__ == '__main__':
    import datetime

    bvl = BolsaValoresLima()
    now = datetime.datetime.now()
    fecha_actual = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day)
    datos = bvl.get_historico('ALICORC1', '', fecha_actual)
    print(len(datos))
    print(datos)
