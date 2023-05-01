# DEFINICIÓN DE UN PLAN DE DESPLIEGUE DE LA APLICACIÓN 

* Estado: propuesta
* Responsables: Oihana, Juana, Nadia y Ainara
* Fecha: 01/05/2023

Historia técnica: -

## Contexto y Planteamiento del Problema

Definición del plan de despliegue de la aplicación incluyendo su despliegue en un entorno de producción y en un entorno de desarrollo. 

## Factores en la Decisión 

* Fácilidad de uso a través de nuestra herramienta de CI Gitlab

## Decisión

 Plan de despliegue elegido: 
 
 	*Si se desea realizar un despliegue en un entorno de producción, se realizará un commit con 			un tag extra utilizando Gitlab. Este tag permite tener la versión concreta de la aplicación. 
 	
 	*En el caso de que se desee realizar un despliegue en desarrollo, el commit no poseerá ningún tag ya que siempre se va a partir de la versión latest. En caso de que se haya enviado una versión a producción, por ejemplo, V1.0 y se desee actualizar ésta con una nueva versión, siempre que estemos en el mismo RFI, lo reflejaremos de la siguiente manera: v1.1 v1.2 v1.3 
 	
 	*Cada RFI va a suponer una nueva versión de nuestra aplicación. 

## Ventajas y Desventajas de las opciones

### Desarrollo en diferentes ramas 
La rama main sería la encargada de realizar el despliegue en producción.
* Negativo, serían necesarios test unitarios y de integración que abarquen todo el código. 

### Cada versión de la aplicación en un repositorio diferente 
* Positivo, no sería necesario utilizar tags. 
* Negativo, sobrecarga de repositorios. 
