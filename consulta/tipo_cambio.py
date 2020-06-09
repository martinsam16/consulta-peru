from typing import List

from pyquery import PyQuery as pq
import requests


class TipoCambio:
    def __init__(self):
        self.__URL = 'http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

    def get_tipo_cambio_actual(self) -> dict:
        """
        Obtiene el tipo de cambio actual
        :return: (compra, venta, dia)
        """
        HTML = requests.get(url=self.__URL).text
        jquery = pq(HTML)
        CSS_COMPRA = '[class=\'class="form-table"\'] tr:last-child td:nth-last-child(2)'
        CSS_VENTA = '[class=\'class="form-table"\'] tr:last-child td:nth-last-child(1)'
        CSS_DIA = '[class=\'class="form-table"\'] tr:last-child td:nth-last-child(3)'

        compra = float(jquery(CSS_COMPRA).text().strip())
        venta = float(jquery(CSS_VENTA).text().strip())
        dia = int(jquery(CSS_DIA).text().strip())

        return {'dia': dia, 'compra': compra, 'venta': venta}

    def get_tipo_cambio(self, anio: int, mes: int) -> List[dict]:
        """
        Obtiene el tipo de cambio dependiendo del año y mes solicitado
        :param anio: año
        :param mes: mes
        :return: lista de tipos de cambio
        """
        HTML = requests.get(url=self.__URL, params={
            'mes': mes,
            'anho': anio
        }).text
        jquery = pq(HTML)

        table = jquery('[class=\'class="form-table"\'] tr')
        return table.map(lambda i: self._mapear(jquery, i, table))

    def get_tipo_cambio_dia(self, anio: int, mes: int, dia: int) -> dict:
        """
        Obtiene el tipo de cambio dependiendo del año, mes y dia solicitado
        :param anio: año
        :param mes: mes
        :param dia: dia
        :return: tipo de cambio solicitado
        """
        data = self.get_tipo_cambio(anio=anio, mes=mes)
        return [e for e in data if e['dia'] >= dia][0]

    def _mapear(self, jquery, indice, table):
        models = list()
        wat = jquery(table).children()
        if indice != 0:
            for i in range(len(wat)):
                try:
                    models.append({
                        'dia': int(wat.eq(i).text().strip()),
                        'compra': float(wat.eq(i + 1).text().strip()),
                        'venta': float(wat.eq(i + 2).text().strip())
                    })
                except ValueError:
                    pass
                i = i + 2
        if len(table) - 1 == indice:
            return models
