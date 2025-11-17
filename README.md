# Evaluación de Modulo 7

La evaluación del Módulo 7 consta de la creación de una aplicación de gestión de productos en donde se adminitra una lista de productos con su información principal, se agrupan en categorías y se asignan etiquetas que muestran sus características.

## Desarrollo de la aplicación

La aplicación se desarrolla con Django, Framework de Desarrollo Web con Python. Se cuenta con dos aplicaciones de Django:

- Usuarios: Utiliza la aplicación preinstalada "auth" para la gestión de usuarios. La aplicación permite el registro de usuarios, el inicio y cierre de sesión. 
- Productos: Administra los productos permitiendo su creación, consulta y modificación. Está dividido en tres modelos: Producto, Categoria y Etiquetas. 

Los productos pertenecen a una categoria y a diferentes etiquetas. Pueden ser filtrados por estas mismas en la interfaz correspondiente a cada una. 

## Ejecución de la aplicación

Para ejecutar la aplicación de forma local se deben seguir los siguientes pasos (códigos para windows):

1. Clonar repositorio.

```
    git clone https://github.com/jflevig/EVAMOD7
```

2. Dentro de la carpeta clonada crear y ejecutar un entorno virtual .
```
    python -m venv venv
    .\venv\Scripts\activate
```

3. Instalar django y mysqlclient mediante pip.

```
    pip install django mysqlclient
```

4. Verificar configuración de base de datos personal (a continuación la por defecto)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'evamod7',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

5. Realizar migración a la base de datos

```
python manage.py migrate
```

6. Ejecutar servidor

```
python manage.py runserver
```

7. Para acceder a la aplicación hay que crear una cuenta y para crear productos debe haber como mínimo una categoría creada. De forma óptima primero se debe crear la categoría de los productos que se van a registrar.