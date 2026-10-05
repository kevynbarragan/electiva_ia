Requisitos No Funcionales
1. Introducción
Los requisitos no funcionales establecen las características de calidad y condiciones bajo las cuales debe funcionar el sistema Análisis de Intención de Compra en una Tienda Virtual .

Estos requisitos complementan las funcionalidades definidas y buscan garantizar que el sistema sea usable, confiable, mantenible y adecuado para el contexto académico del proyecto.

RNF-001 — Rendimiento
Categoría: Rendimiento

Descripción:

El sistema debe procesar el conjunto de datos y presentar los resultados en un tiempo razonable para el volumen de información utilizada en el proyecto.

Criterio verificable:

Las operaciones principales deben completarse sin bloqueos prolongados de la interfaz.

RNF-002 — Usabilidad
Categoría: Usabilidad

Descripción:

La interfaz debe ser sencilla e intuitiva para permitir que un usuario pueda cargar datos, ejecutar el análisis y consultar resultados sin requerir conocimientos avanzados de programación.

Criterio verificable:

Las principales acciones deben estar claramente identificadas en la interfaz.

RNF-003 — Integridad de los datos
Categoría: Integridad

Descripción:

El sistema debe evitar modificaciones accidentales de los datos originales durante el procesamiento.

Criterio verificable:

El procesamiento debe realizarse sobre una representación preparada de los datos cuando sea necesario, conservando la información original.

RNF-004 — Seguridad
Categoría: Seguridad

Descripción:

El sistema debe evitar la exposición innecesaria de información utilizada durante el procesamiento y análisis.

Criterio verificable:

Los datos y resultados no deben mostrarse a usuarios no autorizados cuando el sistema incluye mecanismos de control de acceso.

RNF-005 — Disponibilidad
Categoría: Disponibilidad

Descripción:

El sistema debe encontrarse disponible durante las pruebas y demostraciones del proyecto.

Criterio verificable:

Las funcionalidades principales deben poder ejecutarse correctamente durante las sesiones de prueba.

RNF-006 — Mantenimiento
Categoría: Mantenibilidad

Descripción:

El código debe estar organizado de manera que permita modificar o ampliar las funcionalidades del sistema sin afectar innecesariamente otros componentes.

Criterio verificable:

Los componentes de procesamiento de datos, Machine Learning, backend y frontend deben mantenerse organizados y diferenciados.

RNF-007 — Compatibilidad
Categoría: Compatibilidad

Descripción:

La aplicación web debe poder ejecutarse en navegadores web modernos compatibles con las tecnologías utilizadas.

Criterio verificable:

La interfaz debe poder utilizarse correctamente en navegadores modernos como Google Chrome o Microsoft Edge.

RNF-008 — Escalabilidad
Categoría: Escalabilidad

Descripción:

La estructura del sistema debe permitir trabajar posteriormente con conjuntos de datos de mayor tamaño sin requerir una modificación completa de la solución.

Criterio verificable:

La solución debe mantener separadas las etapas de carga, preparación, análisis y modelado para facilitar futuras ampliaciones.

RNF-009 — Interpretabilidad
Categoría: Interpretabilidad

Descripción:

Los resultados generados por el sistema deben presentarse de manera comprensible para facilitar su interpretación por parte del usuario.

Criterio verificable:

La interfaz debe mostrar claramente la clasificación y las métricas principales del análisis.

RNF-010 — Tolerancia a errores
Categoría: Confiabilidad

Descripción:

El sistema debe informar de manera comprensible los errores que ocurran durante la carga, procesamiento o análisis de los datos.

Criterio verificable:

Cuando ocurre un error controlable, el sistema debe mostrar un mensaje que indique al usuario qué operación presentó el problema.

2. Resumen
IDENTIFICACIÓN	Categoría	Requisito
RNF-001	Rendimiento	Procesamiento en tiempo razonable
RNF-002	Usabilidad	Interfaz sencilla
RNF-003	Integridad	Protección de datos originales
RNF-004	Seguridad	Protección de información
RNF-005	Disponibilidad	Disponibilidad durante las pruebas
RNF-006	Mantenibilidad	Código organizado
RNF-007	Compatibilidad	Navegadores modernos
RNF-008	Escalabilidad	Posibilidad de trabajar con mayor volumen
RNF-009	Interpretabilidad	Resultados comprensibles
RNF-010	Confiabilidad	Manejo de errores
3. Conclusión
Los requisitos no funcionales establecen las condiciones de calidad que complementan las funcionalidades del sistema y permiten que la solución sea adecuada para el análisis de intención de compra.