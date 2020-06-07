FROM python:3.7-alpine

MAINTAINER Martin Alexis Saman Arata

ADD . /

RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    pip install --no-cache-dir lxml>=3.5.0 && \
    apk del .build-deps

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3","./app.py"]

#docker build -t consulta-peru .
#docker run -p 5000:5000 -dit --name="consulta-peru" "consulta-peru"