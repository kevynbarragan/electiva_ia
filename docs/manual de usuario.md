MANUAL DE USUARIO
INSIGHTBUY – Análisis de Intención de Compra en una Tienda Virtual
1. Introducción
El presente manual tiene como finalidad orientar al usuario en el manejo de INSIGHTBUY, una aplicación web diseñada para facilitar la carga, revisión, preparación y análisis exploratorio de conjuntos de datos relacionados con el comportamiento de los usuarios de una tienda virtual.
La aplicación permite identificar problemas de calidad en los datos, revisar registros afectados, aplicar tratamientos de limpieza de manera controlada y consultar información estadística que facilite la comprensión de los datos.
2. Objetivo del manual
Explicar de manera clara y ordenada el funcionamiento de los módulos de INSIGHTBUY, indicando los procedimientos necesarios para registrarse, iniciar sesión, cargar conjuntos de datos, revisar su calidad, aplicar tratamientos y consultar los resultados del análisis exploratorio.
3. Requisitos para utilizar la aplicación
Para utilizar INSIGHTBUY se requiere:
•	Un computador con conexión a Internet.
•	Un navegador web actualizado, como Google Chrome o Microsoft Edge.
•	Una cuenta registrada en la aplicación.
•	Un archivo en formato CSV para realizar los análisis.
La aplicación admite archivos CSV con un tamaño máximo configurado inicialmente en 25 MB.
4. Acceso a la aplicación
4.1. Registro de usuario
Para utilizar la aplicación por primera vez, el usuario debe acceder a la pantalla de registro.
Procedimiento:
1.	Ingresar a la dirección web de INSIGHTBUY.
2.	Seleccionar la opción de registro.
3.	Introducir el nombre completo.
4.	Introducir una dirección de correo electrónico válida.
5.	Crear una contraseña de mínimo ocho caracteres.
6.	Seleccionar el botón para crear la cuenta.
Una vez completado el procedimiento, el sistema registra la cuenta y permite acceder al espacio de trabajo.
4.2. Inicio de sesión
Los usuarios que ya tienen una cuenta deben:
1.	Ingresar a la aplicación.
2.	Introducir su correo electrónico.
3.	Introducir su contraseña.
4.	Seleccionar el botón de inicio de sesión.
El sistema verifica las credenciales y permite acceder al entorno principal de INSIGHTBUY.
5. Interfaz principal
Después de iniciar sesión, el usuario encuentra un espacio de trabajo organizado en diferentes módulos.
El menú lateral permite acceder a:
•	Inicio.
•	Calidad de datos.
•	Análisis exploratorio.
•	Mis datasets.
En la parte inferior del menú se encuentra la información de la cuenta y la opción para cerrar sesión.
6. Módulo Inicio
El módulo Inicio constituye el punto de entrada al procesamiento de datos.
En esta sección se presenta una opción para seleccionar un archivo CSV desde el computador.
Procedimiento para cargar un conjunto de datos:
1.	Acceder al módulo Inicio.
2.	Seleccionar el botón de selección de archivo.
3.	Buscar el archivo CSV en el computador.
4.	Seleccionar el archivo deseado.
5.	Presionar el botón Analizar dataset.
6.	Esperar a que el sistema procese la información.
El backend verifica que el archivo tenga la extensión CSV, que no esté vacío, que pueda interpretarse y que no supere el límite de tamaño establecido.
Cuando la carga se completa correctamente, el sistema presenta información general del conjunto de datos y sus posibles problemas de calidad.
7. Módulo Calidad de datos
Este módulo permite identificar y revisar problemas presentes en el conjunto de datos.
Una vez cargado el archivo, el sistema presenta indicadores generales:
•	Cantidad de filas.
•	Cantidad de columnas.
•	Valores faltantes.
•	Registros duplicados.
También presenta recomendaciones relacionadas con los problemas identificados.
7.1. Identificación de valores faltantes
El sistema identifica valores nulos y celdas que contienen espacios vacíos.
El usuario puede revisar los registros afectados y decidir qué tratamiento aplicar.
Entre las alternativas disponibles se encuentran:
•	Reemplazar por la media.
•	Reemplazar por la mediana.
•	Reemplazar por la moda.
•	Utilizar un valor personalizado.
•	Eliminar las filas seleccionadas.
•	Excluir registros del análisis.
•	Conservar los valores sin modificaciones.
Las opciones disponibles dependen del tipo de variable.
7.2. Identificación de duplicados
El sistema identifica filas completamente duplicadas.
El usuario puede inspeccionar los registros y decidir si desea eliminar los duplicados seleccionados, excluirlos del análisis o conservarlos.
7.3. Identificación de valores atípicos
Los posibles valores atípicos se identifican mediante el método del rango intercuartílico (IQR).
El procedimiento utiliza los cuartiles Q1 y Q3 para establecer los límites de referencia.
Los valores identificados no se eliminan automáticamente, debido a que podrían representar observaciones válidas.
El usuario puede revisarlos y decidir si desea:
•	Conservar los valores.
•	Registrar únicamente su revisión.
•	Reemplazarlos por la media.
•	Reemplazarlos por la mediana.
•	Aplicar el método de capping.
•	Eliminar las filas seleccionadas.
•	Excluirlas del análisis.
7.4. Identificación de inconsistencias de tipo
El sistema puede identificar columnas que contienen valores numéricos mezclados con datos que no pueden convertirse correctamente a números.
Estos registros se presentan para su revisión y tratamiento manual.
7.5. Inspección de registros
Cada recomendación permite consultar los registros afectados.
El usuario puede:
1.	Abrir la recomendación.
2.	Consultar los registros asociados.
3.	Buscar información dentro de los registros.
4.	Seleccionar las filas que desea tratar.
5.	Elegir el método de limpieza.
La aplicación permite consultar los registros mediante páginas para facilitar su revisión.
7.6. Previsualización de cambios
Antes de aplicar una operación, el usuario debe seleccionar la opción de previsualización.
El sistema calcula los cambios propuestos y presenta información como:
•	Método seleccionado.
•	Cantidad de filas antes y después.
•	Cantidad de celdas modificadas.
•	Cantidad de filas que serían eliminadas.
•	Registros que serían excluidos del análisis.
•	Valores originales y valores propuestos, cuando corresponda.
Esta funcionalidad permite revisar las consecuencias de una operación antes de confirmarla.
7.7. Confirmación de cambios
Cuando el usuario revisa la previsualización, puede seleccionar la opción Confirmar y guardar versión.
El sistema registra la operación y, cuando existen modificaciones, genera una nueva versión del conjunto de datos de trabajo.
El archivo original se conserva sin modificaciones.
8. Módulo Análisis exploratorio
Este módulo permite comprender las características y el comportamiento de los datos mediante diferentes procedimientos estadísticos.
Para utilizarlo, el usuario debe tener un conjunto de datos cargado.
El sistema presenta los siguientes elementos:
8.1. Hallazgos iniciales
Se muestran observaciones relacionadas con:
•	Registros duplicados.
•	Valores faltantes.
•	Posibles valores atípicos.
•	Condiciones generales identificadas durante la revisión.
8.2. Estadísticas descriptivas
Se presentan estadísticas para las variables numéricas:
•	Conteo.
•	Media.
•	Mediana.
•	Desviación estándar.
•	Valor mínimo.
•	Primer cuartil (Q1).
•	Tercer cuartil (Q3).
•	Valor máximo.
•	Cantidad de candidatos a valores atípicos mediante IQR.
Estas medidas permiten conocer la distribución y el comportamiento general de las variables.
8.3. Distribuciones
La aplicación presenta representaciones de frecuencias agrupadas para las variables numéricas.
Estas permiten observar cómo se distribuyen los valores dentro de diferentes intervalos.
El sistema genera distribuciones para un máximo de doce columnas numéricas.
8.4. Matriz de correlación
Se presenta una matriz de correlación de Pearson entre las variables numéricas.
Sus valores permiten identificar asociaciones lineales positivas o negativas entre variables.
Los coeficientes se encuentran entre -1 y +1.
Es importante tener presente que una correlación no demuestra una relación de causalidad.
8.5. Vista previa de registros
El módulo también permite consultar una muestra de los registros utilizados durante el análisis exploratorio.
La vista previa presenta hasta quince filas del conjunto de datos analizado.
9. Módulo Mis datasets
Este módulo permite consultar los conjuntos de datos que han sido cargados y asociados a la cuenta del usuario.
Para consultar un conjunto de datos:
1.	Acceder a Mis datasets.
2.	Identificar el archivo que se desea consultar.
3.	Seleccionar el registro correspondiente.
4.	Esperar a que el sistema recupere la información.
5.	Consultar nuevamente sus indicadores y recomendaciones.
Cada archivo aparece identificado mediante su nombre y fecha de carga.
10. Historial y versiones
INSIGHTBUY incorpora un mecanismo de registro de las operaciones realizadas sobre los conjuntos de datos.
En el módulo de calidad se pueden consultar:
•	Versiones guardadas.
•	Fecha de creación de cada versión.
•	Operaciones de limpieza.
•	Estado de las operaciones.
•	Versión de origen de cada operación.
También se pueden descargar las versiones disponibles.
11. Descarga de archivos
La aplicación permite descargar la copia de trabajo del conjunto de datos y las versiones guardadas.
Para hacerlo:
1.	Abrir el conjunto de datos.
2.	Acceder a la sección correspondiente.
3.	Seleccionar la opción de descarga.
4.	Guardar el archivo CSV en el computador.
12. Cierre de sesión
Para finalizar el uso de la aplicación, el usuario debe seleccionar la opción Cerrar sesión ubicada en la parte inferior del menú lateral.
El sistema elimina el token de autenticación almacenado en el navegador y regresa a la pantalla de acceso.
13. Recomendaciones de uso
•	Utilizar archivos CSV correctamente estructurados.
•	Verificar que las columnas contengan información coherente.
•	Revisar las recomendaciones antes de aplicar cualquier tratamiento.
•	No eliminar registros sin comprobar previamente su importancia.
•	Utilizar la previsualización antes de confirmar una operación.
•	Descargar las versiones importantes como respaldo.
•	Interpretar las correlaciones teniendo en cuenta que no representan causalidad.
•	Conservar una copia local de los archivos originales.
14. Consideraciones finales
INSIGHTBUY proporciona herramientas para la revisión, preparación y análisis exploratorio de conjuntos de datos. Su funcionamiento permite que el usuario participe directamente en las decisiones de limpieza, evitando modificaciones automáticas sin revisión previa.
El sistema conserva el archivo original y registra las operaciones efectuadas sobre la copia de trabajo, facilitando la trazabilidad de los procedimientos realizados.

