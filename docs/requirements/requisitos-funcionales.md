Requisitos Funcionales
1. Introducción
Los requisitos funcionales describen las funciones que deben realizar el sistema Análisis de Intención de Compra en una Tienda Virtual para cumplir con su objetivo.

Estos requisitos fueron definidos a partir de las necesidades identificadas durante la entrevista simulada y de los objetivos establecidos para el proyecto.

RF-001 — Conjunto de datos de Cargar
Descripción:

El sistema debe permitir cargar el conjunto de datos que contiene información relacionada con el comportamiento de los usuarios de la tienda virtual.

Fuente: INT-004

Prioridad preliminar: Alta.

RF-002 — Conjunto de datos de validación
Descripción:

El sistema debe validar que el conjunto de datos cargado contiene información utilizable para realizar el análisis.

Fuente: INT-005

Prioridad preliminar: Alta.

RF-003 — Identificar problemas en los datos
Descripción:

El sistema debe identificar problemas presentes en los datos, como valores faltantes, inconsistencias o información que requiera tratamiento antes del análisis.

Fuente: INT-005

Prioridad preliminar: Alta.

RF-004 — Preparar los datos
Descripción:

El sistema debe permitir preparar los datos para que puedan ser utilizados correctamente durante el análisis y el entrenamiento del modelo.

Fuente: INT-006

Prioridad preliminar: Alta.

RF-005 — Realizar análisis exploratorio
Descripción:

El sistema debe permitir realizar un análisis exploratorio del conjunto de datos para conocer sus características y comportamiento.

Fuente: INT-007

Prioridad preliminar: Alta.

RF-006 — Identificar variables relevantes
Descripción:

El sistema debe permitir identificar las variables que presentan una relación relevante con la intención de compra y que puedan ser utilizadas en el modelo.

Fuente: INT-008

Prioridad preliminar: Alta.

RF-007 — Entrenar modelo de Machine Learning
Descripción:

El sistema debe permitir entrenar un modelo de Machine Learning utilizando los datos preparados y las variables seleccionadas.

Fuente: INT-009

Prioridad preliminar: Alta.

RF-008 — Evaluar modelo
Descripción:

El sistema debe permitir evaluar el desempeño del modelo mediante métricas adecuadas para determinar la calidad de sus resultados.

Fuente: INT-010

Prioridad preliminar: Alta.

RF-009 — Clasificar intención de compra
Descripción:

El sistema debe permitir clasificar la intención de compra de los registros analizados utilizando el modelo entrenador.

Fuente: INT-011

Prioridad preliminar: Alta.

RF-010 — Consultar resultados
Descripción:

El sistema debe permitir consultar los resultados obtenidos después de ejecutar el análisis.

Fuente: INT-012

Prioridad preliminar: Alta.

RF-011 — Visualizar resultados mediante tablas
Descripción:

El sistema debe permitir mostrar los resultados del análisis mediante tablas organizadas.

Fuente: INT-013

Prioridad preliminar: Media-Alta.

RF-012 — Visualizar resultados mediante gráficos
Descripción:

El sistema debe permitir representar información relevante del análisis mediante gráficos que faciliten su interpretación.

Fuente: INT-013

Prioridad preliminar: Media-Alta.

RF-013 — Informar errores de procesamiento
Descripción:

El sistema debe informar al usuario cuando ocurre un error durante la carga, validación, preparación o procesamiento de los datos.

Fuente: INT-005

Prioridad preliminar: Alta.

RF-014 — Ejecutar el flujo de análisis
Descripción:

El sistema debe permitir ejecutar el flujo necesario para procesar los datos, realizar el análisis, utilizar el modelo y obtener los resultados de intención de compra.

Fuente: INT-019

Prioridad preliminar: Alta.

2. Resumen
IDENTIFICACIÓN	Requisito	Prioridad
RF-001	Conjunto de datos de Cargar	Alta
RF-002	Conjunto de datos de validación	Alta
RF-003	Identificar problemas en los datos	Alta
RF-004	Preparar los datos	Alta
RF-005	Realizar análisis exploratorio	Alta
RF-006	Identificar variables relevantes	Alta
RF-007	Entrenar modelo	Alta
RF-008	Evaluar modelo	Alta
RF-009	Clasificar intención	Alta
RF-010	Consultar resultados	Alta
RF-011	Visualizar mediante tablas	Media-Alta
RF-012	Visualizar mediante gráficos	Media-Alta
RF-013	Informar errores	Alta
RF-014	Ejecutar flujo de análisis	Alta
3. Alcance funcional
El sistema se enfocará en el análisis de datos y la clasificación de intención de compra. No se incluyen funcionalidades de pago, comercio electrónico completo, recomendaciones personalizadas ni aplicación móvil dentro del alcance inicial.