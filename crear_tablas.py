import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TuPrimeraPagina.settings')
django.setup()

# Ahora podemos importar modelos
from django.db import connection

# Crea tablas manualmente usando SQL
with connection.cursor() as cursor:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "mascotas_perro" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nombre" varchar(50) NOT NULL,
        "raza" varchar(50) NOT NULL,
        "sexo" varchar(10) NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "mascotas_gato" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nombre" varchar(50) NOT NULL,
        "raza" varchar(50) NOT NULL,
        "sexo" varchar(10) NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "mascotas_pajaro" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "nombre" varchar(50) NOT NULL,
        "raza" varchar(50) NOT NULL,
        "sexo" varchar(10) NOT NULL
    )
    ''')

print("Tablas creadas correctamente") 