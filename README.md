# Descripción
Administrador de contraseña (Password Manager). Herramienta CRUD de contraseñas implementando criptografía en los archivos.
## Antes de usar (Primer uso)
Ejecuta el archivo init.py para crear una contraseña de acceso y crear la llave encargada de encriptar y desencriptar los demas archivos (la contraseña de acceso y la información almacenada). Este archivo encriptará los datos creados y se eliminará a sí mismo automaticamente despues de completar su funcion.\
Si ejecuta el programa principal (**Password Manager.py**) antes del archivo init.py, el programa no funcionará correctamente.
## Manual de uso
- Antes que nada, tener en cuenta que para que el programa funcione debe de tener instalado previamente los modulos de **pandas**, **getpass**, **cryptography**
- El programa cuenta con 4 funciones: Leer, Guardar, Borrar y Salir.
- Al abrir el programa se desencriptarán los datos para poder trabajar con los archivos .key y bd.csv
- La información se guardará en el archivo bd.csv
- Para leer, guardar y/o borrar, el programa pedirá una contraseña, la cual habremos creado al momento de ejcutar el archivo init.py.
- La opcion **Borrar** te guiará para borrar columna por columna individualmente a partir de su indice. Para borrar toda la base de dato completa, borrelo desde su carpeta (el archivo csv)
- Al seleccionar la opcion salir, toda la informacion dentro de los archivos creados se encriptarán y volverán a ser desencriptados cuando vuelva a abrir el programa.
## Funciones no visibles
Dentro del programa existen funciones NO visibles para cualquier usuario, de modo que solo el desarrollador, administrador y/o quien conozcoa de ellas podrán acceder.
- Restablecer la contraseña de acceso: Se accede despues de fallar la contraseña. Al momento de preguntar "¿Olvidaste la contraseña?" deberás poner un punto (.) para acceder a la opcion de restablecer contraseña.
# Aviso
Guarde el programa y todos los archivos creados en un lugar seguro donde nadie los mueva. Y evite moverlos, ya que:
- Si mueve alguno de los archivos .key (o los borra) no podrá acceder a la información guardada. 
(Crear una nueva llave no hará que el archivo se desencripte)
