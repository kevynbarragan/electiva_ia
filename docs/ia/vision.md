Documento de Visión

Problema
Cuando un usuario navega por una tienda virtual, deja un rastro de acciones —páginas visitadas, clics, tiempo dedicado a cada producto, artículos añadidos al carrito— que normalmente no se interpreta de forma organizada. Esto impide reconocer, a partir de ese comportamiento, si un usuario está cerca de decidir una compra o simplemente está explorando el catálogo.

Usuarios objetivo [SUPUESTO] Personas encargadas de la operación o análisis de una tienda virtual que deseen comprender mejor el comportamiento de sus visitantes. [SUPUESTO] Docentes o jurados evaluadores del proyecto académico, quienes revisarán el sistema como entregable curricular.
El contexto no especifica con exactitud quién operará el sistema en un escenario real (equipo de análisis, área comercial, desarrolladores), por lo que este punto queda abierto para definirse en etapas posteriores.

Necesidad identificada
Se requiere una herramienta que tome datos de navegación de una tienda virtual, los procese y, a partir de ellos, determine un nivel de intención de compra (baja, media o alta) por usuario, mostrando ese resultado de forma clara mediante tablas y gráficos.

Propuesta de valor
El proyecto ofrece una aplicación web que toma el rastro de navegación de un usuario dentro de una tienda virtual —incluyendo productos consultados, clics realizados, tiempo invertido y artículos agregados al carrito— y lo transforma, mediante un modelo de aprendizaje automático, en una clasificación concreta del nivel de intención de compra. El resultado se entrega de forma visual, a través de tablas y gráficos, facilitando su interpretación.

Solución propuesta
La aplicación contempla el siguiente flujo funcional:

Obtención de un conjunto de datos de navegación (cargado o ya disponible). Preparación de esos datos para su análisis (limpieza y transformación). Selección de las variables que resulten relevantes para el análisis de intención de compra. Construcción o aplicación de un modelo de aprendizaje automático sobre dichas variables. Clasificación de cada usuario en uno de tres niveles: baja, media o alta intención de compra. Despliegue de los resultados en una interfaz web, con apoyo de tablas y gráficos.

Alcance del MVP Carga o utilización de un conjunto de datos de navegación. Procesamiento y preparación de los datos. Identificación de las variables relevantes para el análisis. Desarrollo y/o aplicación de un modelo de aprendizaje automático. Estimación de la intención de compra en tres niveles: baja, media, alta. Visualización de los resultados en una aplicación web. Presentación de resultados mediante tablas y gráficos básicos.

Fuera del alcance Procesamiento de pagos o integración con pasarelas de pago. Generación de recomendaciones personalizadas de productos. Desarrollo de una versión móvil de la aplicación. Incorporación de un módulo de chat o mensajería. Sistema de notificaciones para usuarios o administradores. Cualquier funcionalidad de inteligencia artificial adicional que no esté directamente relacionada con la estimación de intención de compra definida en el MVP. [SUPUESTO] Conexión en tiempo real con una tienda virtual activa; se asume trabajo sobre un conjunto de datos ya existente o simulado, pues el contexto no indica que el sistema deba operar sobre tráfico en vivo.

Beneficios esperados Un conjunto de datos de navegación, antes disperso, queda organizado y disponible para análisis. Se obtiene una clasificación concreta (baja, media, alta) del nivel de intención de compra para los usuarios analizados. Los resultados quedan disponibles en un formato visual (tablas y gráficos) que facilita su lectura e interpretación. El equipo obtiene un producto académico que evidencia la aplicación práctica de un modelo de aprendizaje automático sobre un problema de comportamiento de usuario.

Supuestos [SUPUESTO] El desarrollo se apoyará en un conjunto de datos de navegación ya disponible (por ejemplo, un dataset público), ya que el contexto no precisa su origen. [SUPUESTO] El equipo posee las bases necesarias en desarrollo web y aprendizaje automático para completar el MVP dentro de las 12 semanas. [SUPUESTO] La prioridad del proyecto está en el análisis y la correcta visualización de resultados, más que en un diseño visual elaborado. [SUPUESTO] La evaluación del proyecto se hará en un contexto académico, no como un sistema desplegado con usuarios reales.

Preguntas abiertas ¿El conjunto de datos de navegación será proporcionado, público, o el equipo deberá construirlo/simularlo? ¿Qué variables estarán realmente disponibles en los datos (tiempo de navegación exacto, número de clics, historial detallado) y con qué granularidad? ¿Se cuenta con algún etiquetado previo de intención de compra (baja/media/alta) que sirva como referencia para entrenar el modelo, o deberá definirse un criterio propio? ¿La aplicación debe permitir cargar nuevos conjuntos de datos durante su uso, o trabajará sobre un dataset fijo a lo largo de todo el proyecto? ¿Qué nivel de desempeño del modelo (por ejemplo, exactitud mínima) se considerará suficiente, tomando en cuenta el tiempo disponible de 12 semanas?

CORRECCION DE VISION:

Documento de Visión
1. Problema
Cuando un usuario navega por una tienda virtual, deja un rastro de acciones —páginas visitadas, clics, tiempo dedicado a cada producto, artículos añadidos al carrito— que normalmente no se interpreta de forma organizada. Esto impide reconocer, a partir de ese comportamiento, si un usuario está cerca de decidir una compra o simplemente está explorando el catálogo.

2. Contexto del equipo
El proyecto es desarrollado por 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué, con 12 semanas efectivas de desarrollo disponibles.

3. Usuarios objetivo
[SUPUESTO] Personas encargadas de la operación o análisis de una tienda virtual que deseen comprender mejor el comportamiento de sus visitantes. [SUPUESTO] Docentes o jurados evaluadores del proyecto académico, quienes revisarán el sistema como entregable curricular.

El contexto no especifica con exactitud quién operará el sistema en un escenario real (equipo de análisis, área comercial, desarrolladores), por lo que este punto queda abierto para definirse en etapas posteriores. Se recomienda priorizar una de las dos audiencias para orientar decisiones de diseño (ver sección "Decisiones que debemos tomar" del análisis asociado).

4. Necesidad identificada
Se requiere una herramienta que tome datos de navegación de una tienda virtual, los procese y, a partir de ellos, determine un nivel de intención de compra (baja, media o alta) por usuario, mostrando ese resultado de forma clara mediante tablas y gráficos.

5. Propuesta de valor
El proyecto ofrece una aplicación web que toma el rastro de navegación de un usuario dentro de una tienda virtual —incluyendo productos consultados, clics realizados, tiempo invertido y artículos agregados al carrito— y lo transforma, mediante un modelo de aprendizaje automático, en una clasificación concreta del nivel de intención de compra. El resultado se entrega de forma visual, a través de tablas y gráficos, facilitando su interpretación.

[SUPUESTO] El enfoque de modelado (supervisado con etiquetas de referencia, o no supervisado mediante agrupamiento) está aún por definir, ya que no se ha confirmado la existencia de un etiquetado previo de intención de compra.

6. Solución propuesta
La aplicación contempla el siguiente flujo funcional:

Obtención de un conjunto de datos de navegación (cargado o ya disponible).
Preparación de esos datos para su análisis (limpieza y transformación).
Selección de las variables que resulten relevantes para el análisis de intención de compra.
Construcción o aplicación de un modelo de aprendizaje automático sobre dichas variables.
Clasificación de cada usuario en uno de tres niveles: baja, media o alta intención de compra.
Despliegue de los resultados en una interfaz web, con apoyo de tablas y gráficos.
7. Alcance del MVP
Carga o utilización de un conjunto de datos de navegación.
Procesamiento y preparación de los datos.
Identificación de las variables relevantes para el análisis.
Desarrollo y/o aplicación de un modelo de aprendizaje automático.
Estimación de la intención de compra en tres niveles: baja, media, alta.
Visualización de los resultados en una aplicación web.
Presentación de resultados mediante tablas y gráficos básicos.
8. Fuera del alcance
Procesamiento de pagos o integración con pasarelas de pago.
Generación de recomendaciones personalizadas de productos.
Desarrollo de una versión móvil de la aplicación.
Incorporación de un módulo de chat o mensajería.
Sistema de notificaciones para usuarios o administradores.
Cualquier funcionalidad de inteligencia artificial adicional que no esté directamente relacionada con la estimación de intención de compra definida en el MVP.
[SUPUESTO] Conexión en tiempo real con una tienda virtual activa; se asume trabajo sobre un conjunto de datos ya existente o simulado, pues el contexto no indica que el sistema deba operar sobre tráfico en vivo.
9. Beneficios esperados
Un conjunto de datos de navegación, antes disperso, queda organizado y disponible para análisis.
Se obtiene una clasificación concreta (baja, media, alta) del nivel de intención de compra para los usuarios analizados.
Los resultados quedan disponibles en un formato visual (tablas y gráficos) que facilita su lectura e interpretación.
El equipo obtiene un producto académico que evidencia la aplicación práctica de un modelo de aprendizaje automático sobre un problema de comportamiento de usuario.
10. Supuestos
[SUPUESTO] El desarrollo se apoyará en un conjunto de datos de navegación ya disponible (por ejemplo, un dataset público), ya que el contexto no precisa su origen.
[SUPUESTO] El equipo posee las bases necesarias en desarrollo web y aprendizaje automático para completar el MVP dentro de las 12 semanas.
[SUPUESTO] La prioridad del proyecto está en el análisis y la correcta visualización de resultados, más que en un diseño visual elaborado.
[SUPUESTO] La evaluación del proyecto se hará en un contexto académico, no como un sistema desplegado con usuarios reales.
[SUPUESTO] Existe o puede construirse un criterio de etiquetado de intención de compra que permita entrenar o validar el modelo.
11. Preguntas abiertas
¿El conjunto de datos de navegación será proporcionado, público, o el equipo deberá construirlo/simularlo?
¿Qué variables estarán realmente disponibles en los datos (tiempo de navegación exacto, número de clics, historial detallado) y con qué granularidad?
¿Se cuenta con algún etiquetado previo de intención de compra (baja/media/alta) que sirva como referencia para entrenar el modelo, o deberá definirse un criterio propio?
¿La aplicación debe permitir cargar nuevos conjuntos de datos durante su uso, o trabajará sobre un dataset fijo a lo largo de todo el proyecto?
¿Qué nivel de desempeño del modelo (por ejemplo, exactitud mínima) se considerará suficiente, tomando en cuenta el tiempo disponible de 12 semanas?