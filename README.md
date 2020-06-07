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
Obtiene la información de una persona a partir de su DNI

| URI   | Ejemplo |
|:-------|:------------|
|/dni/{numero_dni}| /dni/72720455|

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



