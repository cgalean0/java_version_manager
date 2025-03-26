import os
import sys
import subprocess
import platform
from importlib import util
from time import sleep

# ==============================================
# FUNCIONES DE CONFIGURACIÓN Y VERIFICACIÓN
# ==============================================

def check_and_install_dependencies():
    """Verifica e instala las dependencias de Python necesarias"""
    required = {'colorama'}
    installed = set()
    
    print("\n🔍 Verificando dependencias de Python...")
    for lib in required:
        if util.find_spec(lib) is None:
            print(f"⚠️ {lib} no está instalado. Instalando...")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib], stdout=subprocess.DEVNULL)
                installed.add(lib)
                print(f"✅ {lib} instalado correctamente")
            except subprocess.CalledProcessError:
                print(f"❌ Error al instalar {lib}. Instálalo manualmente con: pip install {lib}")
                sys.exit(1)
    
    if installed:
        print("\n🔄 Por favor ejecuta el script nuevamente.")
        sys.exit(0)

def check_system_tools():
    """Verifica las herramientas necesarias según el SO"""
    system = platform.system().lower()
    
    if system == 'windows':
        try:
            subprocess.run(['choco', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            print("\n❌ Chocolatey no está instalado (requerido para Windows)")
            install = input("¿Instalar Chocolatey ahora? [S/N]: ").strip().lower()
            if install == 's':
                print("🛠️ Instalando Chocolatey... (Requiere permisos de admin)")
                try:
                    subprocess.run(
                        'Set-ExecutionPolicy Bypass -Scope Process -Force; '
                        '[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; '
                        'iex ((New-Object System.Net.WebClient).DownloadString("https://community.chocolatey.org/install.ps1"))',
                        shell=True, check=True, executable="powershell.exe"
                    )
                    print("✅ Chocolatey instalado. Ejecuta el script nuevamente")
                except:
                    print("❌ Error al instalar. Instálalo manualmente desde: https://chocolatey.org/install")
                sys.exit(0)
            else:
                print("🔴 Debes instalar Chocolatey para continuar")
                sys.exit(1)
    
    elif system == 'linux':
        if os.geteuid() != 0:
            print("\n🔒 Este script requiere sudo en Linux")
            print("Ejecútalo con: sudo python3 main.py")
            sys.exit(1)
        
        try:
            subprocess.run(['apt', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            print("\n⚠️ Solo compatible con Debian/Ubuntu")
            sys.exit(1)

# ==============================================
# FUNCIONES PRINCIPALES
# ==============================================

def clear_screen():
    """Limpia la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Muestra el encabezado con colores"""
    clear_screen()
    from colorama import Fore, Style
    print(Fore.CYAN + r"""
              __                                      
      / /___ __   ______ _                     
 __  / / __ `/ | / / __ `/                     
/ /_/ / /_/ /| |/ / /_/ /                      
\____/\__,_/ |___/\__,_/                       
 _   _____  __________(_)___  ____             
| | / / _ \/ ___/ ___/ / __ \/ __ \            
| |/ /  __/ /  (__  ) / /_/ / / / /            
|__________/ ________________/_____ ____  _____
  / __ `__ \/ __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / / / / / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/ /_/ /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                            /____/             
          """)
    print(Fore.YELLOW + "\n🛠️ Gestor de Versiones de Java" + Style.RESET_ALL)
    print(Fore.GREEN + "="*50 + Style.RESET_ALL)

def get_os_choice():
    """Menú de selección de SO"""
    from colorama import Fore, Style
    print(Fore.BLUE + "\nSelecciona tu sistema operativo:" + Style.RESET_ALL)
    print(Fore.WHITE + "1. Windows")
    print("2. Linux")
    print(Fore.RED + "0. Salir" + Style.RESET_ALL)
    
    while True:
        choice = input(Fore.YELLOW + "\nOpción (1/2/0): " + Style.RESET_ALL)
        if choice in ['1', '2', '0']:
            return choice
        print(Fore.RED + "❌ Opción inválida. Intenta nuevamente" + Style.RESET_ALL)

def get_java_version(os_type):
    """Menú de selección de versión Java"""
    from colorama import Fore, Style
    versions = {
        '1': ['8', '11', '17', '20', '21', '22', '23'],
        '2': ['8', '11', '17', '20', '21', '22', '23']
    }
    
    print(Fore.BLUE + "\nVersiones disponibles:" + Style.RESET_ALL)
    for i, version in enumerate(versions[os_type], 1):
        print(Fore.WHITE + f"{i}. Java {version}")
    print(Fore.RED + "0. Volver" + Style.RESET_ALL)
    
    while True:
        try:
            choice = input(Fore.YELLOW + f"\nSelecciona (1-{len(versions[os_type])}): " + Style.RESET_ALL)
            if choice == '0':
                return None
            if 1 <= int(choice) <= len(versions[os_type]):
                return versions[os_type][int(choice)-1]
            print(Fore.RED + f"❌ Ingresa un número entre 1 y {len(versions[os_type])}" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida" + Style.RESET_ALL)

def change_java_version_windows(version):
    """Cambia versión en Windows"""
    from colorama import Fore, Style
    try:
        print(Fore.GREEN + f"\n🔧 Instalando Java {version}..." + Style.RESET_ALL)
        os.system(f'choco install -y jdk{version}')
        
        print(Fore.GREEN + f"\n⚙️ Configurando Java {version} como predeterminado..." + Style.RESET_ALL)
        os.system(f'setx JAVA_HOME "C:\\Program Files\\Java\\jdk-{version}" /m')
        os.system(f'setx /M PATH "%JAVA_HOME%\\bin;%PATH%"')
        
        print(Fore.GREEN + f"\n✅ Java {version} configurado correctamente" + Style.RESET_ALL)
        print(Fore.YELLOW + "🔄 Reinicia la terminal para aplicar los cambios" + Style.RESET_ALL)
    
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {e}" + Style.RESET_ALL)

def change_java_version_linux(version):
    """Cambia versión en Linux"""
    from colorama import Fore, Style
    try:
        print(Fore.GREEN + "\n🔄 Actualizando paquetes..." + Style.RESET_ALL)
        os.system('sudo apt update -qq')
        
        print(Fore.GREEN + f"\n🔧 Instalando OpenJDK {version}..." + Style.RESET_ALL)
        os.system(f'sudo apt install -y openjdk-{version}-jdk')
        
        print(Fore.GREEN + f"\n⚙️ Configurando versión predeterminada..." + Style.RESET_ALL)
        os.system('sudo update-alternatives --config java')
        
        print(Fore.GREEN + f"\n✅ Java {version} listo" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n🔍 Verificando versión actual:" + Style.RESET_ALL)
        os.system('java -version')
    
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {e}" + Style.RESET_ALL)

# ==============================================
# EJECUCIÓN PRINCIPAL
# ==============================================

def main():
    # Verificar dependencias primero
    check_and_install_dependencies()
    check_system_tools()
    
    # Importar colorama después de verificar
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    
    while True:
        print_header()
        os_choice = get_os_choice()
        
        if os_choice == '0':
            print(Fore.MAGENTA + "\n👋 ¡Hasta luego!" + Style.RESET_ALL)
            sys.exit(0)
        
        java_version = get_java_version(os_choice)
        if java_version is None:
            continue
        
        if os_choice == '1':
            change_java_version_windows(java_version)
        else:
            change_java_version_linux(java_version)
        
        input(Fore.YELLOW + "\n↵ Presiona Enter para continuar..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()