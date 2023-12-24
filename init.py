import os, time, csv
from getpass import getpass
from cryptography.fernet import Fernet

### Genera una clave encriptada para usarla como llave para encriptar y desencriptar los archivos
## Este archivo se eliminará ya que solo sera usado para generar una contraseña inicial.
def generar_llave():
    print('''Antes de comenzar deberá crear una contraseña. Mas adelante podrá cambiarla.
Recomendamos leer la documentación para salir de dudas.\n''')
    time.sleep(3)
    nueva_contraseña = input("Ingrese una contraseña: ")
    with open("password.key","w") as archivo:
        archivo.write(nueva_contraseña)

    print("\nContraseña establecia\n")
    time.sleep(3)

    names=["Plataforma","Correo/Usuario","Clave"]
    
    with open("bd.csv","a",newline='') as bdcsv:
        escribir = csv.writer(bdcsv)
        escribir.writerow(names)
    print("bd.csv creado")
    time.sleep(3)

    key = Fernet.generate_key()

    ## Guardamos la clave encriptada dentro de un archivo .key para usarla como llave
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
        
    print("Llave creada")

def encriptar():
    csv = "bd.csv"
    key = "password.key"

    ## Bucle para encriptar el archivo .csv y el archivo .key
    for i in csv, key:
        ## Guarda la llave con la clave encriptada en la variable "key"
        with open(f'filekey.key', 'rb') as filekey:
            key = filekey.read()
            
        ## Declara la variable con el valor de la llave a usar
        fernet = Fernet(key)

        ## Abre el archivo original
        with open(f'{i}','rb') as file:
            original = file.read()

        ## Encripta el archivo original (encripta la información)
        encriptado = fernet.encrypt(original)
            
        ## Abre el archivo en modo escritura y sobrescribe con los datos encriptados
        with open(f'{i}', 'wb') as archivo_encriptado:
            archivo_encriptado.write(encriptado)

if os.name == "posix":
   borrar = "rm init.py"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   borrar = "del init.py"

generar_llave()
encriptar()
os.system(borrar)