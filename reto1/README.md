# Reto_N1
> Repositorio para alojar la solución al reto #1 sobre microservicios comunicándose con gRPC.
## Información de la asignatura
---

 -  **Nombre de la asignatura:** Tópicos especiales en telemática.
-   **Código de la asignatura:**  C2361-ST0263-4528
-   **Departamento:** Departamento de Informática y Sistemas (Universidad EAFIT).
-   **Nombre del profesor:** Juan Carlos Montoya Mendoza.
-  **Correo electrónico del docente:** __[jcmontoy@eafit.edu.co](mailto:jcmontoy@eafit.edu.co)__.

## Datos del estudiante
---

-   **Nombre del estudiante:** Julian Gomez Benitez.
-  **Correo electrónico del estudiante:** __[jgomeb11@eafit.edu.co](mailto:jgomezb11@eafit.edu.co)__.

## Descripción y alcance del proyecto
---

El proyecto consiste en un sistema de microservicios que se comunican mediante gRPC. Los microservicios tienen las siguientes funcionalidades:

1.  El primer microservicio está escrito en **Python** y se encarga de la **gestión de productos** en un archivo plano, __simulando el comportamiento de un inventario__, con un función de búsqueda y otra de escritura.
2.  El segundo microservicio está escrito en **Python** y se encarga de verificar que **no exista un producto** para poder **escribir productos nuevos en el archivo plano del primer microservicio**.
3.  El tercer microservicio está escrito en **Node** y se encarga de **verificar que exista un producto en el inventario para venderlo satisfactoriamente.** También tiene su persistencia en una base de datos en un archivo plano pero solo realiza operaciones de **CREATE.**

Se ha implementado una API Gateway con **Flask** que se comunica con el cliente a través de REST y con el backend mediante gRPC. Además, algunos microservicios se comunican entre ellos a traves de gRPC también.

El objetivo del proyecto es construir una aplicación eCommerce cuyo back este hecho apartir de microservicios que se comuniquen entre ellos mediante llamadas a procedimientos remotos usando gRPC. El objetivo se cumple a cabalidad.


## Estructura del proyecto
---

Como lo mencionamos se implementaron 3 microservicios y 1 API Gateway, la estructura del proyecto se organiza en diferentes carpetas y archivos para lograr una buena separación de responsabilidades y una fácil mantenibilidad. Cada microservicio tiene su propia carpeta en donde a su vez se encuentran las interfaces de comunicación (archivo `.proto` y archivos que resultan de su compilacion) y su respectivo `.txt` en caso de que el microservicio cuente con base de datos simulada.

* reto1
    - [api_gateway](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/api_gateway "api_gateway")
		- [Service.proto](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/api_gateway/Service.proto "Service.proto")
		- [access_point.py](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/api_gateway/access_point.py "access_point.py")
    - [servicios](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services "servicios")
		- [add_stock](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/add_stock "add_stock")
			- [Service.proto](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/add_stock/Service.proto "Service.proto")
			- [back.py](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/add_stock/back.py "back.py")
    	- [product_inventary](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/product_inventary "product_inventary")
			- [Service.proto](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_inventary/Service.proto "Service.proto")
			- [inventary.txt](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_inventary/inventary.txt "inventary.txt")
			- [back.py](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_inventary/back.py "back.py")
    	- [product_sale](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/product_sale "product_sale")
			- [Service.proto](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_sale/Service.proto "Service.proto")
			- [sales_db.txt](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_sale/sales_db.txt "sales_db.txt")
			- [back.js](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/services/product_sale/back.js "back.js")
    - [README.md](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/README.md "README.md")
	- [config.env](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/config.env "config.env")

## Arquitectura de la solución planteada
---
![arquitectura](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/arquitectura.png)
La arquitectura de la solución planteada se basa en una arquitectura en capas, donde cada capa se encarga de una función específica en el proceso. La capa del mundo real se encarga de tener un dispositivo que pueda usar el protocolo HTTP 1.1 y poder mandar peticiones al servidor. La API Gateway se encarga de coordinar la comunicación entre dichos microservicios y la comunicación con el usuario. La capa de microservicios se encarga de la lógica de negocio y procesamiento de datos.

Además, se ha utilizado un patron de diseño en la implementación de la solución:
*  El patrón de Fachada, que permite esconder tras una interfaz simple un grupo complejo de funcionalidades de un framwork o microservicio. Se empieza a utilizar desde el momento en que se decide hacer la aplicacion por microservicios puesto que, por definicion, los microservicios permiten encapsular funcionalidades detras de una interfaz.

## Resultados logrados
---
Respecto a los logros obtenidos, se ha conseguido instalar un conjunto de microservicios que se comunican mediante gRPC. Este conjunto está formado por tres microservicios, los cuales tienen la tarea de administrar un inventario de productos, validar los productos para llevar a cabo órdenes de venta y realizar adiciones a la base de datos de productos.

También se estableció una puerta de enlace de API que se comunica con los clientes mediante REST y con el backend utilizando gRPC. De esta manera, los clientes pueden interactuar con los microservicios sin necesidad de salirse de lo convencional (`REST`) para ellos.

Además se logró que los microservicios se comuniquen entre ellos en caso de ser necesario sin la necesidad de pasar la request por un intermediario.

## Descripción técnica de la solución implementada
---
Dado que la aplicación cuenta con varios componentes, en este apartado explicaremos qué bibliotecas son necesarias y sus respectivas versiones.

### API_Gateway
Este módulo es responsable de proporcionar la comunicación entre los microservicios y los clientes, y se encuentra en la carpeta [api_gateway](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/api_gateway "api_gateway").

#### Tecnologías usadas y ejecución:

Esta API esta realizada en Python, para poder correrla deberemos tener instalado [Python](https://www.python.org/downloads/release/python-3110/) en nuestro computador, asi como pip y Flask. para esto podemos ejecutar los siguientes comandos.
```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
 pip install Flask
```

Una vez tengamos las librerías podemos ejecutar el servidor usando el siguiente comando:
```bash
python3 access_point.py
```
Si todo esta correcto veremos el siguiente mensaje en consola:
![API Gateway corriendo](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/api_gateway_funcionando.png)

Ahora podemos empezar a realizar peticiones a nuestro API.
#### Librerías:

Las librerías necesarias para poder correr este módulo son:

|Nombre librería| Versión | Propósito | Link |
|--|--|--|--|
| pip | 20.0.2 | Gestor de paquetes de python.| https://pypi.org/project/pip/ | https://flask.palletsprojects.com/en/2.2.x/ |
| flask | 2.2.3 | Permite la configuracion de un server y el setup de varios metodos HTTP |
| dotenv | 1.0.0 | Proporciona una forma de cargar variables de entorno desde un archivo `.env` en una aplicación python.| https://pypi.org/project/python-dotenv/ |
| grpcio | 1.51.3 | Es una biblioteca de Python que proporciona soporte para la implementación del Protocolo de Llamada a Procedimiento Remoto de Google (GRPC) en Python.| https://pypi.org/project/grpcio/ |

### add_stock

Este modulo es el responsable de agregar productos a la base de datos si no existian previamente, esto se logra haciendo uso de los dos metodos que expone el servicio del inventario. [add_stock](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/add_stock "add_stock")

#### Tecnologías usadas y ejecución:
Este servicio esta realizado en Python, para poder correrlo deberemos tener instalado [Python](https://www.python.org/downloads/release/python-3110/) en nuestro computador, asi como pip. para esto podemos ejecutar los siguientes comandos.
```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
```

Una vez tengamos las librerías podemos ejecutar el servidor usando el siguiente comando:
```bash
python3 back.py
```
Si todo esta correcto veremos el siguiente mensaje en consola:
![add_stock_funcionando](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/add_stock_funcionando.png)

Ahora podemos empezar a realizar peticiones a nuestro microservicio.
#### Librerías:
Las librerías necesarias para poder correr este módulo son:

|Nombre librería| Versión | Propósito | Link |
|--|--|--|--|
| pip | 20.0.2 | Gestor de paquetes de python.| https://pypi.org/project/pip/ | https://flask.palletsprojects.com/en/2.2.x/ |
| dotenv | 1.0.0 | Proporciona una forma de cargar variables de entorno desde un archivo `.env` en una aplicación python.| https://pypi.org/project/python-dotenv/ |
| grpcio | 1.51.3 | Es una biblioteca de Python que proporciona soporte para la implementación del Protocolo de Llamada a Procedimiento Remoto de Google (GRPC) en Python.| https://pypi.org/project/grpcio/ |

### product_inventary

Este modulo es el responsable de manejar directamente la base de datos simulada. No lo hace con algun intermediario y es el unico capaz de acceder a base de datos. [product_inventary](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/product_inventary "product_inventary")

#### Tecnologías usadas y ejecución:
Este servicio esta realizado en Python, para poder correrlo deberemos tener instalado [Python](https://www.python.org/downloads/release/python-3110/) en nuestro computador, asi como pip. para esto podemos ejecutar los siguientes comandos.
```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
```

Una vez tengamos las librerías podemos ejecutar el servidor usando el siguiente comando:
```bash
python3 back.py
```
Si todo esta correcto veremos el siguiente mensaje en consola:
![product_inventary_funcionando](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/product_inventary_funcionando.png)

Ahora podemos empezar a realizar peticiones a nuestro microservicio.
#### Librerías:
Las librerías necesarias para poder correr este módulo son:

|Nombre librería| Versión | Propósito | Link |
|--|--|--|--|
| pip | 20.0.2 | Gestor de paquetes de python.| https://pypi.org/project/pip/ | https://flask.palletsprojects.com/en/2.2.x/ |
| dotenv | 1.0.0 | Proporciona una forma de cargar variables de entorno desde un archivo `.env` en una aplicación python.| https://pypi.org/project/python-dotenv/ |
| grpcio | 1.51.3 | Es una biblioteca de Python que proporciona soporte para la implementación del Protocolo de Llamada a Procedimiento Remoto de Google (GRPC) en Python.| https://pypi.org/project/grpcio/ |

### product_sale

Este módulo es el encargado gestionar las ventas de los productos que existen en la base de datos. Se registran en un archivo plano[product_sale](https://github.com/jgomezb11/TopicosEnTelematica/tree/main/reto1/services/product_sale "product_sale").

#### Tecnologías usadas y ejecución:
Esta API esta realizada en Node.js, para poder correrla deberemos tener instalado [Node](https://nodejs.org/en/) en nuestro computador, una vez tengamos podremos instalar las dependencias necesarias
```bash
npm install
```
Una vez tengamos las librerías podemos ejecutar el servidor usando el siguiente comando:
```bash
node back.js
```
Nos deberá salir un mensaje de confirmación como este:
![product_sale_funcionando](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/product_sale_funcionando.png)

#### Librerías:
Las librerías necesarias para poder correr este módulo son:

|Nombre librería| Versión | Propósito | Link |
|--|--|--|--|
| @grpc/grpc-js | 1.8.11 | Proporciona una implementación de cliente y servidor de gRPC (Remote Procedure Call over HTTP/2) para JavaScript basada en Node.js.| https://www.npmjs.com/package/@grpc/grpc-js |
| @grpc/proto-loader | 0.7.5 | Proporciona una forma fácil de cargar archivos de protocolo de buffers de Google (protobufs) en una aplicación Node.js.| https://www.npmjs.com/package/@grpc/proto-loader |
| dotenv | 16.0.3 | Proporciona una forma de cargar variables de entorno desde un archivo `.env` en una aplicación Node.js.| https://www.npmjs.com/package/dotenv |

## Parametrización
---
Para parametrizar las IP's de los servicios que estamos desplegando estamos usando un archivo `.env` [config.env](https://github.com/jgomezb11/TopicosEnTelematica/blob/main/reto1/config.env "config.env"). En este archivo podemos actualizar IP's y puertos de las maquinas que alojan nuestros microservicios.

Nota, no es necesario recompilar los archivos `.proto` pues en el repositorio están los archivos que generó la ultima compilación.
## Guía de uso
---
En está sección vamos a probar las 4 peticiones que le podemos hacer a nuestra API_GATEWAY. Para esto vamos a usar Postman. Es importante que se sigan los pasos de la sección anterior para tener los 4 procesos necesarios corriendo correctamente.

Cabe aclarar que a todas las peticiones hay que setearles el header `Content_Type` a `application/json`.

### Peticiones product_inventary:
#### productExist:
Función para revisar si un producto existe en el inventario.
- Método: **GET**
- Ruta: **/productExist**
- Body:
	```json
	{
    	"name_product":"grafica"
	}
	```
- Valor de response:
	```json
	{
    	"exist": "True",
    	"name_product": "grafica"
	}
	```

##### Ejemplo usando postman
![productExist](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/productExist.png)

#### writeProduct:
Función para escribir en la base de datos.
- Método: **POST**
- Ruta: **/writeProduct**
- Body:
	```json
	{
		"name_product":"grafica"
	}
	```
- Valor de response:
	```json
	{
		"exist": "True",
		"name_product": "grafica"
	}
	```
##### Ejemplo usando postman
![writeExist](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/writeProduct.png)

### Peticiones add_stock:
#### addProduct:
Función para revisar si un producto existe en el inventario y sino existe lo agrega.
- Método: **POST**
- Ruta: **/addProduct**
- Body:
	```json
	{
    	"name_product":"grafica"
	}
	```
- Valor de response:
	```json
	{
    	"exist": "True",
    	"message": "This product already exists, so it can't be added again",
    	"name_product": "grafica"
	}
	```

##### Ejemplo usando postman
![addProduct](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/addProduct.png)

### Peticiones product_sale:
#### productSale:
Función para vender productos si existe en el inventario.
- Método: **POST**
- Ruta: **/productSale**
- Body:
	```json
	{
    	"name_product":"grafica"
	}
	```
- Valor de response:
	```json
	{
    	"exist": "True",
    	"message": "This product already exists, was successfully sold!",
    	"name_product": "grafica"
	}
	```

##### Ejemplo usando postman
![productSale](https://raw.githubusercontent.com/jgomezb11/TopicosEnTelematica/main/static/img/productSale.png)
## Referencias
---

* [Protocol Buffers Documentation](https://protobuf.dev/)
* [How to Create an API Using gRPC and Node.js](https://nordicapis.com/how-to-create-an-api-using-grpc-and-node-js/)
* [Implementing gRPC In Python: A Step-by-step Guide](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)
* [Quick start for Python](https://grpc.io/docs/languages/python/quickstart/)
* [Laboratorio_N1_RPC](https://github.com/ST0263/st0263-2023-1/blob/main/Laboratorio%20N1-RPC/README.md)
