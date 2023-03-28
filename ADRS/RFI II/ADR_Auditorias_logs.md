# HERRAMIENTAS PARA REALIZAR AUDITORIAS DE LOGS

* Estado: propuesta
* Responsables: Oihana, Juana, Nadia y Ainara
* Fecha: 26/03/2023

Historia técnica: 

## Contexto y Planteamiento del Problema

Selección del plugin que permita realizar auditorias de logs en Kong. 

## Factores en la Decisión 

* Lugar de almacenamiento 
* Facilidad de uso

## Opciones Consideradas

* File log
* Http log

## Decisión

Opción elegida: Hemos elegido utilizar el plugin de Kong llamado File log debido a que (como de momento) no tenemos un servidor externo donde guardar los logs, necesitamos un plugin que nos permita almacenarlos en local. 

### Consecuencias

* Positiva: permite realizar un almacenamiento en local de los ficheros de logs generados. 
* Positiva: estos ficheros se pueden leer de una manera muy cómoda haciendo uso de nuestro IDE ya elegido. 
* Negativa: pueden llegar a generarse mucha cantidad de logs en la página web que se acumularán localmente, por lo que será necesario utilizar alguna herramienta de gestión. 


## Ventajas y Desventajas de las opciones

### File log

https://docs.konghq.com/hub/kong-inc/file-log/

* Positivo: mediante la definición de un volumen, se puede definir una tubería en la que podemos leer todos los ficheros de logs generados en el contenedor de Kong y almacenarlos en una ruta local. 
* Positivo: se puede leer de una forma muy cómoda los ficheros de logs generados en forma de jsons bien estructurados utilizando el IDE Visual Studio que ya elegimos previamente. 

### Http log

https://docs.konghq.com/hub/kong-inc/http-log/

* Positivo: cuando no se dispone de un servidor externo, existe la opción mockbin que crea un contenedor temporal. Esto es útil para realizar pruebas. 
* Negativo: no posee un lugar fijo donde almacenar los logs de cara a producción. 
