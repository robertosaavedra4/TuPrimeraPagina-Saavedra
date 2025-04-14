import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TuPrimeraPagina.settings')
django.setup()

# Importa lo necesario
from django.db import connection

# Crear tabla de migraciones si no existe
with connection.cursor() as cursor:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "django_migrations" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        "app" varchar(255) NOT NULL, 
        "name" varchar(255) NOT NULL, 
        "applied" datetime NOT NULL
    )
    ''')
    
    # Crear las tablas de mascotas
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