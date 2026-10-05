Análisis de Intención de Compra en una Tienda Virtual
1. Idea del proyecto
Desarrollaremos una aplicación web capaz de analizar la intención de compra de los usuarios a partir de su comportamiento de navegación dentro de una tienda virtual.

El sistema recopilará o procesará información relacionada con el comportamiento de los usuarios, como productos visitados, cantidad de clics, tiempo de navegación, productos agregados al carrito y otras variables relevantes.

A partir de estos datos, se buscará identificar patrones de comportamiento y estimar el nivel de intención de compra de un usuario, clasificándolo, por ejemplo, como baja, media o alta intención de compra .

El propósito principal del proyecto es aplicar técnicas de análisis de datos y aprendizaje automático para transformar datos de navegación en información útil sobre el comportamiento de los usuarios.

2. MVP (Producto Mínimo Viable)
El MVP será una versión funcional y simplificada del sistema que permitirá demostrar el objetivo principal del proyecto sin incluir funcionalidades que aumenten innecesariamente el alcance.

Funcionalidades principales del MVP
Cargar o utilizar un conjunto de datos de comportamiento de navegación de usuarios.
Procesar y preparar los datos para su análisis.
Identificar las variables más relevantes relacionadas con la intención de compra.
Implementar un modelo de aprendizaje automático para estimar o clasificar la intención de compra.
Generar un resultado para cada usuario, indicando su nivel estimado de intención de compra.
Mostrar los resultados mediante una interfaz web sencilla.
Presentar información básica mediante tablas y/o gráficos para facilitar la interpretación de los resultados.
Fuera del alcance inicial
Para mantener el proyecto dentro del tiempo disponible, inicialmente no se contemplan:

Sistemas de recomendación personalizados.
Procesamiento de pagos.
Integración con tiendas virtuales comerciales reales.
Aplicaciones móviles nativas.
Sistemas avanzados de notificaciones.
Arquitecturas complejas de inteligencia artificial en tiempo real.
Estas funcionalidades podrían considerarse posteriormente si el tiempo y el avance del proyecto lo permiten.

3. Integrantes y roles
Jhon Kevyn Barragán Vásquez
ID: 912409 Rol: Desarrollo Backend y procesamiento de datos

Responsabilidades principales:

Desarrollo de la lógica del servidor.
Implementación de API necesarias para el sistema.
Preparación y procesamiento de los datos.
Integración del modelo de análisis con la aplicación web.
Manejo de la comunicación entre backend, modelo y frontend.
Elian Alexis Sandoval Duran
ID: 1050367 Rol: Desarrollo Frontend e interfaz de usuario

Responsabilidades principales:

Diseño y desarrollo de la interfaz web.
Creación de las vistas para visualizar los resultados.
Implementación de tablas, indicadores y gráficos.
Integración del frontend con el backend.
Pruebas de usabilidad y funcionamiento de la interfaz.
Jonathan Smith Bohorquez
ID: 1045541 Rol: Análisis de datos y Machine Learning

Responsabilidades principales:

Investigación y selección del conjunto de datos.
Limpieza y análisis exploratorio de los datos.
Selección de variables relevantes.
Entrenamiento y evaluación del modelo de aprendizaje automático.
Análisis de métricas y resultados del modelo.
Apoyo en la integración del modelo con el sistema.
4. Tecnologías previstas
Las tecnologías definitivas podrán ajustarse durante el desarrollo según las necesidades del proyecto.

Desarrollo frontend: React / HTML / CSS / JavaScript
Backend: Python / FastAPI
Análisis de datos: Python, Pandas, NumPy
Aprendizaje automático: Scikit-learn
Visualización: Librerías de gráficos para Python o JavaScript
Control de versiones: Git y GitHub
5. Preguntas de viabilidad
¿Podemos conseguir y preparar, dentro de las 12 semanas efectivas, un conjunto de datos reales o simulados que contenga suficiente información de navegación (páginas visitadas, duración, clics, productos vistos, carrito, etc.) y una variable objetivo que permita determinar si hubo intención de compra?

¿Qué características mínimas debe tener el sistema para que el análisis de intención de compra sea demostrable este semestre, y qué funcionalidades podemos eliminar sin afectar el objetivo principal del proyecto?

¿Podemos implementar y probar un modelo de aprendizaje automático que clasifique o estime la intención de compra con los conocimientos y recursos técnicos actuales del equipo de tres personas, sin convertir el proyecto en algo demasiado grande para el tiempo disponible?

¿Cómo vamos a manejar el principal riesgo técnico de que los datos de navegación sean insuficientes, desequilibrados, ruidosos o no tengan suficientes ejemplos de usuarios que realmente compraron para entrenar y evaluar correctamente el modelo?

¿Podemos construir en las 12 semanas un flujo completo y funcional —captura o carga de datos, procesamiento, análisis mediante el modelo y visualización del resultado en una aplicación web— y qué parte específica sería la primera en quedar fuera si el tiempo o la complejidad técnica nos obliga a reducir el alcance?

6. Estado inicial
Proyecto en etapa de planteamiento, definición del MVP y análisis de viabilidad.

El siguiente paso será establecer el conjunto de datos, definir las variables que serán utilizadas para medir la intención de compra y establecer la arquitectura inicial de la aplicación.
