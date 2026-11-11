#!/bin/bash
set -e

echo "Esperando a que la base de datos esté lista..."
sleep 3

# Si no existe manage.py en la carpeta montada, creamos el proyecto Django vacío
if [ ! -f "manage.py" ]; then
    echo "Creando proyecto Django inicial..."
    django-admin startproject core .
fi

echo "Aplicando migraciones a la base de datos..."
python manage.py makemigrations
python manage.py migrate

# Creación automática del superusuario utilizando variables de entorno
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    echo "Verificando/Creando superusuario..."
    python manage.py createsuperuser --noinput || true
fi

echo "Iniciando servidor de desarrollo de Django en el puerto 8000..."
exec python manage.py runserver 0.0.0.0:8000