# EJECUCIÓN DEL ENTORNO
- Instalar Docker en tu ordenador
- Iniciar sesión en Docker
- Ejecutar docker-compose up para iniciar todo el entorno

# BORRAR CONTENEDORES E IMAGENES GENERADOS POR DOCKER
Se ha creado un makefile para agilizar el borrado desde la terminal. 

Se han definido 5 objetivos:
- all: para todos los contenedores y los elimina
- stop-docker: para todos los contenedores
- clean-docker: elimina todos los contenedores
- clean-images: para todas las imágenes
- clean-volume: elimina datos generados por los dockers

Para usar makefile basta con escribir make objetivo (ejemplo make clean-volume) en la terminal. Si solo se escribe make ejecutará el objetivo all.