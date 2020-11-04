# Consulta Perú

![API version](https://img.shields.io/badge/api%20version-0.0.1-orange)
![Python version supported](https://img.shields.io/badge/python-3.x-blue)
[![Docker image size](https://img.shields.io/docker/image-size/malditoidealismo/consulta-peru)](https://hub.docker.com/r/malditoidealismo/consulta-peru)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=MartinSamanArata2018_consulta-peru&metric=alert_status)](https://sonarcloud.io/dashboard?id=MartinSamanArata2018_consulta-peru)
![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

API centralizada y open-source de consultas de datos del Perú

## Deploy
### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Correr
### Python
`````sh
pip install -r requirements.txt
`````
`````sh
py app.py
`````

### Docker

`````docker
docker build -t consulta-peru .
`````

`````docker
docker run -p 5000:5000 -dit --name="consulta-peru" "consulta-peru"
`````

ó

`````docker
docker run -p 5000:5000 -dit malditoidealismo/consulta-peru:latest
`````

# Endpoints
1. [Ciudadano](#ciudadano)
2. [Empresa](#empresa)
3. [Tipo de Cambio](#tipo-de-cambio)
4. [Bolsa de Valores de Lima](#bolsa-de-valores-de-lima)
5. [Comisiones y Primas de Seguro del SPP](#comisiones-y-primas-de-seguro-del-spp)
5. [SUNARP](#SUNARP)

> Nota: Crear issues en caso haya errores o los endpoints a los que se conecta o hayan dejado de funcionar :D

## Ciudadano
Obtiene la información de una persona natural a partir de su DNI

> Puedes sacar su ruc por: 10{dni}{ultimo_digito} y realizar la consulta al endpoint de empresa.

| URI   | Metodo|Ejemplo | |
|:-------|:------------|:------------|:------------|
|/dni_sunat/{numero_dni}| GET|/dni_sunat/72720455|🟢|
|/dni_reniec/{numero_dni}| GET|/dni_reniec/72720455|🟢|
|/dni_essalud/{numero_dni}| GET|/dni_essalud/72720455|🟢|


#### Respuesta
`````json
{
  "apellido_materno": "ARATA",
  "apellido_paterno": "SAMAN",
  "dni": "72720455",
  "domicilio": "URB SANTA ROSA DE HUALCARA MZ D LT 23 SAN VICENTE DE CAÑETE - CAÑETE - LIMA",
  "fecha_nacimiento": "16/10/2000",
  "nombres": "MARTIN ALEXIS",
  "sexo": "-",
  "telefono": "-",
  "ultimo_digito": 1
}
`````

## Empresa
Obtiene la información de una persona jurídica o empresa a partir de su RUC

| URI   | Metodo|Ejemplo |
|:-------|:------------|:------------|
|/ruc/{numero_ruc}| GET|/ruc/20305354563|

### Respuesta

`````json
{
    "actividad_de_comercio_exterior": "SIN ACTIVIDAD",
    "afecto_nuevo_rus": "NO",
    "agente_de_percepcion_comliq": "-",
    "agente_de_percepcion_vtaint": "-",
    "agente_de_retencion": "NO, Excluido del Régimen de Agentes de Retención de IGV a partir del 01/09/2016",
    "buen_contribuyente": "-",
    "condicion_del_contribuyente": "HABIDO",
    "departamento": "LIMA",
    "direccion": "CAL. VICTOR ALZAMORA NRO. 147 URB. SANTA CATALINA",
    "distrito": "LA VICTORIA",
    "estado_del_contribuyente": "BAJA DEFINITIVA",
    "fax": "-",
    "fecha_de_inicio_de_actividades": "01/05/1996",
    "fecha_de_inscripcion": "15/05/1996",
    "nombre__razonsocial": "FARMACIAS PERUANAS S.A.",
    "nombre_comercial": "BOTICAS FASA, MIFARMA, JUSTO",
    "numeroruc": "20305354563",
    "principal_ciiu": "VTA.  MIN. PROD. FARMAC. Y ART. TOCADOR.",
    "profesion_u_oficio": "-",
    "provincia": "LIMA",
    "secundario_1_ciiu": "-",
    "secundario_2_ciiu": "-",
    "telefono": "-",
    "tipo_de_contribuyente": "SOCIEDAD ANONIMA"
}
`````

## Tipo de Cambio
Obtiene el tipo de cambio desde la SUNAT

| URI   |Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/cambio| GET|/cambio|Obtiene el tipo de cambio actual|
|/cambio/periodo/{anio}/{mes}| GET|/cambio/periodo/2020/6|Obtiene el tipo de cambio dependiendo del año y mes solicitado|
|/cambio/dia/{anio}/{mes}/{dia}| GET|/cambio/dia/2020/2/4|Obtiene el tipo de cambio dependiendo del año, mes y día solicitado|

### Respuestas
* /cambio
`````json
{
    "compra": 3.438,
    "dia": 9,
    "venta": 3.441
}
`````
* /cambio/periodo/{anio}/{mes} -> /cambio/periodo/2020/6
`````json
[
    {
        "compra": 3.421,
        "dia": 2,
        "venta": 3.422
    },
    {
        "compra": 3.402,
        "dia": 3,
        "venta": 3.404
    },
    {
        "compra": 3.389,
        "dia": 4,
        "venta": 3.391
    },
    {
        "compra": 3.421,
        "dia": 5,
        "venta": 3.422
    },
    {
        "compra": 3.426,
        "dia": 6,
        "venta": 3.43
    },
    {
        "compra": 3.438,
        "dia": 9,
        "venta": 3.441
    }
]
`````
* /cambio/dia/{anio}/{mes}/{dia} -> /cambio/dia/2020/2/4
`````json
{
    "compra": 3.372,
    "dia": 4,
    "venta": 3.374
}
`````

## Bolsa de Valores de Lima
Obtiene la información de la bvl

> *formato fecha = YYYYMMDD*

| URI   | Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/bvl/resumen_mercado| GET|/bvl/resumen_mercado|Obtiene el resumen del mercado|
|/bvl/cotizaciones| GET|/bvl/cotizaciones|Obtiene todas las cotizaciones|
|/bvl/empresas| GET|/bvl/empresas|Obtiene las empresas que cotizan en bolsa|
|/bvl/empresa/tree/{nemonico}| GET|/|Proximamente..|
|/bvl/{nemonico}| GET|/bvl/NVDA|Obtiene todo el historial en bolsa de un nemonico solicitado|
|/bvl/{nemonico}/{fecha_inicio}| GET|/bvl/NVDA/20200603|Obtiene el historial de un nemonico en bolsa desde la fecha solicitada hasta ahora|
|/bvl/{nemonico}/{fecha_inicio}/{fecha_fin}| GET|/bvl/NVDA/20200501/20200603|Obtiene el historial de un nemonico de un periodo determinado|


### Respuestas
* /bvl/resumen_mercado
`````json
[
    {
        "nombre": "renta variable",
        "numero_operaciones": "116",
        "pen": "8,275,293.08",
        "usd": "2,405,958.16"
    },
    {
        "nombre": "acciones",
        "numero_operaciones": "108",
        "pen": "7,937,328.33",
        "usd": "2,307,698.31"
    },
    {
        "nombre": "adrs",
        "numero_operaciones": "8",
        "pen": "337,964.75",
        "usd": "98,259.85"
    },
    {
        "nombre": "cert. patrim. fideicomiso",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "cert. partic. fibras",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "cert. fondos de inversion",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "cert. suscripc. preferente",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "instrumentos de deuda",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "mercado continuo",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "mercado de dinero",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "colocacion primaria",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "operaciones plazo con prima",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "operaciones de reporte y prestamo",
        "numero_operaciones": "1",
        "pen": "57,506.49",
        "usd": "16,719.43"
    },
    {
        "nombre": "rep renta variable",
        "numero_operaciones": "1",
        "pen": "57,506.49",
        "usd": "16,719.43"
    },
    {
        "nombre": "rep instrumentos de deuda",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "prestamo de valores",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "mienm",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "mercado alternativo de valores",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "renta variable",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "instrumentos de deuda",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "colocación primaria",
        "numero_operaciones": "0",
        "pen": "0.00",
        "usd": "0.00"
    },
    {
        "nombre": "total mercado",
        "numero_operaciones": "117",
        "pen": "8,332,799.57",
        "usd": "2,422,677.59"
    }
]
`````



* /bvl/cotizaciones

`````
[
    {
        "acciones": "",
        "anterior": "331.50",
        "apertura": "",
        "compra": "",
        "empresa": "Apple Inc.",
        "fecha_anterior": "05/06/2020",
        "moneda": "US$",
        "monto_negativo": "",
        "nemonico": "AAPL",
        "operaciones": "",
        "porcentaje_variacion": "",
        "sector": "",
        "segm": "RV3",
        "ultima": "",
        "venta": ""
    },
    {
        "acciones": "",
        "anterior": "23.30",
        "apertura": "",
        "compra": "",
        "empresa": "Barrick Gold Corporation",
        "fecha_anterior": "08/06/2020",
        "moneda": "US$",
        "monto_negativo": "",
        "nemonico": "ABX",
        "operaciones": "",
        "porcentaje_variacion": "",
        "sector": "",
        "segm": "RV3",
        "ultima": "",
        "venta": ""
    },
    {
        "acciones": "",
        "anterior": "76.50",
        "apertura": "",
        "compra": "",
        "empresa": "iShares MSCI ACWI ETF",
        "fecha_anterior": "08/06/2020",
        "moneda": "US$",
        "monto_negativo": "",
        "nemonico": "ACWI",
        "operaciones": "",
        "porcentaje_variacion": "",
        "sector": "",
        "segm": "RV3",
        "ultima": "",
        "venta": ""
    },
    ...
]
`````

* /bvl/empresas
`````
[
    {
        "empresa": "A. JAIME ROJAS REPRESENTACIONES GENERALES S.A.",
        "informacion": "/inf_corporativa71050_SkFJTUUxQkMxQQ.html"
    },
    {
        "empresa": "A.F.P. INTEGRA S.A.",
        "informacion": "/inf_corporativa10400_SU5URUdSQzE.html"
    },
    {
        "empresa": "ADMINISTRADORA DEL COMERCIO S.A.",
        "informacion": "/inf_corporativa71300_QURDT01FQzE.html"
    },
    {
        "empresa": "ADMINISTRADORA JOCKEY PLAZA SHOPPING CENTER S.A.",
        "informacion": "/inf_corporativa71320_SlBMQVoxQkMxQQ.html"
    },
    {
        "empresa": "AFP HABITAT S.A.",
        "informacion": "/inf_corporativa10250_SEFCSVRBQzE.html"
    },
    {
        "empresa": "AGRO INDUSTRIAL PARAMONGA S.A.A.",
        "informacion": "/inf_corporativa77900_UEFSQU1PQzE.html"
    },
  ...
] 
`````

* /bvl/{nemonico} -> /bvl/NVDA
`````json
[
    {
        "apertura": "353.90",
        "cantidad_negociada": "85.00",
        "cierre": "353.90",
        "cierre_anterior": "314.06",
        "fecha": "05/06/2020",
        "fecha_anterior": "14/05/2020",
        "maxima": "353.90",
        "minima": "353.90",
        "monto_negociado": "30,081.50",
        "promedio": "353.90"
    },
    {
        "apertura": "314.06",
        "cantidad_negociada": "18.00",
        "cierre": "314.06",
        "cierre_anterior": "313.10",
        "fecha": "14/05/2020",
        "fecha_anterior": "13/05/2020",
        "maxima": "314.06",
        "minima": "314.06",
        "monto_negociado": "5,653.08",
        "promedio": "314.06"
    },
    {
        "apertura": "313.10",
        "cantidad_negociada": "36.00",
        "cierre": "313.10",
        "cierre_anterior": "245.20",
        "fecha": "13/05/2020",
        "fecha_anterior": "03/04/2020",
        "maxima": "313.10",
        "minima": "313.10",
        "monto_negociado": "11,271.60",
        "promedio": "313.10"
    },
    {
        "apertura": "245.20",
        "cantidad_negociada": "20.00",
        "cierre": "245.20",
        "cierre_anterior": "269.00",
        "fecha": "03/04/2020",
        "fecha_anterior": "31/03/2020",
        "maxima": "245.20",
        "minima": "245.20",
        "monto_negociado": "4,904.00",
        "promedio": "245.20"
    },
    {
        "apertura": "269.00",
        "cantidad_negociada": "18.00",
        "cierre": "269.00",
        "cierre_anterior": "261.00",
        "fecha": "31/03/2020",
        "fecha_anterior": "30/03/2020",
        "maxima": "269.00",
        "minima": "269.00",
        "monto_negociado": "4,842.00",
        "promedio": "269.00"
    },
    {
        "apertura": "261.00",
        "cantidad_negociada": "400.00",
        "cierre": "261.00",
        "cierre_anterior": "250.30",
        "fecha": "30/03/2020",
        "fecha_anterior": "24/03/2020",
        "maxima": "261.00",
        "minima": "261.00",
        "monto_negociado": "104,400.00",
        "promedio": "261.00"
    },
    {
        "apertura": "241.85",
        "cantidad_negociada": "950.00",
        "cierre": "250.30",
        "cierre_anterior": "228.40",
        "fecha": "24/03/2020",
        "fecha_anterior": "12/03/2020",
        "maxima": "250.30",
        "minima": "241.85",
        "monto_negociado": "232,715.00",
        "promedio": "244.96"
    },
    {
        "apertura": "231.85",
        "cantidad_negociada": "542.00",
        "cierre": "228.40",
        "cierre_anterior": "252.14",
        "fecha": "12/03/2020",
        "fecha_anterior": "10/03/2020",
        "maxima": "231.85",
        "minima": "228.40",
        "monto_negociado": "124,717.70",
        "promedio": "230.11"
    },
    {
        "apertura": "252.14",
        "cantidad_negociada": "300.00",
        "cierre": "252.14",
        "cierre_anterior": "249.40",
        "fecha": "10/03/2020",
        "fecha_anterior": "09/03/2020",
        "maxima": "252.14",
        "minima": "252.14",
        "monto_negociado": "75,642.00",
        "promedio": "252.14"
    },
    {
        "apertura": "249.40",
        "cantidad_negociada": "36.00",
        "cierre": "249.40",
        "cierre_anterior": "272.30",
        "fecha": "09/03/2020",
        "fecha_anterior": "03/03/2020",
        "maxima": "249.40",
        "minima": "249.40",
        "monto_negociado": "8,978.40",
        "promedio": "249.40"
    },
    {
        "apertura": "274.11",
        "cantidad_negociada": "886.00",
        "cierre": "272.30",
        "cierre_anterior": "267.60",
        "fecha": "03/03/2020",
        "fecha_anterior": "26/02/2020",
        "maxima": "274.11",
        "minima": "272.30",
        "monto_negociado": "241,322.96",
        "promedio": "272.37"
    },
    {
        "apertura": "271.90",
        "cantidad_negociada": "279.00",
        "cierre": "267.60",
        "cierre_anterior": "273.25",
        "fecha": "26/02/2020",
        "fecha_anterior": "25/02/2020",
        "maxima": "271.90",
        "minima": "267.60",
        "monto_negociado": "74,828.10",
        "promedio": "268.20"
    },
    {
        "apertura": "273.25",
        "cantidad_negociada": "36.00",
        "cierre": "273.25",
        "cierre_anterior": "313.00",
        "fecha": "25/02/2020",
        "fecha_anterior": "20/02/2020",
        "maxima": "273.25",
        "minima": "273.25",
        "monto_negociado": "9,837.00",
        "promedio": "273.25"
    },
    {
        "apertura": "311.00",
        "cantidad_negociada": "872.00",
        "cierre": "313.00",
        "cierre_anterior": "312.30",
        "fecha": "20/02/2020",
        "fecha_anterior": "19/02/2020",
        "maxima": "313.00",
        "minima": "311.00",
        "monto_negociado": "271,812.00",
        "promedio": "311.71"
    },
    {
        "apertura": "312.20",
        "cantidad_negociada": "83.00",
        "cierre": "312.30",
        "cierre_anterior": "271.40",
        "fecha": "19/02/2020",
        "fecha_anterior": "12/02/2020",
        "maxima": "312.30",
        "minima": "312.20",
        "monto_negociado": "25,915.80",
        "promedio": "312.24"
    },
    {
        "apertura": "269.45",
        "cantidad_negociada": "76.00",
        "cierre": "271.40",
        "cierre_anterior": "265.24",
        "fecha": "12/02/2020",
        "fecha_anterior": "11/02/2020",
        "maxima": "271.40",
        "minima": "269.45",
        "monto_negociado": "20,548.40",
        "promedio": "270.37"
    },
    {
        "apertura": "265.24",
        "cantidad_negociada": "570.00",
        "cierre": "265.24",
        "cierre_anterior": "260.00",
        "fecha": "11/02/2020",
        "fecha_anterior": "10/02/2020",
        "maxima": "265.24",
        "minima": "265.24",
        "monto_negociado": "151,186.80",
        "promedio": "265.24"
    },
    {
        "apertura": "260.00",
        "cantidad_negociada": "41.00",
        "cierre": "260.00",
        "cierre_anterior": "251.00",
        "fecha": "10/02/2020",
        "fecha_anterior": "22/01/2020",
        "maxima": "260.00",
        "minima": "260.00",
        "monto_negociado": "10,660.00",
        "promedio": "260.00"
    },
    {
        "apertura": "251.00",
        "cantidad_negociada": "10.00",
        "cierre": "251.00",
        "cierre_anterior": "249.05",
        "fecha": "22/01/2020",
        "fecha_anterior": "17/01/2020",
        "maxima": "251.00",
        "minima": "251.00",
        "monto_negociado": "2,510.00",
        "promedio": "251.00"
    },
    {
        "apertura": "249.05",
        "cantidad_negociada": "40.00",
        "cierre": "249.05",
        "cierre_anterior": "240.54",
        "fecha": "17/01/2020",
        "fecha_anterior": "08/01/2020",
        "maxima": "249.05",
        "minima": "249.05",
        "monto_negociado": "9,962.00",
        "promedio": "249.05"
    },
    {
        "apertura": "240.54",
        "cantidad_negociada": "250.00",
        "cierre": "240.54",
        "cierre_anterior": "236.80",
        "fecha": "08/01/2020",
        "fecha_anterior": "03/01/2020",
        "maxima": "240.54",
        "minima": "240.54",
        "monto_negociado": "60,135.00",
        "promedio": "240.54"
    },
    {
        "apertura": "237.19",
        "cantidad_negociada": "73.00",
        "cierre": "236.80",
        "cierre_anterior": "225.00",
        "fecha": "03/01/2020",
        "fecha_anterior": "16/12/2019",
        "maxima": "237.19",
        "minima": "236.80",
        "monto_negociado": "17,302.39",
        "promedio": "237.02"
    },
    {
        "apertura": "225.00",
        "cantidad_negociada": "36.00",
        "cierre": "225.00",
        "cierre_anterior": "210.03",
        "fecha": "16/12/2019",
        "fecha_anterior": "12/11/2019",
        "maxima": "225.00",
        "minima": "225.00",
        "monto_negociado": "8,100.00",
        "promedio": "225.00"
    },
    {
        "apertura": "210.03",
        "cantidad_negociada": "143.00",
        "cierre": "210.03",
        "cierre_anterior": "206.63",
        "fecha": "12/11/2019",
        "fecha_anterior": "11/11/2019",
        "maxima": "210.03",
        "minima": "210.03",
        "monto_negociado": "30,034.29",
        "promedio": "210.03"
    },
    {
        "apertura": "206.63",
        "cantidad_negociada": "39.00",
        "cierre": "206.63",
        "cierre_anterior": "187.72",
        "fecha": "11/11/2019",
        "fecha_anterior": "11/10/2019",
        "maxima": "206.63",
        "minima": "206.63",
        "monto_negociado": "8,058.57",
        "promedio": "206.63"
    },
    {
        "apertura": "187.72",
        "cantidad_negociada": "500.00",
        "cierre": "187.72",
        "cierre_anterior": "185.72",
        "fecha": "11/10/2019",
        "fecha_anterior": "07/10/2019",
        "maxima": "187.72",
        "minima": "187.72",
        "monto_negociado": "93,860.00",
        "promedio": "187.72"
    },
    {
        "apertura": "185.72",
        "cantidad_negociada": "364.00",
        "cierre": "185.72",
        "cierre_anterior": "179.00",
        "fecha": "07/10/2019",
        "fecha_anterior": "06/09/2019",
        "maxima": "185.72",
        "minima": "185.72",
        "monto_negociado": "67,602.08",
        "promedio": "185.72"
    },
    {
        "apertura": "179.00",
        "cantidad_negociada": "1,300.00",
        "cierre": "179.00",
        "cierre_anterior": "174.10",
        "fecha": "06/09/2019",
        "fecha_anterior": "25/07/2019",
        "maxima": "179.00",
        "minima": "179.00",
        "monto_negociado": "232,700.00",
        "promedio": "179.00"
    },
    {
        "apertura": "174.10",
        "cantidad_negociada": "352.00",
        "cierre": "174.10",
        "cierre_anterior": "141.50",
        "fecha": "25/07/2019",
        "fecha_anterior": "04/06/2019",
        "maxima": "174.10",
        "minima": "174.10",
        "monto_negociado": "61,283.20",
        "promedio": "174.10"
    }
]
`````

* /bvl/{nemonico}/{fecha_inicio} -> /bvl/NVDA/20200603
`````json
[
    {
        "apertura": "353.90",
        "cantidad_negociada": "85.00",
        "cierre": "353.90",
        "cierre_anterior": "314.06",
        "fecha": "05/06/2020",
        "fecha_anterior": "14/05/2020",
        "maxima": "353.90",
        "minima": "353.90",
        "monto_negociado": "30,081.50",
        "promedio": "353.90"
    }
]
`````

* /bvl/{nemonico}/{fecha_inicio}/{fecha_fin} -> /bvl/NVDA/20200501/20200603
`````json
[
    {
        "apertura": "314.06",
        "cantidad_negociada": "18.00",
        "cierre": "314.06",
        "cierre_anterior": "313.10",
        "fecha": "14/05/2020",
        "fecha_anterior": "13/05/2020",
        "maxima": "314.06",
        "minima": "314.06",
        "monto_negociado": "5,653.08",
        "promedio": "314.06"
    },
    {
        "apertura": "313.10",
        "cantidad_negociada": "36.00",
        "cierre": "313.10",
        "cierre_anterior": "245.20",
        "fecha": "13/05/2020",
        "fecha_anterior": "03/04/2020",
        "maxima": "313.10",
        "minima": "313.10",
        "monto_negociado": "11,271.60",
        "promedio": "313.10"
    }
]
`````


## Comisiones y Primas de Seguro del SPP
Obtiene informacion de la Superintendencia de Banca, seguros y AFP

| URI   |Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/spp| GET|/spp|Obtiene información actual (comisión fija ignorada)|
|/spp/periodo| GET|/|Proximamente..|

### Respuesta

`````json
[
    {
        "afp": "HABITAT",
        "aporte_obligatorio_fondo_pensiones": "10.00%",
        "comision_mixta": {
            "comision_anual_sobre_saldo": "1.25%",
            "comision_sobre_flujo": "0.38%"
        },
        "comision_sobre_flujo": "1.47%",
        "prima_seguros": "1.35%",
        "remuneracion_maxima_asegurable": "9,788.95"
    },
    {
        "afp": "INTEGRA",
        "aporte_obligatorio_fondo_pensiones": "10.00%",
        "comision_mixta": {
            "comision_anual_sobre_saldo": "0.82%",
            "comision_sobre_flujo": "0.00%"
        },
        "comision_sobre_flujo": "1.55%",
        "prima_seguros": "1.35%",
        "remuneracion_maxima_asegurable": "9,788.95"
    },
    {
        "afp": "PRIMA",
        "aporte_obligatorio_fondo_pensiones": "10.00%",
        "comision_mixta": {
            "comision_anual_sobre_saldo": "1.25%",
            "comision_sobre_flujo": "0.18%"
        },
        "comision_sobre_flujo": "1.60%",
        "prima_seguros": "1.35%",
        "remuneracion_maxima_asegurable": "9,788.95"
    },
    {
        "afp": "PROFUTURO",
        "aporte_obligatorio_fondo_pensiones": "10.00%",
        "comision_mixta": {
            "comision_anual_sobre_saldo": "1.20%",
            "comision_sobre_flujo": "0.67%"
        },
        "comision_sobre_flujo": "1.69%",
        "prima_seguros": "1.35%",
        "remuneracion_maxima_asegurable": "9,788.95"
    }
]
`````
## SUNARP

| URI   |Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/sunarp/titulo| GET|/sunarp/titulo|Obtiene el trámite por titulo|

* /sunarp/titulo
### Envio
`````json
{
   "zona":"01",
   "oficina":"01",
   "year":"2018",
   "titulo":"02650055"
}
`````
### Respuesta
`````json
{
  "codigoRespuesta": "0000",
  "descripcionRespuesta": "Se muestran los resultados correctamente.",
  "lstPagos": [
    {
      "codSedePago": null,
      "desSedePago": "LIMA",
      "fechaRecibo": "23/11/2018 15:51:02",
      "montoRecibo": "    20.00",
      "numeroRecibo": "372-00054221"
    }
  ],
  "lstParticipantes": [
    {
      "codTipoParticipante": "1",
      "desTipoParticipante": "PN",
      "nombresRazonSocial": "MATSUFUJI FUKUNAGA OSCAR LEOPOLDO"
    }
  ],
  "lstTitulo": [
    {
      "actoRegistral": "SUCESION INTESTADA DEFINITIVA",
      "anioTitulo": "2018",
      "areaRegistral": "23000",
      "codEstadoActual": "120301",
      "documentoPresentante": "DNI-10181827",
      "estadoActual": "INSCRITO",
      "fechaHoraPresentacion": "23/11/2018 15:51:02",
      "fechaVencimiento": "15/01/2019",
      "indiPror": "0",
      "indiSusp": "0",
      "lugarPresentacion": "LIMA / MIRAFLORES",
      "montoDevo": "",
      "nombrePresentante": "GUTIERREZ ADRIANZEN, LUIS BENJAMIN  [ALVAREZ QUISPE, ALBERTO FELIX]",
      "numeroTitulo": "02650055",
      "oficina": "01",
      "partidaMatriz": null,
      "tipoRegistro": "PERSONAS NATURALES",
      "zona": "01"
    }
  ]
}
`````

