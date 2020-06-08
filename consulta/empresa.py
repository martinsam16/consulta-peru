import requests

from zipfile import ZipFile
from io import BytesIO
from pyquery import PyQuery as pq


class Empresa:
    def __init__(self):
        self.__URL_SUNAT = 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc'
        self.__URL_SUNAT_CSV = 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsmulruc'

    def get_datos(self, ruc: str):
        RUC_URL = self.__URL_SUNAT_CSV + '/jrmS00Alias'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Content-Type': 'application/json;chartset=utf-8',
            'Requestverificationtoken': '30OB7qfO2MmL2Kcr1z4S0ttQcQpxH9pDUlZnkJPVgUhZOGBuSbGU4qM83JcSu7DZpZw-IIIfaDZgZ4vDbwE5-L9EPoBIHOOC1aSPi4FS_Sc1:clDOiaq7mKcLTK9YBVGt2R3spEU8LhtXEe_n5VG5VLPfG9UkAQfjL_WT9ZDmCCqtJypoTD26ikncynlMn8fPz_F_Y88WFufli38cUM-24PE1'
        }
        RUC_URL = RUC_URL + "?accion=consManual&textRuc=&numRnd=" + self._get_captcha() + "&selRuc=" + ruc
        HTML = requests.get(url=RUC_URL, headers=headers, allow_redirects=True).text
        jquery = pq(HTML)
        # hacke mate
        url_zip_csv = jquery('td.bg>a').attr('href')
        nombre_zip = jquery('td.bg>a').text()
        return self._extraer_csv_desde_zip(url_zip_csv, nombre_zip)

    def _get_captcha(self):
        CAPTCHA_URL = self.__URL_SUNAT + '/captcha'
        res = requests.post(url=CAPTCHA_URL, data={
            'accion': 'random'
        })
        return res.text

    def _extraer_csv_desde_zip(self, url, nombre_zip: str):
        nombre_txt = nombre_zip.replace('.zip', '.txt')
        res = requests.get(url)
        zipfile = ZipFile(BytesIO(res.content))
        lineas = list()
        for linea in zipfile.open(nombre_txt).readlines():
            lineas.append(linea.decode('utf-8'))
        json_datos = dict()
        cabeceras = lineas[0].split('|')
        valores = lineas[1].split('|')
        for indice, cabecera in enumerate(cabeceras):
            if indice != len(cabeceras) - 1:
                json_datos[cabecera.strip().lower().replace(' ', '_')] = valores[indice].strip()
        return json_datos


if __name__ == '__main__':
    empresa = Empresa()
    empresa.get_datos('20305354563')
