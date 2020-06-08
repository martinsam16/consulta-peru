import json
import datetime

from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin

from consulta.bolsa_valores import BolsaValoresLima
from consulta.ciudadano import Ciudadano
from consulta.empresa import Empresa
from consulta.tipo_cambio import TipoCambio

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ciudadano = Ciudadano()
empresa = Empresa()

cambio = TipoCambio()
bvl = BolsaValoresLima()


@app.route('/dni/<dni>', methods=['GET'])
@cross_origin()
def get_ciudadano(dni):
    return ciudadano.get_essalud_informacion(dni=dni)


@app.route('/ruc/<ruc>', methods=['GET'])
@cross_origin()
def get_empresa(ruc):
    return json.dumps(empresa.get_datos(ruc),ensure_ascii=False)


@app.route('/cambio', methods=['GET'])
@cross_origin()
def get_tipo_cambio_actual():
    return cambio.get_tipo_cambio_actual()


@app.route('/cambio/periodo/<int:anio>/<int:mes>', methods=['GET'])
@cross_origin()
def get_tipo_cambio_periodo(anio, mes):
    return json.dumps(cambio.get_tipo_cambio(anio, mes))


@app.route('/cambio/dia/<int:anio>/<int:mes>/<int:dia>', methods=['GET'])
@cross_origin()
def get_tipo_cambio_periodo_dia(anio, mes, dia):
    return json.dumps(cambio.get_tipo_cambio_dia(anio, mes, dia))


now = datetime.datetime.now()
# formato de fechas para la bvl
fecha_actual = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day)


@app.route('/bvl/<nemonico>', defaults={'fecha_inicio': '', 'fecha_fin': fecha_actual}, methods=['GET'])
@app.route('/bvl/<nemonico>/<fecha_inicio>', defaults={'fecha_fin': fecha_actual}, methods=['GET'])
@app.route('/bvl/<nemonico>/<fecha_inicio>/<fecha_fin>', methods=['GET'])
@cross_origin()
def get_bvl_empresa(nemonico, fecha_inicio, fecha_fin):
    # ALICORC1, AAPL, NVDA
    return json.dumps(bvl.get_historico(nemonico, fecha_inicio, fecha_fin))


@app.route('/bvl/resumen_mercado', methods=['GET'])
@cross_origin()
def get_bvl_resumen_mercado():
    return json.dumps(bvl.get_resumen_mercado(), ensure_ascii=False)


@app.route('/bvl/empresas', methods=['GET'])
@cross_origin()
def get_bvl_empresas():
    return json.dumps(bvl.get_empresas(), ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
