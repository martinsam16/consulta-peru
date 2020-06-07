import json
import datetime

from flask import Flask

from bolsa_valores import BolsaValoresLima
from ciudadano import Ciudadano
from tipo_cambio import TipoCambio

app = Flask(__name__)

ciudadano = Ciudadano()
cambio = TipoCambio()
bvl = BolsaValoresLima()


@app.route('/dni/<dni>')
def get_ciudadano(dni):
    return ciudadano.get_essalud_informacion(dni=dni)


@app.route('/cambio')
def get_tipo_cambio_actual():
    return cambio.get_tipo_cambio_actual()


@app.route('/cambio/periodo/<anio>/<mes>')
def get_tipo_cambio_periodo(anio, mes):
    return json.dumps(cambio.get_tipo_cambio(anio, mes))


now = datetime.datetime.now()
# formato de fechas para la bvl
fecha_actual = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day)


@app.route('/bvl/<nemonico>', defaults={'fecha_inicio': '', 'fecha_fin': fecha_actual})
@app.route('/bvl/<nemonico>/<fecha_inicio>', defaults={'fecha_fin': fecha_actual})
@app.route('/bvl/<nemonico>/<fecha_inicio>/<fecha_fin>')
def get_bvl_empresa(nemonico, fecha_inicio, fecha_fin):
    # ALICORC1, AAPL, NVDA
    return json.dumps(bvl.get_historico(nemonico, fecha_inicio, fecha_fin))

@app.route('/bvl/resumen_mercado')
def get_bvl_resumen_mercado():
    return json.dumps(bvl.get_resumen_mercado())

@app.route('/bvl/empresas')
def get_bvl_empresas():
    return json.dumps(bvl.get_empresas(),ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
