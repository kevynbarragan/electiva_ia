Criterios de Aceptación
1. Introducción
Los criterios de aceptación permiten determinar cuándo una historia de usuario puede considerarse correctamente implementada.

Se utiliza principalmente el formato:

Dado que...

Cuando...

Entonces...

HU-001 — Cargar dataset
CA-HU-001-01
Dado que el usuario tiene un dataset compatible,

cuando seleccione el archivo para cargarlo,

entonces el sistema debe aceptar el archivo e iniciar su procesamiento.

CA-HU-001-02
Dado que el usuario selecciona un archivo no compatible,

cuando intenta cargarlo,

entonces el sistema debe informar que el archivo no cumple con el formato esperado.

HU-002 — Validar dataset
CA-HU-002-01
Dado que existe un dataset cargado,

cuando se ejecute la validación,

entonces el sistema debe revisar la estructura y contenido básico del dataset.

CA-HU-002-02
Dado que el dataset presenta problemas,

cuando finalice la validación,

entonces el sistema debe informar los problemas identificados.

HU-003 — Identificar problemas en los datos
CA-HU-003-01
Dado que el dataset contiene valores faltantes,

cuando se analice la información,

entonces el sistema debe identificar dichos valores.

CA-HU-003-02
Dado que existen inconsistencias detectables,

cuando se ejecute la revisión,

entonces el sistema debe informar las inconsistencias encontradas.

HU-004 — Preparar los datos
CA-HU-004-01
Dado que se han identificado problemas en los datos,

cuando se ejecute el proceso de preparación,

entonces el sistema debe aplicar el tratamiento definido para esos problemas.

CA-HU-004-02
Dado que los datos han sido preparados,

cuando finalice el proceso,

entonces deben quedar disponibles para el análisis y entrenamiento del modelo.

HU-005 — Realizar análisis exploratorio
CA-HU-005-01
Dado que existe un dataset preparado,

cuando se ejecute el análisis exploratorio,

entonces el sistema debe permitir consultar información descriptiva sobre los datos.

CA-HU-005-02
Dado que existen variables en el dataset,

cuando se realice el análisis,

entonces el sistema debe permitir identificar sus características principales.

HU-006 — Identificar variables relevantes
CA-HU-006-01
Dado que los datos han sido analizados,

cuando se evalúen las variables disponibles,

entonces deben poder identificarse las variables relevantes para el modelo.

CA-HU-006-02
Dado que se seleccionan variables relevantes,

cuando finalice el proceso,

entonces estas deben quedar disponibles para el entrenamiento.

HU-007 — Entrenar modelo
CA-HU-007-01
Dado que existen datos preparados y variables seleccionadas,

cuando se ejecute el entrenamiento,

entonces el sistema debe entrenar el modelo de Machine Learning seleccionado.

CA-HU-007-02
Dado que el entrenamiento finaliza correctamente,

cuando se complete el proceso,

entonces el sistema debe generar un modelo disponible para evaluación.

HU-008 — Evaluar modelo
CA-HU-008-01
Dado que existe un modelo entrenado,

cuando se ejecute la evaluación,

entonces el sistema debe calcular métricas de desempeño.

CA-HU-008-02
Dado que se han calculado las métricas,

cuando finalice la evaluación,

entonces el sistema debe permitir consultar los resultados obtenidos.

HU-009 — Clasificar intención de compra
CA-HU-009-01
Dado que existe un modelo entrenado y evaluado,

cuando se procesen los datos correspondientes,

entonces el sistema debe generar una clasificación de intención de compra.

CA-HU-009-02
Dado que se genera una clasificación,

cuando el usuario consulte el resultado,

entonces debe poder identificar claramente el nivel de intención obtenido.

HU-010 — Consultar resultados
CA-HU-010-01
Dado que el análisis ha finalizado,

cuando el usuario consulte los resultados,

entonces el sistema debe mostrar la información generada.

CA-HU-010-02
Dado que todavía no se ha ejecutado un análisis,

cuando el usuario intente consultar resultados,

entonces el sistema debe informar que aún no existen resultados disponibles.

HU-011 — Visualizar resultados mediante tablas
CA-HU-011-01
Dado que existen resultados disponibles,

cuando el usuario acceda a la visualización,

entonces el sistema debe mostrar la información mediante una tabla organizada.

HU-012 — Visualizar resultados mediante gráficos
CA-HU-012-01
Dado que existen resultados disponibles,

cuando el usuario acceda a la visualización gráfica,

entonces el sistema debe mostrar al menos una representación gráfica de la información relevante.

CA-HU-012-02
Dado que se muestra un gráfico,

cuando el usuario lo consulte,

entonces debe poder interpretar claramente qué información representa.

HU-013 — Recibir información sobre errores
CA-HU-013-01
Dado que ocurre un error durante una operación,

cuando el sistema detecte el problema,

entonces debe mostrar un mensaje informativo al usuario.

CA-HU-013-02
Dado que ocurre un error controlable,

cuando se muestre el mensaje,

entonces este debe indicar de manera comprensible qué operación presentó el problema.

HU-014 — Ejecutar análisis completo
CA-HU-014-01
Dado que existe un dataset válido,

cuando el usuario ejecute el análisis,

entonces el sistema debe realizar las etapas necesarias para procesar los datos y generar los resultados.

CA-HU-014-02
Dado que el procesamiento finaliza correctamente,

cuando termine el análisis,

entonces el sistema debe permitir consultar la clasificación y los resultados obtenidos.

2. Criterio general de aceptación
Una historia de usuario será considerada aceptada cuando todos sus criterios de aceptación hayan sido cumplidos y puedan ser verificados mediante pruebas del sistema.