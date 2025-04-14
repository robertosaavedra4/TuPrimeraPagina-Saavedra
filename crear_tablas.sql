-- Tabla para Perros
CREATE TABLE IF NOT EXISTS "mascotas_perro" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nombre" varchar(50) NOT NULL,
    "raza" varchar(50) NOT NULL,
    "sexo" varchar(10) NOT NULL
);

-- Tabla para Gatos
CREATE TABLE IF NOT EXISTS "mascotas_gato" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nombre" varchar(50) NOT NULL,
    "raza" varchar(50) NOT NULL,
    "sexo" varchar(10) NOT NULL
);

-- Tabla para Pájaros
CREATE TABLE IF NOT EXISTS "mascotas_pajaro" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nombre" varchar(50) NOT NULL,
    "raza" varchar(50) NOT NULL,
    "sexo" varchar(10) NOT NULL
); 