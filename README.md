# TuPrimeraPagina

Proyecto usando Django para registrar diferentes tipos de mascotas (perros, gatos y pájaros).

## Características

- Registro de perros, gatos y pájaros con sus nombres, razas y sexo
- Búsqueda de mascotas por nombre
- Interfaz sencilla y fácil de usar

## Instalación

1. Clona el repositorio
2. Instala las dependencias:
   ```
   py -m pip install django
   ```
3. Aplica las migraciones:
   ```
   py manage.py makemigrations
   py manage.py migrate
   ```
4. Ejecuta el servidor:
   ```
   py manage.py runserver
   ```
5. Abre el navegador en http://127.0.0.1:8000/

## Funcionalidades

1. **Página de inicio**: Muestra enlaces a las diferentes secciones
2. **Registro de perros**: Permite agregar y ver perros
3. **Registro de gatos**: Permite agregar y ver gatos
4. **Registro de pájaros**: Permite agregar y ver pájaros
5. **Búsqueda**: Permite buscar mascotas por nombre
