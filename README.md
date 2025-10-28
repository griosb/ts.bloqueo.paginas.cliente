# Bloqueo de Paginas Web con FastAPI 


###### La API requiere para su funcionamiento la instalación de **Python 3.14+**  
Puedes descargarlo desde el sitio oficial:  
[![Python](https://www.python.org/static/img/python-logo.png)](https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe)

Las demás dependencias se instalarán  desde el archivo **`requirements.txt`**.

En la instalacion es **recomendable instalarlo de una vez en el PATH**, esto se logra seleccionando la siguiente opcion en el proceso de instalación:
![](https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2023/12/como-instalar-phyton-windows-11-3245424.jpg?tf=1920x)

## ¿Como instalar las depencias?

###  1 Verificar instalación de Python y pip

    python --version
    pip --version #normalmente viene con python si lo agregamos en el path en la instalacion.
    
###  2 Crear y activar un entorno virtual (Recomendado)

    python -m venv venv
    venv\scripts\activate #activar el entorno virtual
    
### 3 Instalar las dependencias del proyecto

    pip install -r requirements.txt
    
Esto instalara unicamente todas las librerias necesarias para correr la API

>si se quiere agregar mas dependencias al proyecto se necesita ejecutar 
`pip freeze > requirements.txt`

## Uvicorn 

> Cambie la direccion y la base de datos para las consultas de la api y >guardado, en el directorio config\database.py antes de ejecutar el servidor 
> `engine = create_engine("mysql+pymysql://root:root123@localhost:3306/pagesblock") >#access of the db`

Uvicorn  es un servidor ASGI rapido que se basa en uvloop y httptools. Es un componente del ecosistema asicronico de Python, recomendando usar cuando se utiliza FastAPI
```python
#en la termina ejecute este comando para ejecutar el servidor uvicorn
uvicorn main:app --reload 
#esto es para que se actualice cada que se realiza un cambio
```
con esto ya deberia poder correr su servidor sin inconveniente, y poder visualizar la API en funcionamiento.
