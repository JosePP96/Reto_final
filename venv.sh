#!/bin/bash

# Nombre del directorio del entorno virtual
VENV_DIR="venv"

# Verificar si el entorno virtual ya está creado
if [ ! -d "$VENV_DIR" ]; then
    # Crear el entorno virtual
    echo "Creando entorno virtual..."
    virtualenv $VENV_DIR
fi

# Activar el entorno virtual
echo "Activando entorno virtual..."
source $VENV_DIR/bin/activate

# Instalar las dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Mensaje de finalización
echo "Entorno virtual configurado y activado correctamente."