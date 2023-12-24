import os, time, csv
from getpass import getpass
from cryptography.fernet import Fernet

### Genera una clave encriptada para usarla como llave para encriptar y desencriptar los archivos
## Este archivo se eliminará ya que solo sera usado para generar una contraseña inicial.
def generar_llave():
    print('''Antes de comenzar deberá crear una contraseña. Mas adelante podrá cambiarla.
Recomendamos leer la documentación para salir de dudas.''')
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

if os.name == "posix":
   borrar = "rm init.py"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   borrar = "del init.py"

generar_llave()
os.system(borrar)

