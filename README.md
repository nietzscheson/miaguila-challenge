MiAguila Challenge
==============

Por favor, siga las siguientes instrucciones para arrancar el proyecto. 
Los requerimientos mínimos son la última versión de Docker-for(Mac-Windows) y tener instalado el paquete para Mac/Win de Make.
Si por alguna razón no tiene/puede/usa makefile puede leer los comandos escritos en el documento y ejecutar las instruciones.

# Instalación

1. Primero, clonamos el repositorio:

```bash
$ git clone https://github.com/nietzscheson/miaguila-challenge
```

2. Para inicializar el proyecto use:
```bash
$ make init
// o
$ docker-compose up --build -d
```

Si todo ha salido bien puedes revisar que los servicios estén corriendo correctamente:

```bash
> $ docker-compose ps
               Name                             Command               State           Ports
----------------------------------------------------------------------------------------------------
miaguila-challenge_api_1             flask run --host=0.0.0.0         Up      0.0.0.0:5000->5000/tcp
miaguila-challenge_mongo-express_1   tini -- /docker-entrypoint ...   Up      0.0.0.0:8081->8081/tcp
miaguila-challenge_mongo_1           docker-entrypoint.sh mongod      Up      27017/tcp

```

Y visitar:

- [API]('http://localhost:5000')
- [Documentación]('http://localhost:5000/v1')
- [MongoDB UI Manager]('http://localhost:8081')

El proyecto fue construido usando Flask, en Python. Y una versión de MongoDB. Servicios configurados en el docker-compose.yml. Para darle características de API Rest a Flask, se instaló Flask-Restful.

Para poder testear las caracteristicas principales use el commando:

```bash
$ make test
```

Se ha usado Gitflow como enfoque de versionamiento. En etapas tempranas de desarrollo, se generan nuevas características y se hacen merge con la rama develop.