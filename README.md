# Consulta Perú
API centralizada y open-source de consultas de datos del Perú

## Correr

Clona o descarga el repo y ..

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


## Endpoints

### Ciudadano
Obtiene la información de una persona natural a partir de su DNI

> Puedes sacar su ruc por: 10{dni}{ultimo_digito} y realizar la consulta al endpoint de empresa.

| URI   | Metodo|Ejemplo |
|:-------|:------------|:------------|
|/dni/{numero_dni}| GET|/dni/72720455|

#### Respuesta
`````json
{
    "apellido_paterno": "SAMAN",
    "apellido_materno": "ARATA",
    "nombres"         : "MARTIN ALEXIS",
    "dni"             : "72720455",
    "fecha_nacimiento": "16/10/2000",
    "ultimo_digito"   : 1,
    "sexo"            : "M"
}
`````

### Empresa
Obtiene la información de una persona jurídica o empresa a partir de su RUC

| URI   | Metodo|Ejemplo |
|:-------|:------------|:------------|
|/ruc/{numero_ruc}| GET|/ruc/20305354563|

#### Respuesta

`````json
{
  "numeroruc": "20305354563", 
  "nombre_ó_razonsocial": "FARMACIAS PERUANAS S.A.", 
  "tipo_de_contribuyente": "SOCIEDAD ANONIMA", 
  "profesion_u_oficio": "-", 
  "nombre_comercial": "BOTICAS FASA, MIFARMA, JUSTO", 
  "condicion_del_contribuyente": "HABIDO", 
  "estado_del_contribuyente": "BAJA DEFINITIVA", 
  "fecha_de_inscripcion": "15/05/1996", 
  "fecha_de_inicio_de_actividades": "01/05/1996", 
  "departamento": "LIMA", 
  "provincia": "LIMA", 
  "distrito": "LA VICTORIA", 
  "direccion": "CAL. VICTOR ALZAMORA NRO. 147 URB. SANTA CATALINA", 
  "telefono": "-", 
  "fax": "-", 
  "actividad_de_comercio_exterior": "SIN ACTIVIDAD", 
  "principal-_ciiu": "VTA. MIN. PROD. FARMAC. Y ART. TOCADOR.", 
  "secundario_1-_ciiu": "-", 
  "secundario_2-_ciiu": "-", 
  "afecto_nuevo_rus": "NO", 
  "buen_contribuyente": "-", 
  "agente_de_retencion": "NO, Excluido del Régimen de Agentes de Retención de IGV a partir del 01/09/2016", 
  "agente_de_percepcion_vtaint": "-", 
  "agente_de_percepcion_comliq": "-"
}
`````

### Tipo de Cambio
Obtiene el tipo de cambio desde la SUNAT

| URI   |Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/cambio| GET|/cambio|Obtiene el tipo de cambio actual|
|/cambio/periodo/{anio}/{mes}| GET|/cambio/periodo/2020/6|Obtiene el tipo de cambio dependiendo del año y mes solicitado|
|/cambio/dia/{anio}/{mes}/{dia}| GET|/cambio/dia/2020/2/4|Obtiene el tipo de cambio dependiendo del año, mes y día solicitado|

#### Respuestas
* /cambio
`````json
{
    "dia"     : 5,
    "compra"  : 3.421,
    "venta"   : 3.422
}
`````
* /cambio/periodo/{anio}/{mes} -> /cambio/periodo/2020/6
`````json
[
  {"dia": 2, "compra": 3.421, "venta": 3.422}, 
  {"dia": 3, "compra": 3.402, "venta": 3.404}, 
  {"dia": 4, "compra": 3.389, "venta": 3.391}, 
  {"dia": 5, "compra": 3.421, "venta": 3.422}
]
`````
* /cambio/dia/{anio}/{mes}/{dia} -> /cambio/dia/2020/2/4
`````json
{
  "dia"   : 4, 
  "compra": 3.372, 
  "venta" : 3.374
}
`````

### Bolsa de Valores de Lima
Obtiene la información de la bvl

> *formato fecha = YYYYMMDD*

| URI   | Metodo|Ejemplo |Descripción|
|:-------|:------------|:------------|:------------|
|/bvl/resumen_mercado| GET|/bvl/resumen_mercado|Obtiene el resumen del mercado|
|/bvl/cotizaciones| GET|/bvl/cotizaciones|Obtiene todas las cotizaciones|
|/bvl/empresas| GET|/bvl/empresas|Obtiene las empresas que cotizan en bolsa|
|/bvl/{nemonico}| GET|/bvl/NVDA|Obtiene todo el historial en bolsa de un nemonico solicitado|
|/bvl/{nemonico}/{fecha_inicio}| GET|/bvl/NVDA/20200603|Obtiene el historial de un nemonico en bolsa desde la fecha solicitada hasta ahora|
|/bvl/{nemonico}/{fecha_inicio}/{fecha_fin}| GET|/bvl/NVDA/20200501/20200603|Obtiene el historial de un nemonico de un periodo determinado|


#### Respuestas
* /bvl/resumen_mercado
`````json
[
  {"nombre": "renta variable", "pen": "106,130,906.31", "usd": "31,018,823.99", "numero_operaciones": "658"},
  {"nombre": "acciones", "pen": "103,555,476.34", "usd": "30,266,104.43", "numero_operaciones": "633"},
  {"nombre": "adrs", "pen": "858,081.47", "usd": "250,791.02", "numero_operaciones": "17"}, 
  {"nombre": "cert. patrim. fideicomiso", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "cert. partic. fibras", "pen": "2,437.82", "usd": "712.50", "numero_operaciones": "1"}, 
  {"nombre": "cert. fondos de inversion", "pen": "1,714,910.68", "usd": "501,216.04", "numero_operaciones": "7"}, 
  {"nombre": "cert. suscripc. preferente", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "instrumentos de deuda", "pen": "20,395,155.60", "usd": "5,960,881.37", "numero_operaciones": "4"}, 
  {"nombre": "mercado continuo", "pen": "20,395,155.60", "usd": "5,960,881.37", "numero_operaciones": "4"}, 
  {"nombre": "mercado de dinero", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "colocacion primaria", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "operaciones plazo con prima", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "operaciones de reporte y prestamo", "pen": "3,889,597.05", "usd": "1,136,810.48", "numero_operaciones": "22"}, 
  {"nombre": "rep renta variable", "pen": "3,889,597.05", "usd": "1,136,810.48", "numero_operaciones": "22"}, 
  {"nombre": "rep instrumentos de deuda", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "prestamo de valores", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "mienm", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "mercado alternativo de valores", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "renta variable", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "instrumentos de deuda", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "colocación primaria", "pen": "0.00", "usd": "0.00", "numero_operaciones": "0"}, 
  {"nombre": "total mercado", "pen": "130,415,658.96", "usd": "38,116,515.84", "numero_operaciones": "684"}
 ]
`````



* /bvl/cotizaciones

`````
[
    {"empresa": "Apple Inc.", "nemonico": "AAPL", "sector": "", "segm": "RV3", "moneda": "US$", "anterior": "331.50", "fecha_anterior": "05/06/2020", "apertura": "", "ultima": "", "porcentaje_variacion": "", "compra": "", "venta": "", "acciones": "", "operaciones": "", "monto_negativo": ""}, 
    {"empresa": "Barrick Gold Corporation", "nemonico": "ABX", "sector": "", "segm": "RV3", "moneda": "US$", "anterior": "23.22", "fecha_anterior": "05/06/2020", "apertura": "23.30", "ultima": "23.30", "porcentaje_variacion": "0.34", "compra": "", "venta": "", "acciones": "350", "operaciones": "1", "monto_negativo": "8,155"},
    {"empresa": "iShares MSCI ACWI ETF", "nemonico": "ACWI", "sector": "", "segm": "RV3", "moneda": "US$", "anterior": "76.30", "fecha_anterior": "05/06/2020", "apertura": "76.50", "ultima": "76.50", "porcentaje_variacion": "0.26", "compra": "", "venta": "", "acciones": "530", "operaciones": "1", "monto_negativo": "40,545"}, 
    {"empresa": "Adm. del Comercio", "nemonico": "ADCOMEC1", "sector": "DIVERSAS", "segm": "RV2", "moneda": "S/", "anterior": "", "fecha_anterior": "", "apertura": "", "ultima": "", "porcentaje_variacion": "", "compra": "", "venta": "", "acciones": "", "operaciones": "", "monto_negativo": ""},
    {"empresa": "iSh Core US Aggregate Bond ETF", "nemonico": "AGG", "sector": "", "segm": "RV3", "moneda": "US$", "anterior": "116.42", "fecha_anterior": "04/06/2020", "apertura": "", "ultima": "", "porcentaje_variacion": "", "compra": "", "venta": "", "acciones": "", "operaciones": "", "monto_negativo": ""},
    ...
]
`````

* /bvl/empresas
`````
[
  {"empresa": "A. JAIME ROJAS REPRESENTACIONES GENERALES S.A.", "informacion": "/inf_corporativa71050_SkFJTUUxQkMxQQ.html"}, 
  {"empresa": "A.F.P. INTEGRA S.A.", "informacion": "/inf_corporativa10400_SU5URUdSQzE.html"}, 
  {"empresa": "ADMINISTRADORA DEL COMERCIO S.A.", "informacion": "/inf_corporativa71300_QURDT01FQzE.html"}, 
  {"empresa": "ADMINISTRADORA JOCKEY PLAZA SHOPPING CENTER S.A.", "informacion": "/inf_corporativa71320_SlBMQVoxQkMxQQ.html"}, 
  {"empresa": "AFP HABITAT S.A.", "informacion": "/inf_corporativa10250_SEFCSVRBQzE.html"}, 
  {"empresa": "AGRO INDUSTRIAL PARAMONGA S.A.A.", "informacion": "/inf_corporativa77900_UEFSQU1PQzE.html"}, 
  {"empresa": "AGRO PUCALA S.A.A.", "informacion": "/inf_corporativa77935_UFVDQUxBQzE.html"}, 
  {"empresa": "AGROINDUSTRIAL LAREDO S.A.A.", "informacion": "/inf_corporativa77600_TEFSRURPQzE.html"}, 
  {"empresa": "AGROINDUSTRIAS AIB S.A.", "informacion": "/inf_corporativa21000_QUlCQzE.html"},
  ...
] 
`````

* /bvl/{nemonico} -> /bvl/NVDA
`````
[
  {"fecha": "05/06/2020", "apertura": "353.90", "cierre": "353.90", "maxima": "353.90", "minima": "353.90", "promedio": "353.90", "cantidad_negociada": "85.00", "monto_negociado": "30,081.50", "fecha_anterior": "14/05/2020", "cierre_anterior": "314.06"}, 
  {"fecha": "14/05/2020", "apertura": "314.06", "cierre": "314.06", "maxima": "314.06", "minima": "314.06", "promedio": "314.06", "cantidad_negociada": "18.00", "monto_negociado": "5,653.08", "fecha_anterior": "13/05/2020", "cierre_anterior": "313.10"}, 
  {"fecha": "13/05/2020", "apertura": "313.10", "cierre": "313.10", "maxima": "313.10", "minima": "313.10", "promedio": "313.10", "cantidad_negociada": "36.00", "monto_negociado": "11,271.60", "fecha_anterior": "03/04/2020", "cierre_anterior": "245.20"},
  ...
  {"fecha": "25/07/2019", "apertura": "174.10", "cierre": "174.10", "maxima": "174.10", "minima": "174.10", "promedio": "174.10", "cantidad_negociada": "352.00", "monto_negociado": "61,283.20", "fecha_anterior": "04/06/2019", "cierre_anterior": "141.50"}
]
`````

* /bvl/{nemonico}/{fecha_inicio} -> /bvl/NVDA/20200603
`````json
[
  {"fecha": "05/06/2020", "apertura": "353.90", "cierre": "353.90", "maxima": "353.90", "minima": "353.90", "promedio": "353.90", "cantidad_negociada": "85.00", "monto_negociado": "30,081.50", "fecha_anterior": "14/05/2020", "cierre_anterior": "314.06"}
]
`````

* /bvl/{nemonico}/{fecha_inicio}/{fecha_fin} -> /bvl/NVDA/20200501/20200603
`````json
[
  {"fecha": "14/05/2020", "apertura": "314.06", "cierre": "314.06", "maxima": "314.06", "minima": "314.06", "promedio": "314.06", "cantidad_negociada": "18.00", "monto_negociado": "5,653.08", "fecha_anterior": "13/05/2020", "cierre_anterior": "313.10"}, 
  {"fecha": "13/05/2020", "apertura": "313.10", "cierre": "313.10", "maxima": "313.10", "minima": "313.10", "promedio": "313.10", "cantidad_negociada": "36.00", "monto_negociado": "11,271.60", "fecha_anterior": "03/04/2020", "cierre_anterior": "245.20"}
]
`````
