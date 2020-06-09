import requests

from pyquery import PyQuery as pq


class SppComisionesPrimas:
    def __init__(self):
        self.__URL = 'https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/Paginas/comision_prima.aspx'

    def get_data_actual(self):
        res = requests.get(url=self.__URL)
        HTML = res.text
        jquery = pq(HTML)
        contenido = jquery('.JER_filaContenido')
        datos = list()
        contenido.map(lambda i, e: self.__mapear(i, e, datos))
        return datos

    def __mapear(self, indice, elemento, datos):
        texto_columna = pq(elemento).text().splitlines()
        datos.append({
            'afp': texto_columna[0],
            'comision_sobre_flujo': texto_columna[1],
            'comision_mixta': {
                'comision_sobre_flujo': texto_columna[2],
                'comision_anual_sobre_saldo': texto_columna[3],
            },
            'prima_seguros': texto_columna[4],
            'aporte_obligatorio_fondo_pensiones': texto_columna[5],
            'remuneracion_maxima_asegurable': texto_columna[6]
        })

