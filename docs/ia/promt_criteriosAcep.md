# Prompt — Criterios de aceptación

Analiza todas las historias de usuario creadas para:

**Análisis de Intención de Compra en una Tienda Virtual.**

Para cada historia genera criterios de aceptación verificables.

Utiliza preferiblemente el formato:

**Dado que...**

**Cuando...**

**Entonces...**

Cada historia debe tener entre 2 y 4 criterios de aceptación, dependiendo de su complejidad.

Ejemplo:

### HU-001 — Cargar dataset

**CA-HU-001-01**

Dado que el usuario tiene un dataset válido,
cuando lo cargue,
entonces el sistema debe aceptar el archivo y mostrar que la carga fue realizada correctamente.

**CA-HU-001-02**

Dado que el usuario intenta cargar un archivo incompatible,
cuando realice la carga,
entonces el sistema debe informar que el archivo no cumple con el formato esperado.

Los criterios deben:

* Ser claros.
* Ser verificables.
* Ser específicos.
* No introducir funcionalidades nuevas.
* Corresponder directamente a la historia.
* Permitir determinar si la historia está terminada.

Entrega el resultado listo para:

docs/criterios-aceptacion.md