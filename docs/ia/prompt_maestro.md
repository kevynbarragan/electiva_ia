Prompt maestro — Análisis de requisitos del proyecto
Actúa como un Analista Senior de Requisitos, especialista en Ingeniería de Software, levantamiento de requisitos, historias de usuario y metodologías ágiles.

Debes ayudarme a realizar el levantamiento y organización de requisitos del siguiente proyecto universitario:

Proyecto
Nombre: Análisis de Intención de Compra en una Tienda Virtual.

Descripción
El proyecto busca desarrollar un sistema que permita analizar datos relacionados con el comportamiento de usuarios dentro de una tienda virtual con el objetivo de identificar o estimar su intención de compra.

El sistema contempla actividades relacionadas con carga y preparación de datos, análisis exploratorio, identificación de variables relevantes, aplicación de técnicas de Machine Learning, clasificación de la intención de compra y visualización de resultados.

Tecnologías previstas
Python
Pandas
NumPy
Scikit-learn
FastAPI
React, HTML, CSS y JavaScript
Bibliotecas para visualización de datos
Equipo
Jhon Kevyn Barragán Vásquez — backend y procesamiento de datos.
Elian Alexis Sandoval Duran — frontend e interfaz.
Jonathan Smith Bohorquez — análisis de datos y Machine Learning.
Objetivo
Realizar el proceso completo de levantamiento de requisitos del proyecto.

El proceso debe realizarse ÚNICAMENTE en este orden:

Identificación de stakeholders.
Entrevista simulada con el stakeholder/cliente.
Transcripción de la entrevista.
Análisis de la entrevista.
Requisitos funcionales.
Requisitos no funcionales.
Historias de usuario.
Criterios de aceptación.
Priorización mediante MoSCoW.
Product Backlog.
Reglas importantes
No inventes funcionalidades que estén fuera del alcance del proyecto.

No agregues épicas.

No agregues matriz de trazabilidad.

No agregues Jira.

No agregues MCP.

No agregues archivos Excel o CSV como requisito del proceso.

No agregues pagos, aplicación móvil, recomendaciones personalizadas, comercio electrónico real ni funcionalidades avanzadas que no hayan sido justificadas.

Si necesitas hacer una suposición porque no existe un cliente real, indícala claramente como SUPOSICIÓN.

La entrevista debe identificarse claramente como SIMULADA.

No presentes una entrevista simulada como si hubiera ocurrido realmente.

Evita requisitos duplicados.

Cada historia de usuario debe corresponder a una necesidad o requisito previamente identificado.

Los criterios de aceptación deben ser verificables.

La priorización MoSCoW debe estar justificada.

El Product Backlog debe contener las historias de usuario priorizadas.

Mantén consistencia entre todos los documentos.

Utiliza identificadores consistentes:

ST-001 para stakeholders.
INT-001 para preguntas o elementos de entrevista cuando sea necesario.
RF-001 para requisitos funcionales.
RNF-001 para requisitos no funcionales.
HU-001 para historias de usuario.
CA-HU-001-01 para criterios de aceptación.
Formato de historias de usuario
Utiliza obligatoriamente:

"Como [tipo de usuario], quiero [objetivo], para [beneficio]."

Formato de criterios de aceptación
Cuando sea apropiado utiliza:

Dado que [contexto], cuando [acción], entonces [resultado esperado].

Formato MoSCoW
Clasifica las historias como:

MUST: obligatorio.
SHOULD: importante, pero no indispensable.
COULD: deseable.
WON'T: no se realizará en esta versión.
Resultado
Genera los siguientes documentos independientes:

stakeholders.md
entrevista.md
transcripcion.md
requisitos-funcionales.md
requisitos-no-funcionales.md
historias-usuario.md
criterios-aceptacion.md
priorizacion-moscow.md
product-backlog.md
Antes de generar los documentos, analiza primero el proyecto y verifica que las funcionalidades propuestas sean coherentes con su objetivo.

Si falta información, realiza una suposición razonable y márcala claramente como SUPOSICIÓN.

No agregues información innecesaria solamente para hacer el proyecto parecer más grande.

------------------------------------------------------------------------------------------------------------------------------
PROMPT MAESTRO — INSIGHTBUY
1. Rol
Actúa como ingeniero de software especializado en aplicaciones web, calidad de datos, análisis exploratorio, limpieza de CSV y asistencia mediante inteligencia artificial.
2. Problema
INSIGHTBUY es un prototipo web que busca facilitar la limpieza y el análisis de datasets CSV. El usuario debe comprender los problemas detectados, evaluar recomendaciones, elegir las acciones de limpieza y comprobar sus resultados.
Actualmente existen funcionalidades operativas, pero se debe completar el flujo de recomendaciones para que las decisiones del usuario produzcan cambios reales, persistentes y verificables.
3. Contexto
El proyecto existente utiliza React + Vite para el frontend, FastAPI para el backend y SQLite como almacenamiento actual. Incluye autenticación, carga de archivos CSV, recomendaciones de calidad y análisis exploratorio.
Se debe revisar el código existente antes de realizar modificaciones. La estructura, las rutas, los componentes y los modelos actuales deben reutilizarse siempre que sea posible.
4. Objetivo
Completar el prototipo sin reconstruirlo desde cero. El usuario debe poder:
1.	Cargar un CSV y conservar el archivo original.
2.	Detectar problemas de calidad y recibir recomendaciones justificadas.
3.	Inspeccionar los registros reales afectados.
4.	Seleccionar acciones compatibles con el tipo de variable.
5.	Previsualizar los cambios antes de confirmarlos.
6.	Aplicar la limpieza únicamente después de la confirmación.
7.	Guardar los resultados y el historial de decisiones.
8.	Evitar que una misma operación confirmada se ejecute accidentalmente más de una vez.
9.	Consultar análisis exploratorios calculados sobre la versión limpia seleccionada.
10.	Descargar los resultados y comparar el estado anterior y posterior.
5. Asistencia de IA
Las recomendaciones de IA deben basarse en estadísticas y registros calculados por el backend. Deben explicar el problema, justificar las alternativas y advertir sobre los riesgos.
La IA no debe inventar datos ni ejecutar modificaciones automáticamente. La decisión final de limpieza corresponde al usuario.
6. Restricciones
•	No reconstruir el proyecto completo.
•	No eliminar ni sobrescribir funcionalidades existentes sin justificación y autorización.
•	No modificar el CSV original.
•	No eliminar ni reemplazar valores sin una acción confirmada.
•	No utilizar métodos estadísticos incompatibles con el tipo de variable.
•	No mostrar estadísticas ficticias como si fueran resultados reales.
•	No marcar operaciones fallidas como exitosas.
•	No afirmar que una función está terminada sin pruebas.
•	No exponer credenciales ni secretos.
•	No introducir dependencias innecesarias.
7. Contextualización
Antes de modificar código, inspecciona los archivos y determina qué funcionalidades ya existen, cuáles están incompletas y cuáles deben reutilizarse. Formula preguntas cuando falte información esencial. No preguntes por datos que ya estén disponibles en el proyecto.
8. Forma de trabajo
Realiza cambios pequeños, identificables y compatibles con el proyecto. Explica qué archivo se modifica, por qué se modifica y cómo probarlo. Mantén un registro de cada iteración y de las decisiones tomadas.
9. Criterios de aceptación
El prototipo solo se considera funcional cuando se verifica que las recomendaciones permiten inspeccionar registros, previsualizar cambios, confirmar acciones, guardar resultados, recuperar el estado después de recargar y mostrar estadísticas reales de la versión limpia.
La autenticación, la carga de archivos y las demás funciones existentes deben continuar funcionando.
10. Entregables
•	Prototipo funcional.
•	Prompt maestro documentado.
•	Historial de iteraciones.
•	Comparativa de prompts y resultados.
•	Evidencias de pruebas.
•	Registro de limitaciones pendientes.

TABLA DE ITERACIONES.
Iteración	Objetivo	Cambio solicitado en el prompt	Resultado y evidencia
1	Crear la base del prototipo	Definir estructura y tecnologías	Verificar contra el código inicial
2	Habilitar autenticación	Corregir registro e inicio de sesión	Hay evidencia en la conversación de que se solucionó el problema de bcrypt
3	Analizar CSV	Habilitar carga, calidad y exploración	Verificar con el dataset real
4	Mejorar recomendaciones	Mostrar acciones concretas para los problemas detectados	Pendiente de implementar y probar
5	Persistir la limpieza	Guardar versiones e impedir ejecuciones duplicadas	Pendiente de verificar
6	Actualizar el análisis	Recalcular estadísticas de la versión limpia	Pendiente de verificar
7	Validar el prototipo	Ejecutar pruebas de regresión y documentar resultados	Pendiente









PROMPT MAESTRO DEFINITIVO — INSIGHTBUY
Mejoramiento integral del prototipo funcional de calidad de datos, limpieza asistida por IA y análisis exploratorio
1. INSTRUCCIÓN PRINCIPAL
Actúa como un ingeniero de software senior especializado en React, Vite, Python, FastAPI, Pandas, NumPy, bases de datos, inteligencia artificial aplicada a calidad de datos y análisis exploratorio.
Voy a adjuntar un archivo ZIP que contiene el proyecto ACTUAL de INSIGHTBUY, incluyendo el backend y el frontend.
Tu tarea es inspeccionar ese ZIP, comprender la arquitectura existente, implementar las mejoras solicitadas directamente sobre el proyecto y entregarme un NUEVO ARCHIVO ZIP descargable que contenga el backend y el frontend completos, actualizados y funcionales.
No quiero solamente explicaciones, recomendaciones, fragmentos de código, archivos sueltos, pseudocódigo ni una maqueta visual. Quiero que implementes los cambios en el código real y me devuelvas el proyecto completo en un ZIP.
El proyecto ya funciona en sus funciones principales. No debes reconstruirlo desde cero ni sustituirlo por otro proyecto. Debes conservar lo existente y completar las funcionalidades pendientes.
El objetivo es obtener un prototipo funcional de INSIGHTBUY con participación humana real en la limpieza, recomendaciones asistidas por IA, persistencia de los cambios y análisis exploratorio correcto después de limpiar.
________________________________________
2. PROBLEMA QUE DEBE RESOLVERSE
INSIGHTBUY permite trabajar con datasets CSV y muestra recomendaciones sobre problemas de calidad de datos.
Actualmente, algunas recomendaciones pueden aceptarse sin que el usuario pueda inspeccionar suficientemente los registros afectados o sin que se produzca una modificación real de los datos.
El sistema debe dejar de ser un simple detector de problemas y convertirse en un flujo funcional donde:
1.	Se detecta un problema.
2.	Se explica y justifica una recomendación.
3.	El usuario inspecciona los registros reales afectados.
4.	El usuario decide qué acción aplicar.
5.	El sistema calcula una vista previa.
6.	El usuario confirma la operación.
7.	El backend ejecuta la limpieza real.
8.	Los cambios quedan guardados.
9.	La operación no se repite accidentalmente.
10.	El análisis exploratorio muestra estadísticas de la versión limpia.
11.	El usuario puede descargar el resultado y consultar el historial.
La decisión final sobre la limpieza debe pertenecer al usuario.
________________________________________
3. CONTEXTO DEL PROYECTO EXISTENTE
El ZIP adjunto contiene el proyecto que debes modificar.
Según el estado conocido, el proyecto utiliza:
•	Frontend: React + Vite.
•	Backend: Python + FastAPI.
•	Base de datos actual: SQLite.
•	Dataset de referencia: online_shoppers_intention.csv.
•	Variable objetivo de referencia: Revenue.
El proyecto ya cuenta con funcionalidades principales como autenticación, carga de CSV, consulta de datasets, recomendaciones de calidad, limpieza, descarga y análisis exploratorio.
Estos datos son contexto inicial. Verifica todo directamente en el ZIP antes de modificar el código.
No supongas que una función falta si ya existe. Tampoco supongas que funciona solo porque hay un endpoint, botón o componente relacionado.
Debes identificar qué funciona realmente y completar únicamente lo necesario.
No cambies SQLite por PostgreSQL ni reemplaces la arquitectura actual sin una necesidad técnica demostrable.
________________________________________
4. ENTREGA OBLIGATORIA
Debes devolver un único archivo ZIP final que incluya:
•	El backend completo y actualizado.
•	El frontend completo y actualizado.
•	Los archivos de configuración necesarios.
•	Las dependencias declaradas.
•	Las nuevas migraciones o mecanismos de inicialización de base de datos, si son necesarios.
•	Las pruebas implementadas.
•	Las instrucciones de instalación y ejecución.
•	Un README actualizado.
•	La documentación de las mejoras y de las iteraciones realizadas.
La estructura debe conservar la organización existente del proyecto siempre que sea posible. Por ejemplo, si el ZIP original contiene backend/ y frontend/, el ZIP final debe conservar esas carpetas.
No entregues un ZIP con solo los archivos modificados. Debe ser el proyecto completo, listo para descomprimir y probar.
No incluyas carpetas pesadas o generadas que no sean necesarias, como node_modules/, entornos virtuales .venv/, cachés, archivos temporales ni bases de datos personales con información sensible.
No incluyas contraseñas, tokens, claves API reales ni secretos del entorno. Conserva plantillas de configuración seguras, como .env.example, cuando corresponda.
No inventes una ruta de descarga: genera realmente el archivo ZIP y proporciona el enlace al archivo creado.
________________________________________
5. PRIMERA FASE: INSPECCIÓN Y PROTECCIÓN
Antes de editar:
1.	Descomprime y revisa el ZIP.
2.	Inspecciona la estructura del backend y del frontend.
3.	Localiza los componentes del asistente de calidad.
4.	Identifica las funciones actuales de detección, limpieza y análisis exploratorio.
5.	Revisa los modelos de datos, las rutas API y el mecanismo de persistencia.
6.	Comprueba cómo se almacenan los CSV y los resultados de limpieza.
7.	Verifica qué estadísticas son calculadas realmente y cuáles podrían ser valores de demostración.
8.	Identifica si ya existe un proveedor o modelo de IA integrado.
9.	Revisa las dependencias, las variables de entorno y las pruebas.
10.	Determina cómo ejecutar el proyecto en Windows.
Conserva la autenticación, las rutas, los componentes y las funciones que ya funcionan.
Realiza cambios incrementales y localizados. No reemplaces archivos completos cuando sea suficiente modificar una parte.
No elimines información existente para facilitar la implementación.
Si hay errores previos, distingue entre problemas preexistentes y problemas introducidos por los cambios.
Si el ZIP contiene información sensible, no la reproduzcas en la documentación ni en el resultado.
Después de la inspección, continúa con la implementación. No te limites a entregarme un diagnóstico o un plan.
________________________________________
6. ASISTENTE DE CALIDAD CON PARTICIPACIÓN HUMANA
Cada recomendación debe convertirse en una acción útil.
En cada tarjeta de recomendación, mostrar:
•	Tipo de problema.
•	Dataset y versión analizada.
•	Variable o columnas afectadas.
•	Número de registros afectados.
•	Porcentaje del dataset afectado.
•	Método utilizado para detectar el problema.
•	Explicación comprensible del hallazgo.
•	Recomendación sugerida y justificación.
•	Riesgos o consecuencias de cada alternativa.
•	Estado actual de la recomendación.
Implementa o completa las siguientes acciones de interfaz:
•	Ver registros afectados.
•	Buscar y filtrar registros.
•	Seleccionar filas individualmente.
•	Seleccionar varias filas.
•	Elegir la acción de limpieza.
•	Configurar sus parámetros.
•	Previsualizar los cambios.
•	Confirmar la operación.
•	Cancelar sin modificar los datos.
•	Consultar el resultado.
•	Consultar el historial de operaciones.
Si una recomendación indica «Solo revisión; no modifica los valores», el botón de aceptación debe abrir los registros reales afectados y ofrecer opciones apropiadas para revisarlos o tratarlos.
No consideres que una recomendación se ha ejecutado si solo cambia su estado visual.
Si una acción no modifica valores porque el usuario eligió conservarlos o revisar los registros, muestra claramente esa decisión y registra la revisión cuando corresponda.
________________________________________
7. INSPECCIÓN REAL DE LOS REGISTROS
Cuando el usuario pulse «Ver registros» o acepte una recomendación, debe poder consultar los datos reales del CSV.
La vista debe incluir:
•	Identificador estable del registro o fila de origen.
•	Columnas relevantes.
•	Valor original.
•	Motivo por el que se identificó el problema.
•	Método y límites utilizados, cuando correspondan.
•	Selección individual y múltiple.
•	Búsqueda, filtros y paginación.
No cargues innecesariamente miles de filas completas en el navegador. Utiliza consultas paginadas y filtros en el backend cuando resulte apropiado.
Las filas deben corresponder a la versión exacta del dataset y de la recomendación.
No inventes valores de ejemplo en la tabla real. Si utilizas datos ficticios para una demostración automatizada, identifícalos explícitamente como datos de prueba.
Si el CSV no tiene un identificador único, crea una referencia de fila estable durante la ingestión y conserva su correspondencia con los datos originales y sus versiones.
________________________________________
8. ACCIONES REALES DE LIMPIEZA
Implementa acciones funcionales y compatibles con el tipo de variable.
A. Valores atípicos
El usuario debe poder elegir:
1.	Conservar los valores.
2.	Marcar registros para revisión.
3.	Reemplazar valores seleccionados por la media.
4.	Reemplazar valores seleccionados por la mediana.
5.	Limitar valores extremos mediante capping.
6.	Eliminar filas seleccionadas de la versión de trabajo.
7.	Excluir registros del análisis sin borrarlos del archivo original.
8.	Introducir un valor personalizado cuando sea compatible.
Para capping, permite elegir IQR o percentiles y configurar sus parámetros cuando corresponda.
Para cada acción, muestra los registros afectados y los valores originales y propuestos.
La media o mediana debe calcularse realmente sobre los datos válidos de referencia. Debes definir claramente qué registros entran en el cálculo y excluir los valores que no deban contribuir.
No confundas reemplazar los valores atípicos seleccionados por la media con calcular la media de toda la columna.
No elimines automáticamente todos los candidatos a valores atípicos.
B. Valores nulos
Permite:
•	Conservarlos.
•	Reemplazarlos por la media, cuando sea estadísticamente apropiado.
•	Reemplazarlos por la mediana.
•	Reemplazarlos por la moda, cuando sea apropiado.
•	Reemplazarlos por un valor personalizado válido.
•	Eliminar filas seleccionadas.
•	Eliminar columnas solo después de advertir al usuario y confirmar.
•	Excluir registros del análisis sin borrar los datos originales.
Muestra cuántos valores faltantes serán tratados y cómo quedarán.
C. Duplicados
Permite:
•	Mostrar las filas duplicadas.
•	Comparar los registros.
•	Definir o consultar el criterio de duplicidad.
•	Elegir qué registro conservar.
•	Eliminar los duplicados seleccionados de la versión de trabajo tras confirmar.
•	Mostrar cuántas filas se eliminarán.
D. Tipos incorrectos y categorías
Permite:
•	Identificar valores incompatibles con el tipo esperado.
•	Mostrar los valores que no pueden convertirse.
•	Convertir tipos cuando sea seguro.
•	Corregir o mapear categorías.
•	Marcar valores para revisión.
•	Validar categorías permitidas.
No trates automáticamente códigos categóricos como magnitudes continuas. Por ejemplo, Browser, Region y TrafficType no deben recibir una limpieza por IQR solo porque estén codificados numéricamente.
Si una acción no es compatible con el tipo de variable, deshabilítala o explica por qué no puede utilizarse.
________________________________________
9. VISTA PREVIA OBLIGATORIA
La vista previa debe calcularse con el backend sobre los datos reales.
Antes de confirmar, mostrar:
•	Acción elegida.
•	Parámetros utilizados.
•	Dataset y versión de origen.
•	Registros que se modificarán.
•	Valores originales y propuestos.
•	Filas que se eliminarán.
•	Registros que se excluirán del análisis.
•	Cantidad de celdas modificadas.
•	Cantidad de filas antes y después.
•	Estadísticas relevantes antes y después.
•	Riesgos de pérdida de información o sesgo.
La vista previa debe ser temporal y no aplicar la limpieza definitiva.
El usuario debe poder volver atrás, cambiar la acción o cancelar.
Si no se puede calcular la vista previa, muestra un error y no habilites la confirmación.
No presentes cifras ficticias como si fueran resultados reales.
________________________________________
10. CONFIRMACIÓN Y EJECUCIÓN
Cuando el usuario confirme:
1.	Valida la acción, sus parámetros y las filas seleccionadas.
2.	Comprueba que la versión de origen no haya cambiado desde la vista previa.
3.	Ejecuta exactamente la transformación confirmada.
4.	Valida el dataset resultante.
5.	Guarda una nueva versión limpia.
6.	Registra la operación y el resultado.
7.	Actualiza el estado de la recomendación.
8.	Recalcula o invalida las estadísticas afectadas.
9.	Devuelve al frontend un resumen verificable.
No basta con mostrar un mensaje «Limpieza exitosa». Debe comprobarse que el resultado se haya generado y guardado correctamente.
Si la operación falla, no publiques una versión parcial como si estuviera limpia. Conserva la versión anterior y muestra un mensaje de error útil.
________________________________________
11. PERSISTENCIA, VERSIONES E HISTORIAL
El usuario no debe tener que repetir el procedimiento cada vez que abra el dataset.
Implementa un mecanismo compatible con la base de datos actual para guardar:
•	Dataset original.
•	Versiones limpias.
•	Versión activa.
•	Historial de operaciones.
•	Recomendaciones y su estado.
•	Acción elegida.
•	Parámetros utilizados.
•	Registros afectados.
•	Valores originales y nuevos, cuando corresponda.
•	Usuario que confirmó.
•	Fecha y hora.
•	Resultado de la operación.
•	Errores, si ocurrieron.
Conserva el archivo original intacto.
No vuelvas a ejecutar automáticamente una limpieza solo porque el usuario recargó la página o volvió a abrir el dataset.
Cada operación confirmada debe tener un identificador único y un mecanismo de idempotencia. Repetir la misma solicitud por doble clic o por un reintento no debe aplicar dos veces la misma transformación.
Utiliza transacciones y controles de concurrencia cuando corresponda.
Si se necesitan nuevas tablas, modelos o migraciones, incorpóralos de forma compatible y documentada. No borres tablas existentes ni reinicialices la base de datos del usuario.
Después de reiniciar el backend y volver a iniciar sesión, el usuario debe poder recuperar las versiones y el historial persistidos.
________________________________________
12. ESTADOS DE LAS RECOMENDACIONES
Implementa estados claros, persistidos y coherentes:
•	Detectada.
•	Seleccionada.
•	Pendiente de confirmación.
•	Aplicada.
•	Descartada.
•	Error.
•	Revisada sin cambios.
•	Problema todavía presente, si corresponde después de volver a analizar.
No vuelvas a presentar una recomendación ya aplicada como si nunca hubiera sido atendida.
Sin embargo, no ocultes artificialmente problemas que persisten. Un nuevo análisis puede detectar un nuevo hallazgo, actualizar su cantidad o indicar que todavía quedan registros por tratar.
Las recomendaciones deben estar vinculadas al dataset y a la versión que se analizó. No reutilices una recomendación antigua sobre una versión diferente sin verificarla.
________________________________________
13. ANÁLISIS EXPLORATORIO DESPUÉS DE LA LIMPIEZA
El análisis exploratorio debe mostrar los resultados calculados sobre la versión activa del dataset.
Después de cada limpieza confirmada, recalcula o recupera estadísticas correspondientes a esa versión.
Incluye, según el tipo de datos:
•	Filas y columnas.
•	Tipos de datos.
•	Valores nulos.
•	Duplicados.
•	Media.
•	Mediana.
•	Desviación estándar.
•	Mínimo y máximo.
•	Cuartiles.
•	Frecuencias categóricas.
•	Distribuciones.
•	Histogramas.
•	Diagramas de caja.
•	Correlaciones entre variables numéricas.
•	Distribución de Revenue cuando la variable exista.
•	Problemas de calidad que persistan.
•	Comparación antes y después de limpiar.
Todos los resultados deben calcularse con los datos reales mediante el backend.
No uses valores hardcodeados ni resultados de demostración como si fueran estadísticas del dataset actual.
Muestra claramente el nombre y la versión del dataset que se está analizando.
La comparación antes y después debe permitir identificar:
•	Qué cambió.
•	Qué permaneció igual.
•	Qué problemas se resolvieron.
•	Qué problemas persisten.
•	Cuántas filas o celdas cambiaron.
•	Si hubo pérdida de registros.
•	Cómo cambiaron las estadísticas relevantes.
Si la limpieza falla, conserva los resultados válidos de la versión anterior y no muestres estadísticas parciales como definitivas.
La descarga debe generar el CSV correspondiente a la versión seleccionada.
________________________________________
14. INTEGRACIÓN REAL DE INTELIGENCIA ARTIFICIAL
Inspecciona si el ZIP ya incluye un proveedor o modelo de IA.
No inventes claves API ni supongas que existe una integración que no esté implementada.
Separa claramente:
1.	Motor estadístico: detecta problemas y calcula métricas reales.
2.	Asistente de IA: interpreta los resultados y propone tratamientos justificados.
3.	Motor de limpieza: ejecuta la acción determinista confirmada por el usuario.
Si ya existe una integración de IA, reutilízala y comprueba su funcionamiento.
Si no existe, implementa una integración desacoplada y segura solo si hay suficiente configuración disponible. Si requiere una clave o servicio externo que no está disponible, deja el mecanismo preparado, documenta la variable de entorno necesaria y no simules una IA real.
Las reglas estadísticas deben seguir funcionando incluso si el proveedor de IA no está disponible.
Las recomendaciones de IA deben incluir explicación, alternativas y riesgos. No permitas que el modelo invente registros, estadísticas o resultados, ni que elimine o modifique datos sin la confirmación explícita del usuario.
________________________________________
15. FRONTEND Y EXPERIENCIA DE USUARIO
Conserva el diseño y la navegación existentes de INSIGHTBUY.
Integra las mejoras en las pantallas actuales, sin crear una aplicación separada.
El asistente de calidad debe permitir completar el flujo sin abandonar innecesariamente el dataset.
Incluye:
•	Tabla de registros afectados.
•	Paginación y filtros.
•	Selección múltiple.
•	Selector de acción.
•	Configuración de parámetros.
•	Vista previa.
•	Confirmación.
•	Indicador de procesamiento.
•	Mensajes de éxito y error.
•	Resumen de cambios.
•	Estado de cada recomendación.
•	Historial de operaciones.
•	Acceso a las versiones.
•	Análisis exploratorio actualizado.
Los botones deben ejecutar acciones reales contra el backend. No implementes botones decorativos ni respuestas simuladas.
Mantén la interfaz consistente con la estructura actual y evita cambios visuales innecesarios.
________________________________________
16. SEGURIDAD Y COMPATIBILIDAD
No elimines ni reconstruyas las funciones existentes de:
•	Registro e inicio de sesión.
•	Autenticación.
•	Carga de CSV.
•	Gestión de datasets.
•	Recomendaciones.
•	Limpieza.
•	Descarga.
•	Análisis exploratorio.
•	Navegación.
No modifiques credenciales ni expongas secretos.
No incluyas .env con claves reales en el ZIP final.
No cambies SQLite por PostgreSQL sin una necesidad demostrada.
No borres archivos, tablas ni datasets existentes para facilitar la implementación.
No sustituyas funciones reales por mocks o datos ficticios.
Si introduces dependencias, deben quedar declaradas en los archivos correspondientes y ser compatibles con el entorno del proyecto.
No cambies rutas API existentes sin una razón justificada. Si necesitas nuevas rutas, intégralas de forma compatible con las actuales.
________________________________________
17. PRUEBAS OBLIGATORIAS
Ejecuta las pruebas que permita el entorno disponible y añade pruebas para los casos que falten.
Verifica como mínimo:
1.	Backend inicia correctamente.
2.	Frontend compila y se inicia.
3.	Registro e inicio de sesión siguen funcionando.
4.	Se puede cargar un CSV.
5.	Se detecta un problema real.
6.	Se muestran los registros afectados.
7.	Se seleccionan registros individuales y múltiples.
8.	Se calcula una vista previa real.
9.	Cancelar no modifica los datos.
10.	Confirmar aplica la acción elegida.
11.	Los valores modificados coinciden con la transformación esperada.
12.	El archivo original permanece intacto.
13.	La nueva versión queda guardada.
14.	La limpieza persiste después de recargar.
15.	Un reintento no duplica la operación.
16.	El análisis exploratorio refleja los datos limpios.
17.	La descarga corresponde a la versión seleccionada.
18.	Las recomendaciones se actualizan correctamente.
19.	Las acciones incompatibles con una variable se bloquean.
20.	Los errores no se registran como operaciones exitosas.
21.	Las funciones originales siguen funcionando.
Utiliza datasets de prueba pequeños con resultados conocidos para comprobar matemáticamente las transformaciones.
No hagas pruebas destructivas sobre los datos reales del usuario.
Si no puedes ejecutar alguna prueba, indícalo explícitamente. No afirmes que la prueba pasó si no se ejecutó.
________________________________________
18. DOCUMENTACIÓN Y TRAZABILIDAD DE LA IA
Esta es una entrega académica que requiere documentar el proceso de ingeniería asistida por IA.
Incluye en el ZIP una documentación que contenga:
•	El prompt maestro utilizado.
•	El problema inicial.
•	El contexto del proyecto.
•	Las restricciones.
•	Las preguntas de contextualización que fueron necesarias.
•	Las iteraciones realmente realizadas.
•	El prompt exacto de cada iteración cuando esté disponible.
•	Las diferencias entre prompts.
•	Los archivos modificados por iteración.
•	Los cambios realizados.
•	Los errores detectados.
•	Las pruebas ejecutadas.
•	Los resultados verificados.
•	Las limitaciones pendientes.
No inventes un número histórico de iteraciones ni afirmes que se utilizaron prompts que no puedan comprobarse.
Si esta ejecución comienza con un único prompt maestro, regístrala como la iteración correspondiente y añade las iteraciones posteriores a medida que realmente ocurran.
Diferencia los resultados verificados de las hipótesis y de las tareas pendientes.
________________________________________
19. INSTRUCCIONES DE INSTALACIÓN Y EJECUCIÓN
Incluye un README en español que explique cómo:
1.	Descomprimir el proyecto.
2.	Crear y activar el entorno virtual del backend en Windows.
3.	Instalar las dependencias.
4.	Configurar las variables de entorno sin incluir secretos reales.
5.	Iniciar FastAPI.
6.	Instalar las dependencias del frontend.
7.	Iniciar React + Vite.
8.	Abrir la aplicación.
9.	Cargar el dataset.
10.	Probar las recomendaciones y la limpieza.
11.	Verificar la persistencia.
12.	Comprobar el análisis exploratorio.
13.	Ejecutar las pruebas.
Respeta los puertos y comandos existentes cuando sean compatibles con la configuración real del ZIP.
No inventes rutas, módulos ni comandos sin verificarlos en el código.
________________________________________
20. CRITERIOS FINALES DE ACEPTACIÓN
El trabajo se considera terminado únicamente si:
•	Se modificó el proyecto real contenido en el ZIP.
•	El backend y frontend completos están incluidos en el ZIP final.
•	Las funciones existentes se conservaron.
•	Las recomendaciones permiten consultar los registros reales afectados.
•	El usuario puede elegir acciones de limpieza.
•	La vista previa muestra los cambios reales.
•	La confirmación ejecuta la acción seleccionada.
•	Los resultados quedan guardados.
•	La misma operación no se repite accidentalmente.
•	El CSV original permanece intacto.
•	El análisis exploratorio utiliza la versión limpia.
•	Las estadísticas se calculan con datos reales.
•	El usuario puede descargar la versión resultante.
•	Las pruebas ejecutadas y sus resultados están documentados.
•	El historial de iteraciones se conserva.
•	El ZIP final se puede descargar y contiene el backend y frontend completos.
No consideres suficiente que la aplicación se vea bien. Debe ejecutar las acciones y conservar sus resultados.
________________________________________
21. RESPUESTA FINAL OBLIGATORIA
Cuando termines, entrega:
1.	Un enlace descargable al ZIP completo generado.
2.	Un resumen de las mejoras implementadas.
3.	La lista de archivos principales modificados.
4.	Los comandos exactos para ejecutar backend y frontend en Windows.
5.	Las pruebas ejecutadas y sus resultados reales.
6.	Las instrucciones para comprobar una limpieza completa.
7.	Las limitaciones que todavía existan.
8.	La documentación del prompt maestro y de las iteraciones incluida en el ZIP.
Si una funcionalidad no pudo implementarse o probarse, dilo claramente.
No me entregues únicamente un plan. No me pidas que copie manualmente decenas de fragmentos de código. No generes un proyecto independiente de ejemplo.
Procesa el ZIP adjunto, implementa las mejoras sobre el proyecto existente, verifica el resultado y devuélveme un único ZIP final con backend y frontend completos y actualizados.

