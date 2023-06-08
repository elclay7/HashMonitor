Español
# HashMonitor
 Monitoreo de archivos utilizando hashes

El repo contiene 2 scripts:

1. hashcreation.sh - Busca los hash de todos los archivos que se encuentren en los directorios seleccionados y guarda esos hash en el archivo hash.txt

2. hashmonitor.sh - Busca los hash de todos los archivos que se encuentren en los directorios seleccionados y los compara con los almacenados en hash.txt

Realiza una notificación vía correo si encuentra:

1. Archivos modificados: El hash encontrado no coincide con el almacenado en hash.txt
2. Archivos nuevos: El hash encontrado no existe en hash.txt

Ejecución manual del script

python3 hashcreation.sh
python3 hashmonitor.sh

hashmonitor.sh se recomienda ejecutarlo mediante crontab
0 */1 * * * python3 /storage/scripts/hashmonitor.sh

La creación de los hash (hashcreation.sh) se debe ejecutar de forma manual siempre y cuando estemos seguros de que nuestro sitio está limpio y ejecutarlo cada vez que realicemos una modificación de algún archivo que se encuentre dentro de los directorios monitoreados.

English
# HashMonitor
 Monitoring files using hashes

The repo contains 2 scripts:

1. hashcreation.sh - Finds the hashes of all files found in the selected directories and saves those hashes to the file hash.txt

2. hashmonitor.sh - Looks up the hashes of all files in the selected directories and compares them with those stored in hash.txt

Email notification if:

1. Files changed: The hash found does not match the one stored in hash.txt
2. New files: Found hash does not exist in hash.txt

Manual execution of the script

python3 hashcreation.sh
python3 hashmonitor.sh

hashmonitor.sh is recommended to be run via crontab
0 */1 * * * python3 /storage/scripts/hashmonitor.sh

The creation of the hash (hashcreation.sh) must be executed manually as long as we are sure that our site is clean and run it every time we make a modification to a file that is found within the monitored directories.

