import requests
from pyquery import PyQuery as pq


class BolsaValoresLima:

    def __init__(self):
        self.__URL_COTIZACION = 'https://www.bvl.com.pe/jsp/cotizacion.jsp'
        self.__URL_RESUMEN_MERCADO = 'https://www.bvl.com.pe/includes/resumen_mercado.dat'
        self.__URL_EMPRESAS = 'https://www.bvl.com.pe/includes/empresas_todas.dat'
        self.__URL_COTIZACIONES_TODAS = 'https://www.bvl.com.pe/includes/cotizaciones_todas.dat'

    def get_empresas(self):
        HTML = requests.get(url=self.__URL_EMPRESAS, verify=False).text
        tabla = pq(HTML)
        lista_empresas = list()

        pq(tabla).children().children().children().map(lambda i, e: self.__mapear_empresas(i, e, lista_empresas))
        return lista_empresas

    def get_cotizaciones_todas(self):
        HTML = requests.get(url=self.__URL_COTIZACIONES_TODAS, verify=False).text
        filas = pq(HTML).find('table').children()
        lista_datos = list()
        filas.map(lambda i, e: self.__mapear_cotizaciones_todas(i, e, lista_datos))
        return lista_datos

    def get_resumen_mercado(self):
        HTML = requests.get(url=self.__URL_RESUMEN_MERCADO, verify=False).text
        jquery = pq(HTML)
        tabla = jquery.find('table').children()
        lista_datos = list()
        tabla.map(lambda i, e: self.__mapear_resumen_mercado(i, e, lista_datos))
        return lista_datos

    def get_historico(self, nemonico: str, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene la tendencia en bolsa de un nemonico dado dependiendo del periodo
        :param nemonico: nemonico de la empresa en bolsa
        :param fecha_inicio: fecha inicio traer
        :param fecha_fin: fecha fin traer
        :return: datos del periodo del nemonico
        """
        HTML = requests.get(url=self.__URL_COTIZACION, params={
            'fec_inicio': fecha_inicio,
            'fec_fin': fecha_fin,
            'nemonico': nemonico
        }, verify=False).text
        jquery = pq(HTML)
        tabla = jquery.find('table').children()
        lista_datos = list()
        tabla.map(lambda i, e: self.__mapear_historico(i, e, lista_datos))
        return lista_datos

    def __mapear_empresas(self, indice, elemento, lista_datos):
        # TODO sacar nemonico de las rutas ('divTabB')
        lista_datos.append({
            'empresa': pq(elemento).text(),
            'informacion': pq(elemento).attr('href'),
        })

    def __mapear_cotizaciones_todas(self, indice, elemento, lista_datos):
        if indice > 1:
            fila = pq(elemento).children()
            temporal = list()
            fila.map(lambda i, e: temporal.append(pq(e).eq(0).text()))
            i = 1
            while i < len(temporal):
                lista_datos.append({
                    'empresa': temporal[i].strip(),
                    'nemonico': temporal[i + 1].strip(),
                    'sector': temporal[i + 2].strip(),
                    'segm': temporal[i + 3].strip(),
                    'moneda': temporal[i + 4].strip(),
                    'anterior': temporal[i + 5].strip(),
                    'fecha_anterior': temporal[i + 6].strip(),
                    'apertura': temporal[i + 7].strip(),
                    'ultima': temporal[i + 8].strip(),
                    'porcentaje_variacion': temporal[i + 9].strip(),
                    'compra': temporal[i + 10].strip(),
                    'venta': temporal[i + 11].strip(),
                    'acciones': temporal[i + 12].strip(),
                    'operaciones': temporal[i + 13].strip(),
                    'monto_negativo': temporal[i + 14].strip(),
                })
                i += 15

    def __mapear_resumen_mercado(self, indice, elemento, lista_datos):
        if indice > 1:
            fila = pq(elemento).children()
            temporal = list()
            fila.map(lambda i, e: temporal.append(pq(e).eq(0).text()))
            i = 0
            while i < len(temporal):
                lista_datos.append({
                    'nombre': temporal[i].lower(),
                    'pen': temporal[i + 1],
                    'usd': temporal[i + 2],
                    'numero_operaciones': temporal[i + 3]
                })
                i += 4

    def __mapear_historico(self, indice, elemento, lista_datos):
        if indice > 4:
            fila = pq(elemento).children()
            datos = fila.text().split()
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
    # import datetime

    bvl = BolsaValoresLima()
    # now = datetime.datetime.now()
    # fecha_actual = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day)
    # datos = bvl.get_historico('ALICORC1', '', fecha_actual)
    # print(len(datos))
    # print(datos)

    # bvl.get_resumen_mercado()
    bvl.get_cotizaciones_todas()
