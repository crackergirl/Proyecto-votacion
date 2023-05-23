# DEFINICIÓN DE LA ARQUITECTURA DEL SISTEMA DE MÉTRICAS/LOGS Y MÉTRICAS DE EVALUACIÓN EN CLOUD

* Estado: propuesta
* Responsables: Oihana, Juana, Nadia y Ainara
* Fecha: 22/05/2023

Historia técnica: -

## Contexto y Planteamiento del Problema

Definición de las métricas de evaluación en cloud para cada uno de los servicios de la aplicación y planteamiento de la arquitectura de métricas/logs. 

## Factores en la Decisión de las métricas

* Coste por gráfica: debido al límite de coste total y a que el precio por gráfica obtenida es de 0.3$, vamos a usar las métricas por recurso que aparecerán en la sección posterior para poder observar la funcionalidad del sistema. 

## Decisión

 Para cada recurso del sistema hemos decidido usar las siguientes métricas: 
 
 * Para el servicio ECS: vcpu y memoria.
 	
 * Para el balanceador de carga: número de unidades de capacidad del balanceador de carga (LCU), conexiones activas y nuevas conexiones.
 	
 * Base de datos: almacenamiento total para todas sus instancias (AllocatedStorage). 

## Factores en la Decisión de la Arquitectura del sistema de métricas/logs

* rapidez en la obtención de la representación gráfica de las métricas.

* comodidad: ofrece una única vista para todas las métricas. 

## Decisión

Se ha decidido hacer uso del dashboard de cloudwatch que ofrece AWS. De esta manera, siempre que ocurra un evento en cualquiera de los servicios, CloudWatch va a ser el encargado de obtener los parámetros deseados, el AWS System Manager guardará cada parámetro y finalmente Amazon CloudWatch mostrará cada gráfico en el Dashboard correspondiente. 



