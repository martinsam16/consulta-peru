import datetime
import os

from flask import Flask
from flask import json
from flask import Response
from flask_cors import CORS
from flask_cors import cross_origin

from consulta.bolsa_valores import BolsaValoresLima
from consulta.ciudadano import Ciudadano
from consulta.empresa import Empresa
from consulta.spp_comisiones_primas import SppComisionesPrimas
from consulta.tipo_cambio import TipoCambio

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
port = int(os.environ.get("PORT", 5000))

ciudadano = Ciudadano()
empresa = Empresa()

cambio = TipoCambio()
bvl = BolsaValoresLima()
spp = SppComisionesPrimas()


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return {
        'estado': 'corriendo :D',
        'repo': 'https://github.com/MartinSamanArata2018/consulta-peru'
    }


@app.route('/dni_essalud/<dni>', methods=['GET'])
@cross_origin()
def get_ciudadano_essalud(dni):
    return ciudadano.get_essalud_informacion(dni=dni)


@app.route('/dni_sunat/<dni>', methods=['GET'])
@cross_origin()
def get_ciudadano_sunat(dni):
    return ciudadano.get_sunat_informacion(dni=dni)


@app.route('/ruc/<ruc>', methods=['GET'])
@cross_origin()
def get_empresa(ruc):
    return Response(json.dumps(empresa.get_datos(ruc)), content_type="application/json; charset=utf-8")


@app.route('/cambio', methods=['GET'])
@cross_origin()
def get_tipo_cambio_actual():
    return cambio.get_tipo_cambio_actual()


@app.route('/cambio/periodo/<int:anio>/<int:mes>', methods=['GET'])
@cross_origin()
def get_tipo_cambio_periodo(anio, mes):
    return Response(json.dumps(cambio.get_tipo_cambio(anio, mes)), content_type="application/json; charset=utf-8")


@app.route('/cambio/dia/<int:anio>/<int:mes>/<int:dia>', methods=['GET'])
@cross_origin()
def get_tipo_cambio_periodo_dia(anio, mes, dia):
    return Response(json.dumps(cambio.get_tipo_cambio_dia(anio, mes, dia)),
                    content_type="application/json; charset=utf-8")


# ToDo :bug:
now = datetime.datetime.now()
# formato de fechas para la bvl
fecha_actual = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day)


@app.route('/bvl/<nemonico>', defaults={'fecha_inicio': '', 'fecha_fin': fecha_actual}, methods=['GET'])
@app.route('/bvl/<nemonico>/<fecha_inicio>', defaults={'fecha_fin': fecha_actual}, methods=['GET'])
@app.route('/bvl/<nemonico>/<fecha_inicio>/<fecha_fin>', methods=['GET'])
@cross_origin()
def get_bvl_empresa(nemonico, fecha_inicio, fecha_fin):
    return Response(json.dumps(bvl.get_historico(nemonico, fecha_inicio, fecha_fin)),
                    content_type="application/json; charset=utf-8")


@app.route('/bvl/resumen_mercado', methods=['GET'])
@cross_origin()
def get_bvl_resumen_mercado():
    return Response(json.dumps(bvl.get_resumen_mercado()), content_type="application/json; charset=utf-8")


@app.route('/bvl/empresas', methods=['GET'])
@cross_origin()
def get_bvl_empresas():
    return Response(json.dumps(bvl.get_empresas()), content_type="application/json; charset=utf-8")


@app.route('/bvl/cotizaciones', methods=['GET'])
@cross_origin()
def get_cotizaciones():
    return Response(json.dumps(bvl.get_cotizaciones_todas()), content_type="application/json; charset=utf-8")


@app.route('/spp', methods=['GET'])
@cross_origin()
def get_comisiones_primas():
    return Response(json.dumps(spp.get_data_actual()), content_type="application/json; charset=utf-8")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
