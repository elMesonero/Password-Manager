import csv, os, time
import pandas as pd
from getpass import getpass
from cryptography.fernet import Fernet

### Funcion para guardar información. 
def guardar():
    plataforma = input("Plataforma: ")
    correo = input("Correo o Usuario: ")
    clave = input("Clave: ")
    
    ## Filtra las variables antes de guardar para una mejor lectura
    plataforma_inicial_mayuscula = plataforma.capitalize()
    correo_minuscula = correo.lower()

    cuenta = [plataforma_inicial_mayuscula,correo_minuscula,clave]
    
    ## Agrega los datos dentro de un archivo y si el archivo no existe lo crea
    with open("bd.csv","a", newline='') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(cuenta)
        os.system(limpiar)
        print("***Guardado***\n")
        
    menu()
        
### Función para leer los datos almacenados dentro del archivo    
def leer():
    ## getpass() no muestra la contraseña al momento de escribirla
    contraseña = getpass("Ingrese contraseña: ")
    with open("password.key","r") as password:
        password = password.read()
        
    if contraseña == password:
        
        ## Limpia la consola
        os.system(limpiar)
        
        ## Muestra las plataformas que existen actualmente dentro del archivo
        df = pd.read_csv("bd.csv", names=["Plataforma","Correo/Usuario","Clave"])
        df_loc = df["Plataforma"]
        clean = df_loc.drop_duplicates()
        print(clean.to_string(index=False))

        ## Muestra los datos/credenciales de la plataforma consultada
        defplat = input("\nIngrese plataforma a consultar: ")
        print("\n")
        df_pf = df[df["Plataforma"] == defplat.capitalize()]
        print(df_pf.to_string(index=False))
        
        menu()
        
    else:
        ## Si la contraseña es incorrecta, envia a la funcion de verificacion y control de contraseña
        print("Contraseña incorrecta")
        time.sleep(3)
        verificacion()
        
### Función de verificacion y seguridad
def verificacion():
    print("¿Olvidaste la contraseña?")
    opcion = input("1. Si\n2. No\nNumero: ")
    
    ## Opcion no mostrada en pantalla por seguridad. 
    if opcion == ".":
        os.system(limpiar)
        
        ## Solo la conocera el desarrollador/administrador de las contraseñas
        nueva_contraseña = input("Ingrese nueva contraseña: ")
        with open("password.key","w") as archivo:
            archivo.write(nueva_contraseña)
            
        os.system(limpiar)
        print("Contraseña restablecia")
            
        menu()
        
    elif opcion == "1":
        print("Contacte con el desarrollador")
        menu()
        
    elif opcion == "2":
        os.system(limpiar)
        menu()
    
    else:
        ## Si no ingresa un numero valido, mostrara mensaje de error y volvera a repetir la funcion
        print("Error.. Ingrese un numero: ")
        verificacion()

### Función para borar fila teniendo como referencia el indice solicitado
def borrar():
    ## getpass() no muestra la contraseña al momento de escribirla
    contraseña = getpass("Ingrese contraseña: ")
    with open("python/modules/proyectos/Password Manager/password.key","r") as password:
        password = password.read()
        
    if contraseña == password:
        
        ## Limpia la consola
        os.system(limpiar)
        
        ## Muestra las plataformas que existen actualmente dentro del archivo
        df = pd.read_csv("python/modules/proyectos/Password Manager/bd_prueba.csv", names=["Plataforma","Correo/Usuario","Clave"])
        df_loc = df["Plataforma"]
        clean = df_loc.drop_duplicates()
        print(clean.to_string(index=False))

        ## Muestra los datos/credenciales de la plataforma consultada
        df_plat = input("\nIngrese plataforma a consultar: ")
        print("\n")
        df_del = pd.read_csv("python/modules/proyectos/Password Manager/bd_prueba.csv")
        df_pf = df_del[df_del["Plataforma"] == df_plat.capitalize()]
        print(df_pf)
        
        ## El usuario decide la clumna que desea eliminar a travez del indice a ingresar
        df_reset = df_del.reset_index(drop=True) # Formatea el indice de cada columna
        columna = int(input("Ingrese el indice de la columna a eliminar: "))
        df_reset.drop([columna], axis=0, inplace=True)
        df_reset.to_csv("python/modules/proyectos/Password Manager/bd_prueba.csv",index=False)
        print(df_reset)
        
        menu()
        
    else:
        ## Si la contraseña es incorrecta, envia a la funcion de verificacion y control de contraseña
        print("Contraseña incorrecta")
        time.sleep(3)
        verificacion()
        
        
### Genera una clave encriptada para usarla como llave para encriptar y desencriptar los archivos
def generar_llave():
    key = Fernet.generate_key()

    ## Guardamos la clave encriptada dentro de un archivo .key para usarla como llave
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    
### Funcion para encriptar un archivo deseado
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
    
### Funcion para desencriptar un archivo deseado
def desencriptar():
    csv = "bd.csv"
    key = "password.key"

    ## Bucle para desencriptar el archivo .csv y el archivo .key
    for i in csv, key:
        ## Guarda la llave con la clave encriptada en la variable "key"
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        ## Declara la variable con el valor de la llave a usar
        fernet = Fernet(key)

        ## Abre el archivo encriptado
        with open(f'{i}', 'rb') as file:
            encriptado = file.read()

        ## Desencripta el archivo encriptado
        desencriptado = fernet.decrypt(encriptado)

        ## Abre el archivo en modo escritura y sobrescribe con los datos desencriptados
        with open(f'{i}','wb') as file:
            file.write(desencriptado)
    
    menu()

def menu():
    var = input('''\n¿Qué desea hacer?\n
1. Ver
2. Guardar
3. Borrar
4. Salir
\nNumero: ''')
    
    if var == "1":
        os.system(limpiar)
        leer()
    elif var == "2":
        os.system(limpiar)
        guardar()
    elif var == "3":
        borrar()
    elif var == "4":
        os.system(limpiar)
        encriptar()
    else:
        print("***Error.. Ingrese un numero valido***")
        menu()

if os.name == "posix":
   limpiar = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   limpiar = "cls"

borrar()


#-crear y guardar la información - Listo
#-Clave para acceder/leer informacion - Listo
#-Editar contraseña para leer informacion al momento de olvidar contraseña - Listo
#-Encriptar contraseña para leer información
# Funcion borrar columna - Aun no funcional
#-encriptar la clave
#-encriptar el archivo csv donde se guarda
#-Funcion buscar por plataforma y/o correo-usuario
# Definir mejor la variables para que el codigo sea mas legible y comprensible
# Verificar si los archivos bd.csv y password.key existen
# mostrar clave en csv con tkinter o menu en consola
# Crear archivo/modulo aparte para generar llave y que sea autoborrable (se borre a si mismo despues de generar la llave)
# Mejorar la documentación y lectura del código 

# Ruta por emergencia: python/modules/proyectos/Password Manager/