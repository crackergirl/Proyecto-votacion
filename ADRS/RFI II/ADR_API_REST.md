# HERRAMIENTAS PARA LA GESTIÓN DE PROYECTOS

* Estado: aprobada
* Responsables: Oihana, Juana, Nadia y Ainara
* Fecha: 22/03/2023

Historia técnica: -

## Contexto y Planteamiento del Problema

Selección de las rutas de la API Rest de votación y de los modos y permisos necesarios para acceder a las mismas.

## Decisión
### /api/v1/[votation]/[category]
Utiliza el métogo GET para obtener el número de votos de una categoria (category) en una votación concreta (votation). Necesario para mostrar el número de votos de cada votación en la página web. Se considera un método bácico para conocer como van las votaciones, ya sea a traves de la web o directamente desde la API. Es un método accesible por todo el mundo, ya que solo solicita información, no modifica la información de las votaciones.
Como respuesta debe mostrar el nombre de la categoria seleccionada y el numero de votos. 
{
    'category' : 'cat',
    'value': 2
} 

### /api/v1/drop/[votation]
Utiliza el método DELETE para eliminar una votación. Ayuda a enriquecer la API de votación. Se considera necsario porque se permiten crear nuevas votaciones. Se ha decidido que se requiera de autentificación para poder realizar la petición. Esto es para que no cualquiera pueda modifcar la información de las votaciones, eliminandolas en este caso. Que solo puedan eliminar las votaciones ciertas personas, como por ejemplo administradores registrados. Puede resultar útil para aligerar el tamaño de la base de datos dada la estructura seleccionada, se pueden eliminar tablas de votaciones cerradas ya que no se relacionan con el resto de tablas de la BBDD.
Es necesario indicar la votacion (votation) a eliminar.

### /api/v1/reset/[votation]
Utiliza el método DELETE para eliminar todas las votaciones realizadas en una votación concreta (votation). Ayuda a enriquecer la API de votación. Se ha decido que se requiera de autentificación para poder realizar la petición. Esto es para que no cualquiera pueda modificar la información de una votación reseteándola y que solo personas previamente autorizadas puedan realizar dicha acción. Puede ser util cuando se desea reiniciar una votación que ya había finalizado, en vez de eliminar la votación, la volvemos a abrir.
Es necesario indicar la votación (votation) a resetear.

### /api/v1/new
Utiliza el método POST para crear una nueva votación. Se considera una funcionalidad básica y necesaria. Se ha decidido que requiera de autentificación para porder realizar la petición. Esto se debe a que no sería recomendable que cualquiera pueda crear las votaciones que quiera y que solo las personas autorizadas para crear las nuevas votaciones puedan hacerlo, en este caso los administradores por ejemplo. 
Es necesario indicar en el cuerpo de la votación, el nombre de la misma y los nombres de las categorías que tendrá.
{
    "name": "votation",
    "categories": {
        "value1":"cat",
        "value2":"dog"
    }
}

### /api/v1/vote/[votation]
Utiliza el método POST para votar por una categoría en una votación (votation). Es el método principal de la API, es necesario que los usuarios puedan votar. Se ha decidido que cualquiera podar votar en las votaciones, por ese motivo no requierie de autentificación ni autorización. Aunque en este caso si se modifica la información de la BBDD, creemos que la información a añadir es suficientemente concreta como para permitir que cualquiera pueda añadirla. Esta funcionalidad se puede comprobar en la página web, ya que es la principal entrada de votos. 
Es necesario especificar la votación (votation) a la que se quiere votar. Además, hay que indicar la categoría en el cuerpo de la petición: {"category": "cat"}
