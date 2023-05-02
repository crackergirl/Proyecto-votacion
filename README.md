# PROYECTO DE VOTACIÓN
Creación de una página web para votación.  El proyecto se va a desarrollar en Python Flask utilizando como IDE Visual Studio Code. También se va ha hacer uso de Docker para correr la aplicación final. La aplicación se va a desplegar en arquitecturas cloud de AWS haciendo uso de Terraform y además va a contar con una API mediante la cual se podrán consultar diferentes servicios de la aplicación.

En el directorio proyectoVotacion se encuentra el despliegue de nuestra app votación en local usando docker.
En el directorio proyectoVotacionTerraform se encuetra el despliegue de nuestra app votación en aws usando terraform.

## EQUIPO
Para este proyecto se definen 3 equipos.
* El equipo de desarrollo es el responsable de las tareas propias de desarrollo.
* El equipo de mantenimiento realiza todas las pruebas sobre la solución implementada por el equipo de desarrollo. 
* El equipo de operaciones tiene dos funciones principales: realizar pruebas de despliegue y desplegar la aplicación en el cliente final.

## ROLES
* El jefe de proyecto es responsable de las actividades de gestión y mantenimiento del proyecto. 
* El responsable de desarrollo se encarga de supervisar y dirigir el equipo de desarrollo. Es el encargado de revisar todas las tareas completadas por el equipo.
* El responsable de mantenimiento se encarga de supervisar y dirigir el equipo de mantenimiento. Es el encargado de revisar todas las tareas completadas por el equipo.
* El responsable de operaciones se encarga de supervisar y dirigir el equipo de operaciones. Es el encargado de revisar todas las tareas completadas por el equipo.

## METODOLOGÍA DE DESARROLLO Y BUENAS PRÁCTICAS
Se ha decidido usar Scrum como metodología de desarrollo para este proyecto. Scrum es una metodología que define una serie de prácticas para trabajar en equipo y desarrollar proyectos de manera ágil. 
https://es.wikipedia.org/wiki/Scrum_(desarrollo_de_software)#Beneficios_de_Scrum 

Buenas prácticas:
- Brainstorming 
- Pair programing
- Utilizar pull request para gestionar las versiones de la solución
- Redacción de ADRs
- Test unitarios
- Definir normas de nombrado de variables y funciones
- Utilizar un IDE (Visual Studio)
- Comentar o documentar el código.

## HERRAMIENTAS
-	Gitlab
-	Python Flask
-	Visual Studio Code
-	Docker
-	AWS
-	Terraform
-	APIs

## ORGANIZACIÓN Y FORMA DE TRABAJO
Para desarrollar el proyecto se han definido tres equipos y un jefe de proyecto, además cada equipo va a tener un responsable. Todos los miembros de la organización van a formar parte de todos los equipos definidos, solo que, cada uno será responsable de un equipo o fase del desarrollo.

Para gestionar el proyecto vamos a utilizar mayoritariamente Gitlab, pero también nos vamos a apoyar en Excel. Vamos a realizar un Product Backlog en Excel. En este documento vamos a especificar las historias de usuario definidas para el proyecto de votación. Las tareas en las que se descomponen las historias de usuario las vamos a llevar a gitlab en forma de issue. En nuestro caso hemos decidido crear más de una épica por proyecto, vamos a crear una épica por entrega que tengamos que realizar y al mismo tiempo cada historia de usuario será un milestone.

En Gitlab hemos creado 4 etiquetas en nuestro board: to do, doing, review y done. Cuando desglosamos las historias de usuario en tareas vamos a crear una issue por tarea. Al principio se le asigna la etiqueta to do, en cuanto el jefe de proyecto asigne la tarea a uno de los miembros para que la complete se pasara la etiqueta de la issue a doing. Una vez la persona a la que se le ha asignado la tarea la complete, pasara a la etiqueta review, donde el responsable revisara el resultado de la tarea. Una vez el responsable la revise, puede darla por finalizada y modificar la etiqueta a done. Si el responsable considera que hay algo que modificar, cambiará la etiqueta a doing y se la asignará a la persona que la ha desarrollado o a otro miembro del equipo. Además de eso, se ha definido una norma de escritura para los commits. Vamos a indicar el número de issue entre corchetes seguido del comentario del commit, [#1] – Comentario commit.

Se ha decido crear una rama por cada issue en el repositorio de Gitlab. Una vez la tarea se ha revisado y cerrado, haremos un merge request y eliminaremos la rama creada para trabajar en la tarea. La persona encargada de revisar la issue es quién va a revisar el merge request aceptándolo o no. Hacer esto puede llevar a que surjan colisiones en ficheros sobre los que se trabaja en diferentes casos. Cuando surja una colisión modificaremos el fichero para que incluya las dos versiones y aceptaremos el merge request.