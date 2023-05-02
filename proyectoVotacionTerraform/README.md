# PRERREQUISITOS
Primero hay que instalarse AWS CLI en nuestro ordenador. Es una herramienta de código abierto que nos permite interactuar con los servicios de AWS desde la terminal. También, será necesaria la intalación de terraform. Para poder acceder a nuestra cuenta de aws, hay que colocar las credenciales en el siguiente directorio: ~/.aws/credentials.

# PASO 1 - SUBIR IMÁGENES AL REPOSITORIO ECR EN AWS
Previamente, hay que acceder a la cuenta de aws y en el servicio ECR crear un repositorio. La imagen que se va a subir al repositorio es el Dockerfile que aparece en proyectoVotacionTerraform. 

Para crear la imagen Dockerfile en docker, hay que iniciar nuestra cuenta de docker y posteriormente, ejecutar este comando: 
"docker build -t <nombreImagen> .".

Se ha creado el script pushContainer.sh para automatizar la subida. Dentro del archivo tenemos que especificar estas 4 variables:

- ACCOUNT_ID: Tu id de la cuenta de aws.
- AWS_DEFAULT_REGION: La región en la que está ubicada tu cuenta.
- IMAGE_DOCKER_NAME: nombre de tu imagen docker.
- IMAGE_REPO_NAME: nombre de tu repositorio ECR en aws.

Posteriormente, se le dan permisos al script con el siguiente comando en la terminal: chmod +x pushContainer.sh. Para finalizar, ejecutamos ./pushContainer.sh.

# PASO 2 - DESPLEGAR INFRAESTRUCTURA EN AWS USANDO TERRAFORM
Una vez realizado el paso anterior, es necesario modificar ciertas partes del fichero provider.tf y main.tf para que terraform sepa donde tiene que crear, modificar o destruir los recursos en aws.

En provider.tf se encuentra el bloque provider donde se configura el proveedor especificado. Hay que pasarle las credenciales de la cuenta aws donde se quiera crear y gestionar los recursos. Para ello, en el pluguin provider se especificarán los siguientes valores:

- region = región donde está ubicada la cuenta de aws.
- profile = perfil de nuestra cuenta.
- shared_credentials_file = "~/.aws/credentials".

En main.tf se encuentran toda la infraestructura y recursos que queremos crear en nuestra cuenta de aws. Cuando se define la tarea, esta se encarga de generar un contenedor. Es necesario especificarle la ruta donde se encuentra el repositorio creado en el paso 1 y también la ruta donde se encuentra el rol.

Después de realizar estos cambios, ya se puede desplegar la infraestructura en aws. Para ello se ejecutarán los siguientes comandos:

- terraform init: Inicializa el directorio de trabajo y crea el fichero de estado.
- terraform plan: Compara el estado actual, guardado en el fichero de estado, con el código e indica los cambios que deben realizarse. 
- terraform apply: Crea los recursos especificados en main.tf.

Si se quiere eliminar todos los recursos que se han creado, basta con ejecutar terraform destroy.

# BORRAR CONTENEDORES E IMAGENES GENERADOS POR DOCKER
Se ha creado un makefile para agilizar el borrado desde la terminal. 

Se han definido 5 objetivos:
- all: para todos los contenedores y los elimina.
- stop-docker: para todos los contenedores.
- clean-docker: elimina todos los contenedores.
- clean-images: para todas las imágenes.
- clean-volume: elimina datos generados por los dockers.

Para usar makefile basta con escribir make objetivo (ejemplo make clean-volume) en la terminal. Si solo se escribe make ejecutará el objetivo all.

El makefile esta probado en un dispositivo macos. Si no funciona en otro sistema operativo como windows, cambiar en el archivo makefile rm por kill.

