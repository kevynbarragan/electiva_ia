DOCUMENTO TÉCNICO
INSIGHTBUY – Análisis de Intención de Compra en una Tienda Virtual
1. Introducción
INSIGHTBUY es una aplicación web orientada a la gestión, preparación y análisis exploratorio de conjuntos de datos relacionados con el comportamiento de los visitantes de una tienda virtual.
La solución permite cargar archivos CSV, identificar problemas de calidad, revisar registros afectados, aplicar tratamientos de limpieza bajo aprobación del usuario y consultar resultados estadísticos.
El sistema utiliza una arquitectura cliente-servidor, en la cual el frontend gestiona la interacción con el usuario y el backend se encarga del procesamiento de datos, la autenticación, las operaciones de limpieza y la persistencia de la información.
2. Objetivo del sistema
Desarrollar una herramienta web que facilite el análisis y preparación de datos relacionados con la actividad de los usuarios de una tienda virtual, proporcionando mecanismos para evaluar su calidad, realizar tratamientos controlados y comprender su comportamiento mediante técnicas de análisis exploratorio.
3. Alcance técnico
La implementación actual contempla:
•	Registro de usuarios e inicio de sesión.
•	Autenticación mediante tokens.
•	Carga de conjuntos de datos en formato CSV.
•	Validación básica de archivos.
•	Identificación de valores faltantes.
•	Identificación de registros duplicados.
•	Detección de posibles valores atípicos.
•	Identificación de posibles inconsistencias de tipo.
•	Inspección de registros afectados.
•	Previsualización y confirmación de operaciones de limpieza.
•	Gestión de versiones de conjuntos de datos.
•	Registro de operaciones y decisiones.
•	Análisis exploratorio de datos.
•	Visualización de estadísticas, distribuciones y correlaciones.
•	Consulta de conjuntos de datos asociados al usuario.
El entrenamiento y evaluación de modelos de Machine Learning, así como la clasificación predictiva de intención de compra, constituyen funcionalidades previstas en los requisitos del proyecto, pero no están implementadas en la versión de código documentada.
4. Arquitectura del sistema
La aplicación utiliza una arquitectura cliente-servidor.
4.1. Frontend
El frontend constituye la capa de presentación y permite al usuario interactuar con las funcionalidades del sistema.
Está desarrollado con:
•	React: construcción de componentes e interfaz de usuario.
•	JavaScript: lógica de interacción y comunicación con el backend.
•	CSS: estilos y presentación visual.
•	Vite: entorno de desarrollo y herramienta de construcción.
Entre sus responsabilidades se encuentran:
•	Presentar los formularios de autenticación.
•	Gestionar la navegación entre módulos.
•	Permitir la selección de archivos CSV.
•	Enviar solicitudes al backend.
•	Mostrar indicadores de calidad.
•	Presentar las recomendaciones de limpieza.
•	Permitir seleccionar registros.
•	Mostrar las previsualizaciones.
•	Consultar versiones e historial.
•	Presentar los resultados del análisis exploratorio.
La comunicación con el backend se realiza mediante solicitudes HTTP utilizando la API REST.
La dirección del servidor se configura mediante la variable de entorno VITE_API_URL.
4.2. Backend
El backend constituye la capa encargada de la lógica de negocio y del procesamiento de información.
Está desarrollado utilizando:
•	Python: lenguaje de programación principal.
•	FastAPI: framework para la construcción de la API REST.
•	Pandas: manipulación, limpieza y análisis de conjuntos de datos.
•	NumPy: operaciones numéricas y cálculos estadísticos.
•	SQLAlchemy: interacción con la base de datos.
•	Pydantic: validación de estructuras de entrada.
•	Passlib: manejo de contraseñas mediante funciones de hash.
•	Python-JOSE: generación y validación de tokens JWT.
•	Uvicorn: servidor ASGI para ejecutar la aplicación.
El backend se encarga de recibir las solicitudes del frontend, validar la información, ejecutar las operaciones solicitadas y devolver los resultados en formato JSON.
4.3. Base de datos
La aplicación utiliza SQLAlchemy como herramienta de mapeo objeto-relacional (ORM).
La configuración local utiliza SQLite mediante el archivo insightbuy.db.
El código también contempla la conexión a una base de datos PostgreSQL mediante la variable DATABASE_URL y el controlador psycopg.
La persistencia permite almacenar usuarios, conjuntos de datos, versiones y registros de operaciones.
5. Tecnologías utilizadas
Tecnología	Función dentro del sistema
React	Interfaz de usuario
JavaScript	Lógica del frontend
CSS	Diseño visual
Vite	Desarrollo y compilación
Python	Procesamiento del backend
FastAPI	Servicios REST
Pandas	Procesamiento de datos
NumPy	Operaciones estadísticas
SQLAlchemy	Acceso a datos
SQLite	Persistencia local
PostgreSQL	Alternativa de persistencia para despliegue
JWT	Autenticación
Passlib	Hash de contraseñas
Uvicorn	Ejecución del backend
6. Organización del proyecto
La estructura principal del proyecto se encuentra dividida en dos componentes:
Backend
•	app/
o	main.py
•	tests/
o	test_analysis.py
o	test_cleaning_workflow.py
•	requirements.txt
•	.env.example
•	insightbuy.db
El archivo main.py contiene la implementación principal de la API, los modelos de persistencia, los procedimientos de análisis y las operaciones de limpieza.
La carpeta tests contiene pruebas automatizadas para verificar funciones de análisis y tratamientos de datos.
Frontend
•	src/
o	App.jsx
o	main.jsx
o	styles.css
•	index.html
•	package.json
•	package-lock.json
•	vite.config.js
•	.env.example
El archivo App.jsx contiene la lógica principal de interacción y los módulos de la aplicación.
El archivo main.jsx inicializa la aplicación React.
El archivo styles.css define los estilos visuales.
7. Funcionamiento general del sistema
El funcionamiento de INSIGHTBUY se organiza mediante el siguiente flujo:
1.	El usuario ingresa a la aplicación.
2.	Se registra o inicia sesión.
3.	Accede al espacio de trabajo.
4.	Selecciona un archivo CSV.
5.	El frontend envía el archivo al backend.
6.	El backend valida el archivo y lo procesa utilizando Pandas.
7.	Se genera un perfil inicial del conjunto de datos.
8.	Se identifican problemas de calidad.
9.	El usuario inspecciona los registros afectados.
10.	Selecciona los tratamientos que desea aplicar.
11.	El sistema genera una previsualización.
12.	El usuario confirma la operación.
13.	El backend guarda los cambios y registra una nueva versión cuando corresponde.
14.	El usuario consulta los resultados y el análisis exploratorio.
8. Módulos y funcionamiento interno
8.1. Autenticación
El sistema incorpora mecanismos de registro e inicio de sesión.
Las contraseñas se almacenan mediante hashes utilizando Passlib y el algoritmo bcrypt.
Después de validar las credenciales, el backend genera un token JWT que permite identificar al usuario en las solicitudes posteriores.
El frontend conserva el token en el almacenamiento local del navegador y lo envía mediante la cabecera Authorization utilizando el esquema Bearer.
8.2. Carga y validación de datos
El sistema permite cargar archivos CSV.
El backend realiza las siguientes validaciones:
•	Comprueba la extensión del archivo.
•	Verifica que no esté vacío.
•	Controla el tamaño máximo permitido.
•	Intenta interpretar la codificación UTF-8 con BOM.
•	Utiliza Latin-1 como alternativa de lectura.
•	Comprueba que el contenido pueda procesarse mediante Pandas.
El tamaño máximo inicial se establece mediante MAX_UPLOAD_MB, cuyo valor predeterminado es 25 MB.
Una vez procesado, el sistema genera un identificador para el conjunto de datos y registra su información.
8.3. Perfilado de datos
El procedimiento de perfilado obtiene información general sobre el conjunto de datos.
Entre los indicadores calculados se encuentran:
•	Número de filas.
•	Número de columnas.
•	Valores faltantes.
•	Celdas vacías.
•	Tipos de datos.
•	Duplicados exactos.
•	Estadísticas de variables numéricas.
•	Frecuencias de variables categóricas.
•	Candidatos a valores atípicos.
8.4. Motor de recomendaciones de calidad
El sistema analiza las columnas y genera recomendaciones cuando identifica condiciones que requieren revisión.
Las reglas implementadas contemplan:
•	Valores faltantes y celdas vacías.
•	Filas completamente duplicadas.
•	Valores que no pueden convertirse a un tipo numérico esperado.
•	Posibles valores atípicos mediante el rango intercuartílico.
Para los valores atípicos se utiliza el método IQR, basado en los cuartiles Q1 y Q3 y el factor de referencia 1,5.
El sistema evita tratar automáticamente ciertos códigos categóricos como variables numéricas continuas.
8.5. Limpieza asistida
El proceso de limpieza se realiza bajo intervención del usuario.
Primero se identifican los registros afectados. Posteriormente, el usuario selecciona las filas y el tratamiento que desea aplicar.
El backend calcula una previsualización sin modificar inmediatamente la copia de trabajo.
Después de la confirmación, se ejecuta nuevamente la operación sobre la versión vigente y se registra el resultado.
Los tratamientos implementados incluyen:
•	Imputación por media.
•	Imputación por mediana.
•	Imputación por moda.
•	Sustitución mediante valor personalizado.
•	Eliminación de filas seleccionadas.
•	Exclusión de registros del análisis.
•	Capping de valores atípicos.
•	Conservación de valores.
•	Registro de revisiones sin modificaciones.
La disponibilidad de cada tratamiento depende del tipo de problema identificado.
8.6. Conservación de datos y versionamiento
El sistema diferencia entre el archivo original y la copia de trabajo.
El archivo original se conserva en el registro del conjunto de datos, mientras que las operaciones confirmadas pueden modificar la copia de trabajo.
Cuando una operación modifica las celdas o elimina filas, se genera una nueva versión.
El sistema registra información relacionada con:
•	Identificador de la operación.
•	Usuario responsable.
•	Acción realizada.
•	Parámetros utilizados.
•	Registros seleccionados.
•	Versión de origen.
•	Resultado de la operación.
•	Fecha de ejecución.
•	Estado de la operación.
Este mecanismo facilita la trazabilidad de los tratamientos realizados.
Las exclusiones destinadas únicamente al análisis se registran de forma separada y permiten conservar los registros en el CSV de trabajo.
8.7. Análisis exploratorio de datos
El análisis exploratorio utiliza Pandas y NumPy para obtener información estadística del conjunto de datos.
Se implementan los siguientes procedimientos:
Estadísticas descriptivas: cálculo de conteo, media, mediana, desviación estándar, mínimo, máximo y cuartiles.
Distribuciones: agrupación de frecuencias de variables numéricas mediante histogramas calculados con NumPy.
Frecuencias categóricas: identificación de los valores más frecuentes de las variables no numéricas.
Correlación: cálculo de correlaciones de Pearson entre variables numéricas.
Hallazgos: generación de observaciones sobre valores faltantes, duplicados y candidatos a valores atípicos.
El análisis considera las exclusiones registradas para la versión actual del conjunto de datos.
9. API REST
La aplicación utiliza una API REST para establecer la comunicación entre el frontend y el backend.
Los principales endpoints implementados son:
Método	Endpoint	Función
GET	/api/health	Verificar disponibilidad del backend
POST	/api/auth/register	Registrar usuario
POST	/api/auth/login	Iniciar sesión
GET	/api/auth/me	Consultar usuario autenticado
POST	/api/datasets/upload	Cargar conjunto de datos
GET	/api/datasets	Consultar datasets
GET	/api/datasets/{id}	Consultar un dataset
POST	/api/datasets/{id}/clean	Limpieza mediante endpoint heredado
GET	/api/datasets/{id}/download	Descargar copia de trabajo
GET	/api/datasets/{id}/eda	Ejecutar análisis exploratorio
GET	/api/datasets/{id}/records	Consultar registros
POST	/api/datasets/{id}/clean/preview	Previsualizar limpieza
POST	/api/datasets/{id}/clean/confirm	Confirmar limpieza
GET	/api/datasets/{id}/versions	Consultar versiones
GET	/api/datasets/{id}/versions/{version}/download	Descargar versión
GET	/api/datasets/{id}/operations	Consultar operaciones
GET	/api/datasets/{id}/decisions	Consultar decisiones
Los endpoints que consultan o modifican información protegida requieren autenticación mediante token.
10. Seguridad
La implementación contempla los siguientes mecanismos:
•	Autenticación mediante JWT.
•	Hash de contraseñas mediante bcrypt.
•	Verificación de identidad del usuario en las operaciones protegidas.
•	Comprobación de propiedad de los conjuntos de datos.
•	Validación de archivos recibidos.
•	Control del tamaño máximo de carga.
•	Configuración de orígenes permitidos mediante CORS.
•	Validación de datos de entrada.
Para un despliegue en producción se requiere configurar una clave JWT segura, utilizar HTTPS, proteger las variables de entorno y establecer una política adecuada de almacenamiento y acceso a los datos.
11. Escalabilidad y mantenibilidad
La arquitectura separa las responsabilidades de presentación, procesamiento y persistencia.
El frontend puede desplegarse independientemente del backend, mientras que la API permite incorporar nuevas funcionalidades sin reconstruir completamente la interfaz.
La utilización de Pandas y NumPy facilita la incorporación de nuevos procedimientos de análisis.
La configuración de SQLAlchemy permite utilizar PostgreSQL en lugar de SQLite para un entorno de despliegue.
Como mejoras futuras se contempla separar la lógica actualmente concentrada en main.py en módulos especializados, optimizar el almacenamiento de archivos y preparar el procesamiento para conjuntos de datos de mayor tamaño.
12. Pruebas del sistema
El proyecto incorpora pruebas automatizadas con Pytest.
Entre los aspectos cubiertos por las pruebas existentes se encuentran:
•	Cálculo de indicadores del perfil de datos.
•	Identificación de valores faltantes.
•	Detección de duplicados.
•	Previsualización de imputaciones.
•	Conservación de los datos originales durante la previsualización.
•	Eliminación controlada de duplicados.
•	Revisión de valores atípicos sin modificación automática.
•	Validación de registros seleccionados.
•	Exclusión de códigos categóricos de determinadas reglas de valores atípicos.
Estas pruebas permiten verificar partes importantes de la lógica de procesamiento y limpieza.
13. Limitaciones y funcionalidades futuras
La versión documentada se encuentra enfocada en la calidad de datos y el análisis exploratorio.
Se identifican como ampliaciones futuras:
•	Incorporación del entrenamiento de modelos de Machine Learning.
•	Evaluación mediante métricas de clasificación.
•	Predicción de intención de compra.
•	Implementación de una clasificación de intención baja, media y alta, si se define y valida previamente su metodología.
•	Optimización del almacenamiento de conjuntos de datos.
•	Incorporación de procesamiento para archivos de mayor tamaño.
•	Ampliación de las pruebas automatizadas.
•	Despliegue en infraestructura de nube.
14. Despliegue
La solución está preparada estructuralmente para separar el frontend y el backend durante el despliegue.
El frontend debe construirse como una aplicación web estática mediante Vite.
El backend debe ejecutarse como un servicio Python mediante Uvicorn.
Para el despliegue se deben configurar:
•	Variables de entorno.
•	URL pública del backend.
•	URL pública del frontend.
•	Orígenes CORS permitidos.
•	Clave JWT de producción.
•	Base de datos persistente.
•	Dependencias de cada componente.
•	Configuración de ejecución del servidor.
Como infraestructura de despliegue se contempla Microsoft Azure, utilizando servicios independientes para la interfaz web, la API y la persistencia de información.
15. Conclusión
INSIGHTBUY cuenta con una arquitectura cliente-servidor que integra tecnologías orientadas al desarrollo web y al procesamiento de datos.
La implementación actual proporciona funcionalidades para la carga, revisión, preparación, versionamiento y análisis exploratorio de conjuntos de datos.
La separación entre frontend y backend, junto con el uso de una API REST y un ORM, proporciona una base que permite mantener y ampliar el sistema.
La incorporación posterior de los componentes de Machine Learning permitirá completar el objetivo predictivo planteado para el proyecto.
