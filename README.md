
# Java Version Manager (JVM)

**Java Version Manager (JVM)** es una herramienta diseñada para facilitar el cambio de versiones de Java en sistemas operativos basados en Linux (actualmente compatible con Ubuntu/Debian). Su objetivo principal es simplificar el proceso para usuarios y desarrolladores que no cuentan con experiencia en la gestión de versiones mediante la terminal.

## Instalación

Para comenzar, sigue estos pasos:

### 1. Clonar el repositorio

Ejecuta el siguiente comando en la terminal para clonar el repositorio en el directorio de tu preferencia:

```bash
git clone https://github.com/cgalean0/java_version_manager.git

```

### 2. Acceder al directorio del proyecto

```bash
cd java_version_manager

```

Dentro de la carpeta encontrarás los siguientes archivos:

-   `main.py`
    
-   `requirements.txt`
    
-   `README.md`
    

### 3. Instalar dependencias

Es importante contar con **Python** instalado en tu sistema. Asumiendo que ya lo tienes, ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt

```

## Uso

### En Windows:

```bash
python3 main.py

```

### En Linux (requiere permisos de superusuario):

```bash
sudo python3 main.py

```

Sigue las instrucciones del script para seleccionar la versión de Java deseada.

## Cambio de versión posterior

Si en el futuro necesitas cambiar nuevamente de versión, simplemente ejecuta:

```bash
python3 main.py  # En Windows
sudo python3 main.py  # En Linux

```

## Compatibilidad

Actualmente, **Java Version Manager** es compatible únicamente con sistemas basados en **Ubuntu/Debian**.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, puedes enviar un **Pull Request** o contactarme directamente.

📧 [Contactar vía email](mailto:cngaleano56@gmail.com)

----------

**Licencia:** Este proyecto está bajo la licencia MIT.
