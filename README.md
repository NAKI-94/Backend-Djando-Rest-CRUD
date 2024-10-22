# Backend de la Aplicación - Django REST

Este es el backend de la aplicación desarrollado con Django y Django REST Framework. Esta guía te llevará a través del proceso de instalación, ejecución y configuración de la aplicación.

## Tabla de Contenidos

- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Configuración](#configuración)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu computadora:

1. **Python**: Necesitas Python para ejecutar el backend. Puedes descargar la última versión desde [aquí](https://www.python.org/downloads/). Asegúrate de que Python esté en tu PATH.

2. **pip**: Es el gestor de paquetes para Python y generalmente se incluye con la instalación de Python. Puedes verificar si está instalado ejecutando el siguiente comando:
   ```bash
   pip -V
Esto debería mostrar la versión instalada de pip.

Instalación
Clonar el repositorio: Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

bash
Copiar código
git clone https://github.com/NAKI-94/Backend-Django-Rest-CRUD.git
Navegar a la carpeta del proyecto:

bash
Copiar código
cd Backend-Django-Rest-CRUD
Crear un entorno virtual (opcional pero recomendado): Es recomendable usar un entorno virtual para gestionar las dependencias. Puedes crear uno ejecutando:

bash
Copiar código
python -m venv venv
Luego, activa el entorno virtual:

En Windows:
bash
Copiar código
venv\Scripts\activate
En macOS/Linux:
bash
Copiar código
source venv/bin/activate
Instalar dependencias: Asegúrate de que el entorno virtual esté activado y ejecuta el siguiente comando para instalar todas las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Este comando instalará Django, Django REST Framework y cualquier otra dependencia que hayas listado en el archivo requirements.txt.

Ejecución
Realizar las migraciones de la base de datos: Antes de ejecutar el servidor, necesitas aplicar las migraciones:

bash
Copiar código
python manage.py migrate
Crear un superusuario (opcional): Si deseas acceder al panel de administración de Django, puedes crear un superusuario con el siguiente comando:

bash
Copiar código
python manage.py createsuperuser
Ejecutar el servidor de desarrollo: Finalmente, puedes iniciar el servidor de desarrollo con el siguiente comando:

bash
Copiar código
python manage.py runserver
Acceder a la API: Abre tu navegador y visita http://127.0.0.1:8000/ para ver la API en funcionamiento. Si creaste un superusuario, puedes acceder al panel de administración en http://127.0.0.1:8000/admin.

Configuración
Configuración de variables de entorno: Si necesitas configurar variables de entorno, puedes hacerlo en un archivo .env. Asegúrate de que tu proyecto esté configurado para leer estas variables (puedes usar la biblioteca django-environ para facilitar esto).
Uso
Instrucciones sobre cómo usar la API, incluyendo ejemplos de rutas y métodos disponibles.

Contribuciones
Hacer un fork del repositorio.

Crear una nueva rama:

bash
Copiar código
git checkout -b nombre-de-la-rama
Realizar cambios y confirmar:

bash
Copiar código
git commit -m "Descripción de los cambios"
Enviar los cambios:

bash
Copiar código
git push origin nombre-de-la-rama
Crear un Pull Request.
