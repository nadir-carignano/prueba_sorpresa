#versiones de python
FROM python:alpine3.8

#Le decimos que copie todo en la carpeta "docker_python" dentro del contenedor
COPY . /docker_python

#Le indicamos donde va atrabajar
#donde va a correr los comandos
WORKDIR /docker_python

#Le damos la orden de que corra el pip install
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#exponemos el puerto para acceder a la app del contenedor
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
