#!/bin/bash


sudo apt update -y
sudo apt install postgresql postgresql-contrib -y


# Iniciar el servicio de PostgreSQL
sudo service postgresql start

# Crear usuario y base de datos
sudo -u postgres psql -c "CREATE USER myuser WITH PASSWORD 'mypassword';"
sudo -u postgres psql -c "CREATE DATABASE mydatabase;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;"

echo "Base de datos configurada exitosamente."