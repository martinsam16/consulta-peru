import requests


class Sunarp:
    def __init__(self):
        self.__URL = 'https://tracking-sunarp-production.apps.paas.sunarp.gob.pe/tracking/api/consultaTitulo'

    def get_tramite_titulo(self, json: dict):
        json['ip'] = 'pms.sunarp.gob.pe'
        json['userApp'] = 'extranet'
        json['userCrea'] = '11111'
        json['status'] = 'A'
        return requests.post(url=self.__URL,
                             json=json).json()
