version pyton
3.12.9
Guía Rápida: Configuración del Entorno y Uso de Git
1. Crear un entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual en Python:
python -m venv .venv
2. Activarlo
Dependiendo del sistema operativo, usa el comando correspondiente:
Windows (CMD):
.venv\Scripts\activate
PowerShell:
.venv\Scripts\Activate.ps1
Linux/Mac/Git Bash:
source .venv/bin/activate
3. Instalar una librería y guardar dependencias
Ejemplo con la librería requests:
pip install requests
pip freeze > requirements.txt
4. Inicializar Git y preparar archivos
Para iniciar un repositorio Git y registrar los archivos:
git init
git add .
git commit -m "Inicio del proyecto"
5. Subirlo a GitHub
Conéctalo a un repositorio remoto y súbelo:
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
6. Ejecutar el código
Si tienes un archivo principal, ejecútalo con:
python main.py
7. Copiar y compartir el enlace del repositorio
Dirígete a GitHub y copia el enlace de tu repositorio para compartirlo.

