# SELECCIÓN DE MOTOR DE BASE DE DATOS

* Estado: propuesta
* Responsables: Oihana, Juana, Nadia y Ainara
* Fecha: 16/03/2023

Historia técnica: -

## Contexto y Planteamiento del Problema

Selección de la herramienta a utilizar para crear la base de datos de proyectos de la organización. Una herramienta para manejar y guardar los datos.

## Factores en la Decisión 

* Precio
* Fácilidad de uso
* Esfuerzo de instalación
* Funcionalidades incluidas
* Experiencia de los miembros

## Opciones Consideradas

* MySQL
* PostgreSQL
* Oracle Databse
* Microsoft SQL sever
* MariaDB

## Decisión

 Opción elegida: Elegimos MySQL como nuestro sistema de gestión de bases de datos para el proyecto porque todos los miembros del grupo tienen conocimientos y experiencia en su uso. Consideramos que esta es la mejor opción porque nos da la confianza de que podemos manejarlo con facilidad y evitando errores comunes. Además, MySQL ofrece todas las funcionalidades necesarias para crear nuestra base de datos de proyecto.

### Consecuencias

* Positiva: MySQL es conocido por ser fácil de instalar, configurar y utilizar.
* Positiva: MySQL es compatible con una amplia variedad de lenguajes de programación y sistemas operativos.
* Negativa: En algunas situaciones, MySQL puede tener problemas de rendimiento en comparación con otros sistemas de gestión de bases de datos.


## Ventajas y Desventajas de las opciones

### PostgreSQL

https://www.postgresql.org/

* Positivo, PostgreSQL es un sistema de gestión de bases de datos de código abierto, lo que significa que es completamente gratuito para usar y descargar.  
* Negativo, necesario recurrir a plugins o extensiones de terceros para acceder a determinadas funcionalidades. 
* Negativo, PostgreSQL puede no ser tan fácil de usar como algunos otros sistemas de gestión de bases de datos, como MySQL o SQLite, especialmente para principiantes. 

### Oracle Databse

https://www.oracle.com/database/

* Positivo, Oracle ofrece una gran cantidad de funciones y herramientas avanzadas que no están disponibles en otras bases de datos.
* Negativo, Oracle es una de las bases de datos más caras disponibles en el mercado.
* Negativos, Oracle puede ser difícil de usar para usuarios novatos o aquellos que no tienen experiencia en programación o bases de datos.

### Microsoft SQL sever

https://www.microsoft.com/en-us/sql-server/sql-server-downloads

* Positivo, SQL Server tiene una interfaz de usuario organizada y fácil de usar.
* Negativo, la instalación y configuración de SQL Server puede requerir hardware y software específicos, lo que puede ser costoso y complicado.
* Negativo, SQL Server puede ser costoso.


### MariaDB

https://mariadb.org/

* Positivo, MariaDB es una opción de base de datos de código abierto gratuita.
* Positivo, MariaDB tiene una interfaz de usuario intuitiva y fácil de usar, lo que la hace una buena opción para usuarios nuevos o menos experimentados.
* Negativo, algunas de sus herramientas y características avanzadas pueden requerir una licencia o suscripción, lo que puede aumentar el costo.
* Negativo, la configuración y administración de la base de datos puede requerir cierta experiencia técnica.


# SELECCIÓN DE ESTRUCTURA DE LA BASE DE DATOS

## Decisión
En la estructura seleccionada se crea una tabla por cada votación activa. Cada tabla tendrá dos campos. Primero el id de la votación que actúa como clave primaria de cada tabla. Segundo el nombre de la categoría a la que corresponde el voto. Por lo tanto, por cada voto se escribirá un nuevo registro en la tabla con el id y la categoría a la que se vota. Las tablas de cada votación son independientes, no hay relación entre ellas.

```
CREATE TABLE {} (
                    id int not null AUTO_INCREMENT,
                    category ENUM({}) NOT NULL,
                    PRIMARY KEY (id)
                )
```
### Consecuencias

#### Positivas
De esta manera aseguramos que los votos que actualicen siempre en la base de datos y que no haya problemas si dos usuarios diferentes están votando al mismo tiempo. Esto es porque no actualizan un valor sino que siempre crean uno nuevo, no realizan una acción sobre los votos que ya están insertados en la base de datos.

### Negativas
Si la aplicación obtiene una gran afluencia de votos puede hacer que las operaciones de la base de datos se ralenticen. Además, hay una gran cantidad de redundancia ya que constantemente se están escribiendo los mismos valores. 
Llegados a esta punto podemos implementar una estructura alternativa en la que en cada tabla de votación se almacene el nombre de cada categoría como clave primaria y se vaya actualizando el numero votos mediante consultas UPDATE, sumándole uno al valor actual.
Esta solución no tiene redundancia y la cantidad de datos o registros es mucho menor. Pero en este caso, que dos personas actualicen el número de votos al mismo tiempo sí que es un problema porque puede llegar a haber un desfase de votos. Por defecto el Connector/Python no autocompila, es importante llamar a commit() después de cada transacción para que modifique los datos en las tablas.
