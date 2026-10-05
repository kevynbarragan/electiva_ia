PROMPT 01 — ANÁLISIS COMPETITIVO.

Actúa como analista de negocios y analista de productos digitales senior, especializado en aplicaciones web y comercio electrónico.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué. Tenemos 12 semanas efectivas para desarrollar un proyecto académico.

Nuestro proyecto consiste en desarrollar una aplicación web capaz de analizar la intención de compra de los usuarios de una tienda virtual a partir de su comportamiento de navegación.

La aplicación analizará variables como productos visitados, cantidad de clics, tiempo de navegación, productos agregados al carrito y otras variables disponibles en los datos. El objetivo es identificar patrones y estimar si un usuario presenta una intención de compra baja, media o alta.

El MVP contempla:

Cargar o utilizar datos de comportamiento de navegación.
Procesar y preparar los datos.
Identificar variables relevantes.
Utilizar un modelo de aprendizaje automático.
Estimar el nivel de intención de compra.
Mostrar los resultados en una interfaz web mediante tablas y gráficos.
TAREA: Realiza un análisis competitivo de 3 soluciones, aplicaciones, plataformas o proyectos existentes que tengan relación directa con el análisis del comportamiento de usuarios, analítica de comercio electrónico, predicción de compras o intención de compra mediante datos.

FORMATO: Entrega una tabla Markdown con las siguientes columnas:

| Competidor/Solución | Qué hace | Relación con nuestro proyecto | Tecnologías o enfoque conocido | Fortalezas | Limitaciones | Qué podemos aprender |

Después de la tabla, agrega:

Principales diferencias entre esas soluciones y nuestro proyecto.
Tres oportunidades de diferenciación técnica para nuestro MVP.
Tres riesgos que debemos considerar al comparar nuestro proyecto con estas soluciones.
RESTRICCIONES:

Prioriza soluciones reales y verificables.
No inventes nombres, funcionalidades, tecnologías ni datos.
Si tienes acceso a búsqueda web, utiliza fuentes verificables y proporciona los enlaces o referencias utilizadas.
Si no puedes verificar un dato, indícalo como "No verificado".
No incluyas análisis de marketing, precios, ventas o rentabilidad.
Enfócate exclusivamente en aspectos funcionales y técnicos relacionados con nuestro proyecto.
No propongas funcionalidades fuera del alcance del MVP.
Diferencia claramente entre información verificada y conclusiones propias.
EJEMPLO DEL NIVEL ESPERADO:

Competidor/Solución	Qué hace	Relación con nuestro proyecto
Ejemplo verificable	Describe brevemente su función	Explica qué relación tiene con el análisis de comportamiento
No utilices este ejemplo como un competidor real; solo úsalo para entender el formato y nivel de detalle esperado.

Evaluación del Prompt 1

Resumen de la evaluación
El prompt está bien construido, con rol, contexto y tarea claros, y con restricciones explícitas sobre verificación y alcance. La respuesta de la IA identificó tres competidores reales y verificables (Google Analytics 4 – Métricas Predictivas, el dataset UCI Online Shoppers Purchasing Intention y Nosto), respetó el formato de tabla solicitado y se mantuvo dentro del alcance del MVP. Sin embargo, incumplió una restricción explícita del prompt (no incluyó enlaces ni referencias verificables) y presentó dos cifras específicas sobre Nosto que no logré confirmar con fuentes actuales — una de ellas contradice la información disponible hoy — sin marcarlas como "No verificado", lo que constituye un fallo de control de alucinaciones.

Evaluación de los 6 componentes Componente Puntuación Evaluación Role 1/1 Rol específico y coherente con la tarea ("analista de negocios y de productos digitales senior, especializado en apps web y e-commerce"). No requiere ajustes. Context 1/1 Contexto completo: equipo, tiempo disponible, objetivo del proyecto, MVP y alcance fuera del MVP. Permite a la IA entender qué tipo de competidores son relevantes. Task 1/1 La tarea es concreta y acotada: análisis competitivo de exactamente 3 soluciones relacionadas con comportamiento de usuario/intención de compra. Format 1/1 Especifica columnas exactas de la tabla y tres secciones posteriores obligatorias. La respuesta siguió esta estructura de forma literal. Constraints 0.5/1 Las restricciones son numerosas y relevantes (verificabilidad, no inventar datos, marcar "No verificado", excluir marketing/precios), pero no exige explícitamente citar la fuente de cada dato ni indicar la fecha de consulta de cifras dinámicas (ej. número de clientes de una empresa), lo cual habría evitado el problema principal detectado en la respuesta. Examples 0.5/1 El ejemplo aclara el nivel de detalle esperado, pero solo muestra 3 de las 7 columnas solicitadas, dejando parcialmente indefinido cómo debían verse columnas como "Fortalezas" o "Qué podemos aprender". TOTAL 5/6 Prompt sólido y bien estructurado; el margen de mejora está en constraints (citación de fuentes) y examples (cobertura completa de columnas).
Evaluación de la respuesta generada Cumplimientos Los tres competidores elegidos son reales y verificables: confirmé mediante búsqueda web que GA4 sí ofrece métricas predictivas de probabilidad de compra/abandono con el umbral de 1.000 usuarios positivos y 1.000 negativos en 28 días exactamente como se describe, que el dataset UCI "Online Shoppers Purchasing Intention" tiene efectivamente 12.330 sesiones, 10 atributos numéricos y 8 categóricos con "Revenue" como etiqueta (autoría de Sakar, Kastro et al.), y que Nosto es una plataforma real de personalización con su producto "experience.AI". Respetó exactamente la estructura de tabla de 7 columnas solicitada. Incluyó las tres secciones adicionales pedidas (diferencias, oportunidades de diferenciación, riesgos), cada una con exactamente el número de elementos pedido (3). Se mantuvo dentro del alcance técnico/funcional: no incluyó precios, marketing ni rentabilidad, cumpliendo esa restricción. Usó correctamente la etiqueta "No verificado" al menos una vez (detalle de la licencia CC BY 4.0 del dataset UCI), mostrando que sí aplicó parcialmente la instrucción de marcar información no confirmable. Problemas encontrados Incumplimiento de una restricción explícita: el prompt exige "si tienes acceso a búsqueda web, utiliza fuentes verificables y proporciona los enlaces o referencias utilizadas". La respuesta no incluye ningún enlace ni bibliografía, en ninguna parte del documento. Cifras no marcadas como "No verificado" que deberían haberlo sido: la fila de Nosto afirma "más de 2.500 minoristas en más de 100 países" y que la plataforma "procesa más de 1.100 millones de recomendaciones diarias", presentadas como hechos sin matiz alguno. Información que requiere verificación La cifra "más de 1.100 millones de recomendaciones diarias" de Nosto: NO VERIFICADO — no encontré ninguna fuente actual que respalde este dato específico. El número "más de 2.500 minoristas" de Nosto: al buscarlo, las fuentes oficiales de Nosto (blog corporativo, LinkedIn, G2, comunicados de 2025-2026) indican consistentemente que Nosto da soporte a más de 1.500 marcas en más de 100 países, no 2.500. Esto es una discrepancia significativa, no solo un dato "no verificado" sino aparentemente incorrecto frente a la evidencia disponible. Nosto launches AI-powered Post-Purchase Upsell for Shopify +3
Posibles alucinaciones

Sí se detectó una probable alucinación o dato desactualizado/inventado: la cifra de "2.500 minoristas" para Nosto contradice directamente lo que reportan múltiples fuentes actuales e independientes (sitio oficial de Nosto, LinkedIn, G2), que coinciden en ~1.500 marcas. La cifra de "1.100 millones de recomendaciones diarias" tampoco pudo confirmarse en ninguna fuente consultada. Ambas cifras se presentaron como hechos verificados, sin la etiqueta "No verificado" que el prompt exigía para este tipo de casos.

¿Qué funcionó? El rol y el contexto fueron suficientemente específicos como para que la IA seleccionara competidores realmente pertinentes (no genéricos): un producto de analítica con ML real (GA4), un dataset académico casi idéntico al problema planteado (UCI) y un SaaS comercial de personalización (Nosto), cubriendo tres ángulos distintos (analítica nativa, dataset académico, producto comercial). La respuesta respetó fielmente la estructura de tabla y las tres secciones adicionales solicitadas, sin omitir ni agregar apartados. Se mantuvo dentro del alcance del MVP: no propuso funcionalidades fuera de alcance (recomendación avanzada, pagos, apps móviles), y de hecho advirtió explícitamente sobre riesgos de comparar el MVP con productos maduros como GA4 o Nosto, lo cual es coherente con el contexto de un proyecto académico de 12 semanas. Usó al menos una vez la etiqueta "No verificado" tal como exigía el prompt, demostrando que la instrucción fue comprendida, aunque no se aplicó de forma consistente en todos los casos que lo requerían.
¿Qué no funcionó? No se proporcionó ningún enlace ni referencia, pese a que el prompt lo exige explícitamente cuando hay acceso a búsqueda web. Se presentaron cifras estadísticas específicas y potencialmente desactualizadas o incorrectas (número de minoristas de Nosto, volumen de recomendaciones diarias) sin la etiqueta "No verificado", lo que es justamente el tipo de error que la restricción del prompt buscaba prevenir. El ejemplo de formato incluido en el prompt original no cubría las 7 columnas, lo que pudo dejar ambigüedad sobre el nivel de detalle esperado en columnas como "Tecnologías o enfoque conocido".
Correcciones realizadas o recomendadas Problema Corrección No se incluyeron enlaces ni referencias pese a exigirlo el prompt. Mover la exigencia de citar fuentes del bloque de RESTRICCIONES al bloque de FORMATO, indicando explícitamente: "Agrega una columna o sección de 'Fuente' con el enlace verificable de cada competidor." Se presentaron cifras concretas (número de clientes, volumen de uso) como hechos sin marcarlas como "No verificado", y al menos una de ellas no coincide con la evidencia disponible. Añadir una restricción explícita: "Toda cifra estadística específica (número de usuarios, clientes, volumen de datos, porcentajes) debe ir acompañada de su fuente y fecha de publicación. Si no puedes confirmar la cifra con una fuente verificable, indícala como 'No verificado' en lugar de presentarla como un hecho." El ejemplo de formato solo mostraba 3 de las 7 columnas solicitadas. Ampliar el ejemplo para incluir las 7 columnas completas, aunque sea con contenido breve, para fijar el nivel de detalle esperado en cada una. No se exige indicar la fecha de la información recuperada por búsqueda web, relevante para datos que cambian con el tiempo (ej. número de clientes de una empresa).
PROMT SUGERIDO O MEJORADO:
Actúa como analista de negocios y analista de productos digitales senior, especializado en aplicaciones web y comercio electrónico.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué. Tenemos 12 semanas efectivas para desarrollar un proyecto académico.

Nuestro proyecto consiste en desarrollar una aplicación web capaz de analizar la intención de compra de los usuarios de una tienda virtual a partir de su comportamiento de navegación (productos visitados, clics, tiempo de navegación, productos agregados al carrito y otras variables disponibles en los datos), clasificando la intención en baja, media o alta.

El MVP contempla: cargar/usar datos de comportamiento, procesarlos, identificar variables relevantes, implementar un modelo de Machine Learning, estimar el nivel de intención de compra por usuario, y mostrar resultados en una interfaz web con tablas y gráficos básicos.

TAREA: Realiza un análisis competitivo de 3 soluciones, aplicaciones, datasets o plataformas existentes y reales relacionadas con análisis de comportamiento de usuarios, analítica de e-commerce o predicción/estimación de intención de compra.

FORMATO: Entrega una tabla Markdown con las columnas: | Competidor/Solución | Qué hace | Relación con nuestro proyecto | Tecnologías o enfoque conocido | Fortalezas | Limitaciones | Qué podemos aprender | Fuente (enlace o referencia) |

Después de la tabla, agrega:

Principales diferencias entre esas soluciones y nuestro proyecto.
Tres oportunidades de diferenciación técnica para nuestro MVP.
Tres riesgos que debemos considerar al comparar nuestro proyecto con estas soluciones.
RESTRICCIONES:

Prioriza soluciones reales y verificables; no inventes nombres, funcionalidades, tecnologías ni cifras.
Toda cifra estadística concreta (usuarios, clientes, volumen de datos, porcentajes, etc.) debe incluir su fuente y, si es relevante, la fecha aproximada del dato. Si no puedes confirmarla con una fuente verificable, escribe "No verificado" en lugar de presentarla como hecho.
Incluye siempre el enlace o referencia usada para cada competidor en la columna "Fuente".
No incluyas análisis de marketing, precios, ventas o rentabilidad.
Enfócate exclusivamente en aspectos funcionales y técnicos relacionados con nuestro proyecto.
No propongas funcionalidades fuera del alcance del MVP.
Diferencia claramente entre información verificada y conclusiones propias.
EJEMPLO DEL NIVEL ESPERADO (no usar como competidor real, solo como referencia de formato):

Competidor/Solución	Qué hace	Relación con nuestro proyecto	Tecnologías o enfoque conocido	Fortalezas	Limitaciones	Qué podemos aprender	Fuente
Ejemplo verificable	Describe brevemente su función	Explica la relación con el análisis de comportamiento	Enfoque técnico conocido	Puntos fuertes reales	Limitaciones reales	Aprendizaje aplicable al MVP	Enlace o referencia consultada
PROMPT 02 — DOCUMENTO DE VISIÓN.

Actúa como analista de sistemas y redactor de documentos de visión de software senior.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué y desarrollaremos un proyecto académico durante 12 semanas efectivas.

IDEA DEL PROYECTO: Desarrollaremos una aplicación web capaz de analizar la intención de compra de los usuarios de una tienda virtual a partir de su comportamiento de navegación.

El sistema procesará datos como productos visitados, cantidad de clics, tiempo de navegación, productos agregados al carrito y otras variables relevantes.

A partir de estos datos se buscarán patrones de comportamiento y se estimará el nivel de intención de compra de un usuario, clasificándolo como baja, media o alta intención de compra.

MVP:

Carga o utilización de un conjunto de datos de navegación.
Procesamiento y preparación de datos.
Identificación de variables relevantes.
Modelo de aprendizaje automático.
Estimación de intención de compra.
Visualización de resultados mediante una aplicación web.
Tablas y gráficos básicos.
TAREA: Genera un documento de visión inicial para nuestro proyecto.

FORMATO: Utiliza Markdown y organiza el documento exactamente en estas secciones:

Documento de Visión
1. Problema
2. Usuarios objetivo
3. Necesidad identificada
4. Propuesta de valor
5. Solución propuesta
6. Alcance del MVP
7. Fuera del alcance
8. Beneficios esperados
9. Supuestos
10. Preguntas abiertas
En "Preguntas abiertas", incluye máximo 5 preguntas cuya respuesta pueda cambiar decisiones importantes del proyecto.

RESTRICCIONES:

No inventes información que no esté en el contexto.
Si necesitas realizar una suposición, márcala explícitamente como [SUPUESTO].
No agregues pagos, recomendaciones personalizadas, aplicaciones móviles, chat, notificaciones ni funcionalidades de IA innecesarias.
No conviertas el documento en un plan de marketing.
No inventes estadísticas sobre usuarios o tiendas virtuales.
Mantén el alcance realista para un equipo de 3 estudiantes y 12 semanas.
El documento debe servir como base para posteriores requisitos de software.
EJEMPLO DEL NIVEL ESPERADO:

1. Problema
Los datos generados durante la navegación de una tienda virtual pueden contener señales relacionadas con el comportamiento de compra, pero esas señales no siempre se analizan de manera estructurada para estimar la intención de compra.

4. Propuesta de valor
[Redactar una propuesta concreta basada únicamente en el contexto proporcionado.]

No copies literalmente los ejemplos; utilízalos únicamente como referencia de estructura y nivel de precisión.
Evaluación del Prompt 2

Resumen de la evaluación
El prompt está muy bien construido: define una estructura exacta de 10 secciones, restricciones claras sobre alcance y honestidad epistémica (uso de [SUPUESTO]), y limita el número de preguntas abiertas. La respuesta de la IA siguió correctamente la estructura, marcó apropiadamente las suposiciones, respetó el alcance del MVP y no inventó estadísticas externas. Sin embargo, comparando ambos documentos se detecta un incumplimiento verificable de una restricción explícita: la sección "1. Problema" reproduce casi literalmente la oración de ejemplo del prompt, pese a la instrucción de no copiar los ejemplos textualmente.

Evaluación de los 6 componentes Componente Puntuación Evaluación Role 1/1 "Analista de sistemas y redactor de documentos de visión de software senior" es un rol específico y directamente aplicable a la tarea. Context 1/1 Incluye equipo, tiempo disponible, idea del proyecto y MVP resumido; suficiente para redactar el documento sin ambigüedad sobre el objetivo del sistema. Task 1/1 "Genera un documento de visión inicial" es una tarea clara, y la instrucción adicional sobre el límite de preguntas en la sección 10 la hace aún más precisa. Format 1/1 Especifica exactamente las 10 secciones y su encabezado Markdown, sin dejar ambigüedad sobre la estructura esperada. Constraints 0.5/1 Son extensas y pertinentes (no inventar información, marcar supuestos, no ampliar alcance, no estadísticas, no marketing), pero la instrucción contra copiar el ejemplo ("no copies literalmente") resultó insuficiente en la práctica: la respuesta la incumplió de forma verificable, lo que sugiere que debería reforzarse (p. ej. "no reproduzcas ninguna oración del ejemplo, ni siquiera parcialmente"). Examples 0.5/1 El ejemplo aclara el nivel de precisión esperado, pero al usar contenido temáticamente casi idéntico al problema real (mismo dominio, misma redacción posible), incrementa el riesgo de copia textual, como efectivamente ocurrió. Un ejemplo de otro dominio habría cumplido la misma función de referencia estructural con menos riesgo. TOTAL 5/6 Prompt muy sólido; el margen de mejora está en constraints (prohibición de copia más explícita) y en el diseño del ejemplo (usar un dominio distinto).
Evaluación de la respuesta generada Cumplimientos Siguió exactamente las 10 secciones solicitadas, en el orden y con los encabezados pedidos. Usó la etiqueta [SUPUESTO] de forma consistente y justificada en los puntos donde el contexto no ofrecía información (usuarios objetivo, origen de los datos, conocimientos del equipo, tipo de evaluación del proyecto, alcance de integración en tiempo real). La sección "10. Preguntas abiertas" contiene exactamente 5 preguntas (el máximo permitido), y todas están relacionadas con decisiones que efectivamente podrían cambiar el rumbo del proyecto (origen de los datos, variables disponibles, existencia de ground truth para entrenamiento supervisado, carga dinámica de datos, nivel de precisión aceptable). No se agregaron funcionalidades fuera del MVP: la sección "7. Fuera del alcance" excluye explícitamente pagos, recomendaciones personalizadas, apps móviles, chat y notificaciones, tal como exigía el prompt. No se inventaron estadísticas sobre usuarios o tiendas virtuales en ninguna sección. El documento mantiene un alcance realista para un equipo de 3 estudiantes en 12 semanas, y lo declara explícitamente como supuesto en la sección 9. Problemas encontrados Incumplimiento verificable de una restricción explícita: la primera oración de la sección "1. Problema" del documento generado ("Los datos generados durante la navegación de una tienda virtual pueden contener señales relacionadas con el comportamiento de compra, pero esas señales no siempre se analizan de manera estructurada para estimar la intención de compra") es prácticamente idéntica, palabra por palabra, al texto de ejemplo incluido en el prompt para la misma sección. El prompt indicaba explícitamente "No copies literalmente los ejemplos; utilízalos únicamente como referencia de estructura y nivel de precisión", instrucción que no se respetó en este punto. No se detectaron otros incumplimientos de formato, alcance o restricciones. Información que requiere verificación
Este documento no contiene afirmaciones externas verificables (no hay cifras, nombres de empresas ni datos de terceros), por lo que no aplica el uso de "No verificado" salvo en el punto de copia textual detectado, que es un hecho comprobable directamente comparando los dos textos, no una incertidumbre externa.

Posibles alucinaciones

No se detectaron posibles alucinaciones con la información disponible. El problema identificado es de reproducción textual de una fuente proporcionada por el propio prompt (el ejemplo), no de invención de datos falsos.

¿Qué funcionó? El uso de [SUPUESTO] fue preciso y se limitó a los puntos donde realmente faltaba información en el contexto (por ejemplo, en "Usuarios objetivo" se señaló correctamente que no hay una definición precisa de quién usará el sistema), lo cual demuestra que la IA distinguió bien entre lo dado y lo inferido. El límite de 5 preguntas abiertas se cumplió exactamente, y las preguntas elegidas tienen relevancia real para el proyecto (ground truth para entrenamiento supervisado, origen de los datos), no son preguntas genéricas de relleno. El documento respetó rigurosamente el alcance fuera del MVP definido en el prompt, sin agregar ninguna funcionalidad no solicitada (ni siquiera sugerencias veladas de recomendaciones o pagos). No hay señales de invención de estadísticas o datos de mercado, cumpliendo una restricción que suele ser fuente común de alucinaciones en este tipo de documentos.
¿Qué no funcionó? La sección "Problema" copió casi literalmente la redacción del ejemplo del prompt, en lugar de usarla solo como referencia de estructura y nivel de precisión, tal como se pedía explícitamente. El riesgo de esta copia se vio favorecido por el diseño del propio ejemplo (mismo dominio y fraseo natural para el tema), lo que facilitó que la IA lo reutilizara en vez de generar una redacción propia.
Correcciones realizadas o recomendadas Problema Corrección La respuesta copió casi literalmente la oración de ejemplo en la sección "Problema", pese a la restricción explícita contra esto. Reforzar la restricción con una frase más estricta: "No reproduzcas ninguna oración del ejemplo, ni siquiera parcialmente; redacta cada sección completamente con palabras propias, aunque el contenido temático sea similar." El ejemplo proporcionado usaba el mismo dominio y fraseo del proyecto real, lo que facilitó la copia. Sustituir el ejemplo de la sección "Problema" por uno de un dominio distinto (por ejemplo, un sistema de gestión de inventario en lugar de e-commerce), manteniendo el mismo nivel de precisión pero eliminando el riesgo de copia literal.
PROMT FINAL SUGERIDO: PROMPT 02 — DOCUMENTO DE VISIÓN. Actúa como analista de sistemas y redactor de documentos de visión de software senior.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué y desarrollaremos un proyecto académico durante 12 semanas efectivas.

IDEA DEL PROYECTO: Desarrollaremos una aplicación web capaz de analizar la intención de compra de los usuarios de una tienda virtual a partir de su comportamiento de navegación. El sistema procesará datos como productos visitados, cantidad de clics, tiempo de navegación, productos agregados al carrito y otras variables relevantes. A partir de estos datos se buscarán patrones de comportamiento y se estimará el nivel de intención de compra de un usuario, clasificándolo como baja, media o alta intención de compra.

MVP: - Carga o utilización de un conjunto de datos de navegación. - Procesamiento y preparación de datos. - Identificación de variables relevantes. - Modelo de aprendizaje automático. - Estimación de intención de compra. - Visualización de resultados mediante una aplicación web. - Tablas y gráficos básicos.

TAREA: Genera un documento de visión inicial para nuestro proyecto.

FORMATO: Utiliza Markdown y organiza el documento exactamente en estas secciones:

Documento de Visión
1. Problema ## 2. Usuarios objetivo ## 3. Necesidad identificada ## 4. Propuesta de valor ## 5. Solución propuesta ## 6. Alcance del MVP ## 7. Fuera del alcance ## 8. Beneficios esperados ## 9. Supuestos ## 10. Preguntas abiertas
En "Preguntas abiertas", incluye máximo 5 preguntas cuya respuesta pueda cambiar decisiones importantes del proyecto.

RESTRICCIONES:

No inventes información que no esté en el contexto.
Si necesitas realizar una suposición, márcala explícitamente como [SUPUESTO].
No agregues pagos, recomendaciones personalizadas, aplicaciones móviles, chat, notificaciones ni funcionalidades de IA innecesarias.
No conviertas el documento en un plan de marketing.
No inventes estadísticas sobre usuarios o tiendas virtuales.
Mantén el alcance realista para un equipo de 3 estudiantes y 12 semanas.
El documento debe servir como base para posteriores requisitos de software.
No reproduzcas ninguna oración del ejemplo siguiente, ni siquiera parcialmente; úsalo únicamente como referencia de estructura y nivel de precisión, y redacta cada sección completamente con tus propias palabras.
EJEMPLO DEL NIVEL ESPERADO (de un dominio distinto, solo como referencia de estructura, NO copiar frases):

1. Problema
Un sistema de gestión de inventario en una bodega puede generar registros de entradas y salidas de productos, pero sin un mecanismo de análisis estructurado, esos registros no se traducen en alertas claras sobre quiebres de stock.

4. Propuesta de valor
[Redactar una propuesta concreta basada únicamente en el contexto proporcionado, con redacción original.]

PROMPT 03 — EVALUACIÓN Y MEJORA DEL PROMPT

Actúa como experto en Prompt Engineering para proyectos de software.

CONTEXTO: Estamos desarrollando un proyecto académico de Ingeniería de Sistemas en UNIMINUTO Ibagué.

Nuestro proyecto es una aplicación web que analiza la intención de compra en una tienda virtual a partir del comportamiento de navegación de los usuarios.

El prompt que vas a evaluar será utilizado para obtener resultados relacionados con este proyecto.

TAREA: Evalúa el prompt delimitado entre ### utilizando exactamente los 6 componentes de un prompt profesional:

Rol
Contexto
Tarea
Formato
Restricciones
Ejemplos
CALIFICA cada componente con:

0 = ausente o inútil
1 = presente y útil
FORMATO: Entrega:

Evaluación
Componente	Puntuación (0-1)	¿Está bien definido?	Mejora necesaria
Puntuación total: X/6

Problemas principales
Máximo 5 puntos.

Prompt mejorado
Devuelve el prompt completo, listo para copiar y pegar.

Cambios realizados
Máximo 3 líneas.

RESTRICCIONES:

No ejecutes el prompt original.
No cambies el objetivo de la tarea.
No agregues funcionalidades que no pertenezcan al proyecto.
No hagas el prompt innecesariamente largo.
Mantén el contexto suficiente para que otra IA pueda ejecutarlo correctamente.
Si un componente ya está bien construido, consérvalo.
Prioriza claridad y precisión sobre longitud.
EJEMPLO DE CRITERIO: Un prompt que diga solamente "analiza mi proyecto" tendría una puntuación baja porque no define claramente rol, tarea, formato ni restricciones.

[PEGAR AQUÍ EL PROMPT A EVALUAR]

Evaluación Componente Puntuación (0-1) ¿Está bien definido? Mejora necesaria Rol 1 Sí. Define un rol específico (analista de negocios y de productos digitales senior, en e-commerce), coherente con la tarea de análisis competitivo. Ninguna relevante. Contexto 1 Sí. Explica equipo, plazo, objetivo del proyecto, variables de análisis y alcance del MVP con suficiente detalle para que otra IA entienda el dominio. Podría acotar aún más el foco ("comportamiento de navegación pre-compra") para evitar desviaciones hacia analítica general de e-commerce. Tarea 1 Sí. Pide explícitamente un análisis competitivo de 3 soluciones relacionadas con comportamiento de usuario/intención de compra. Podría aclarar qué tipo de soluciones priorizar (académicas, comerciales, open source) para acotar la búsqueda. Formato 1 Sí. Especifica columnas exactas de la tabla y estructura de las secciones posteriores (diferencias, oportunidades, riesgos). Falta indicar extensión máxima del texto fuera de la tabla, para evitar respuestas demasiado largas. Restricciones 1 Sí. Lista clara de 8 restricciones (verificabilidad, fuentes, alcance funcional, no marketing/precios). Se pueden consolidar restricciones redundantes y añadir un límite de antigüedad de las fuentes (p. ej. últimos 3-5 años). Ejemplos 1 Presente y útil, pero incompleto: solo muestra 3 de las 7 columnas requeridas, lo que puede generar ambigüedad sobre el nivel de detalle esperado en las columnas restantes. Completar el ejemplo con las 7 columnas para que sirva de referencia real de formato.

Puntuación total: 6/6

Problemas principales El ejemplo de formato no cubre todas las columnas de la tabla, dejando ambigüedad sobre el detalle esperado en "Tecnologías", "Fortalezas", "Limitaciones" y "Qué podemos aprender". No se define una extensión máxima para el análisis textual posterior a la tabla, lo que puede producir respuestas innecesariamente largas. No se exige una antigüedad mínima/máxima de las fuentes, lo que podría traer información desactualizada como "verificada". No se especifica el idioma de respuesta de forma explícita (se infiere por el idioma del prompt, pero conviene declararlo). Algunas restricciones son redundantes (varias apuntan a "no inventar datos") y podrían consolidarse para mayor claridad.

PROMPT MEJORADO: Actúa como analista de negocios y analista de productos digitales senior, especializado en aplicaciones web y comercio electrónico.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué. Tenemos 12 semanas efectivas para desarrollar un proyecto académico.

Nuestro proyecto consiste en desarrollar una aplicación web capaz de analizar la intención de compra de los usuarios de una tienda virtual a partir de su comportamiento de navegación (productos visitados, clics, tiempo de navegación, productos agregados al carrito, entre otras variables disponibles). El objetivo es identificar patrones y estimar si un usuario presenta una intención de compra baja, media o alta.

El MVP contempla:

Cargar o utilizar datos de comportamiento de navegación.
Procesar y preparar los datos.
Identificar variables relevantes.
Utilizar un modelo de aprendizaje automático.
Estimar el nivel de intención de compra.
Mostrar los resultados en una interfaz web mediante tablas y gráficos.
TAREA: Realiza un análisis competitivo de 3 soluciones, aplicaciones, plataformas o proyectos reales y verificables (académicos, open source o comerciales) que tengan relación directa con el análisis del comportamiento de usuarios, analítica de comercio electrónico, o predicción/estimación de intención de compra mediante datos.

FORMATO: Responde en español. Entrega una tabla Markdown con las siguientes columnas:

| Competidor/Solución | Qué hace | Relación con nuestro proyecto | Tecnologías o enfoque conocido | Fortalezas | Limitaciones | Qué podemos aprender |

Después de la tabla, agrega (máximo 400 palabras en total):

Principales diferencias entre esas soluciones y nuestro proyecto.
Tres oportunidades de diferenciación técnica para nuestro MVP.
Tres riesgos que debemos considerar al comparar nuestro proyecto con estas soluciones.
RESTRICCIONES:

Usa únicamente soluciones reales y verificables; no inventes nombres, funcionalidades, tecnologías ni datos.
Prioriza fuentes de los últimos 3-5 años; si usas fuentes más antiguas, indícalo.
Si tienes acceso a búsqueda web, cita fuentes o enlaces verificables. Si no puedes verificar un dato, márcalo como "No verificado".
Enfócate exclusivamente en aspectos funcionales y técnicos relacionados con comportamiento de navegación e intención de compra; no incluyas marketing, precios ni rentabilidad.
No propongas funcionalidades fuera del alcance del MVP descrito.
Diferencia claramente entre información verificada y conclusiones propias.
EJEMPLO DEL NIVEL ESPERADO (no usar como competidor real, solo como referencia de formato y nivel de detalle):

Competidor/Solución	Qué hace	Relación con nuestro proyecto	Tecnologías o enfoque conocido	Fortalezas	Limitaciones	Qué podemos aprender
Ejemplo verificable	Describe brevemente su función principal	Explica qué relación tiene con el análisis de comportamiento e intención de compra	Menciona el enfoque técnico o herramientas conocidas (ej. modelo, arquitectura)	Señala 1-2 puntos fuertes relevantes	Señala 1-2 limitaciones relevantes	Indica una lección aplicable a nuestro MVP
Cambios realizados						
Se completó el ejemplo con las 7 columnas, se añadió límite de extensión (400 palabras) y antigüedad de fuentes (3-5 años), y se declaró explícitamente el idioma de respuesta. El resto del prompt se conservó por estar ya bien construido.
PROMPT 04 — REFINAMIENTO DEL DOCUMENTO DE VISIÓN

Problemas encontrados No se confirma el origen ni la estructura del dataset. El documento no aclara si existe un conjunto de datos real, público o simulado, ni qué variables contiene realmente. Esto es crítico porque todo el flujo (procesamiento, selección de variables, modelo) depende de esta decisión. No hay etiquetado confirmado de intención de compra. Para clasificar en baja/media/alta con un modelo de aprendizaje automático supervisado se necesitan etiquetas de referencia. El documento no confirma si existen; sin ellas, el enfoque tendría que ser no supervisado (clustering) o basado en reglas, lo cual cambia el proyecto. Usuarios objetivo ambiguos y potencialmente contradictorios. Se mezclan "encargados de operación de tienda" con "docentes/jurados evaluadores" sin definir cuál orienta las decisiones de diseño y alcance. No hay criterio de éxito/desempeño definido. No se establece qué exactitud o métrica se considerará aceptable, quedando solo como pregunta abierta al final, cuando debería condicionar decisiones tempranas. El tipo de modelo de aprendizaje automático no está especificado. No se indica si será supervisado, no supervisado, ni qué algoritmo se contempla, lo que dificulta estimar el esfuerzo real en 12 semanas. No se menciona la distribución de trabajo entre los 3 integrantes ni el volumen de datos esperado. Esto es relevante para validar la viabilidad temporal del MVP. Las preguntas abiertas incluyen decisiones bloqueantes (existencia de etiquetas, origen del dataset) que deberían resolverse antes de iniciar el desarrollo, no quedar solo como preguntas al cierre del documento.

Supuestos detectados [SUPUESTO] Los usuarios objetivo son personas encargadas de operación/análisis de tienda virtual. [SUPUESTO] Los usuarios objetivo también incluyen docentes o jurados evaluadores del proyecto académico. [SUPUESTO] El sistema trabajará sobre un dataset ya existente o simulado, no sobre tráfico en vivo. [SUPUESTO] El dataset de navegación ya está disponible (por ejemplo, un dataset público). [SUPUESTO] El equipo posee las bases necesarias en desarrollo web y aprendizaje automático para completar el MVP en 12 semanas. [SUPUESTO] La prioridad del proyecto es el análisis y la visualización de resultados, más que un diseño visual elaborado. [SUPUESTO] La evaluación se realizará en un contexto académico, no como sistema desplegado con usuarios reales. [SUPUESTO] Existe (o se puede construir) un criterio de etiquetado de intención de compra que permita entrenar o validar el modelo. [SUPUESTO] El modelo de aprendizaje automático será de tipo supervisado (no se ha confirmado si se usará clustering u otro enfoque no supervisado).

Decisiones que debemos tomar Confirmar la fuente del dataset: público existente, simulado, o construido por el equipo. Definir si el modelo será supervisado (requiere etiquetas de intención de compra) o no supervisado (clustering), según la disponibilidad real de etiquetas. Establecer una métrica mínima de desempeño aceptable para el modelo, ajustada al tiempo disponible (12 semanas). Priorizar el usuario objetivo real del sistema (operador de tienda vs. evaluador académico) para orientar decisiones de alcance y presentación de resultados. Definir si la aplicación trabajará sobre un dataset fijo durante todo el proyecto o si debe permitir cargar nuevos datasets.

Documento de visión corregido

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

Cambios realizados Se añadió una sección de "Contexto del equipo" para dejar explícito que el proyecto es desarrollado por 3 estudiantes de UNIMINUTO Ibagué en 12 semanas, dato relevante para evaluar viabilidad. Se marcó explícitamente como [SUPUESTO] el enfoque de modelado (supervisado vs. no supervisado), dado que no hay etiquetado de intención de compra confirmado. Se agregó una nota en la sección de usuarios objetivo señalando la necesidad de priorizar una audiencia, en lugar de dejarlo implícito. Se añadió el supuesto sobre la existencia (o construcción) de un criterio de etiquetado, antes ausente pero necesario para el modelo. No se agregaron ni eliminaron funcionalidades del alcance; solo se reforzó la trazabilidad de los supuestos y se mantuvo intacta la estructura original del documento.
PROMPT 05 — DETECCIÓN DE VACÍOS Y RIESGOS DEL PROYECTO

Actúa como arquitecto de software y analista de riesgos técnicos senior.

CONTEXTO: Somos un equipo de 3 estudiantes de Ingeniería de Sistemas de UNIMINUTO Ibagué.

Tenemos 12 semanas efectivas para desarrollar una aplicación web que analice la intención de compra en una tienda virtual a partir del comportamiento de navegación.

El sistema utilizará datos como productos visitados, clics, tiempo de navegación, productos agregados al carrito y otras variables disponibles.

El MVP contempla:

Cargar o utilizar datos de navegación.
Procesar los datos.
Identificar variables relevantes.
Entrenar y evaluar un modelo de aprendizaje automático.
Estimar intención de compra baja, media o alta.
Mostrar resultados mediante una interfaz web.
DOCUMENTO ACTUAL:

[PEGAR AQUÍ EL DOCUMENTO DE VISIÓN O ANÁLISIS COMPETITIVO]

TAREA: Identifica los vacíos de información, supuestos y riesgos técnicos que podrían impedir que el MVP sea desarrollado correctamente.

FORMATO: Entrega una tabla Markdown:

| ID | Riesgo o vacío | Por qué importa | Impacto | Cómo verificarlo | Acción recomendada |

Utiliza únicamente estas categorías de impacto:

Alto
Medio
Bajo
Después de la tabla incluye:

1. Información crítica que todavía necesitamos
Máximo 5 puntos.

2. Riesgos que debemos resolver primero
Máximo 5 puntos.

3. Preguntas para el equipo
Máximo 5 preguntas.

RESTRICCIONES:

Enfócate únicamente en alcance, datos y riesgos técnicos.
No incluyas marketing ni finanzas.
No inventes información sobre nuestro dataset.
Si no existe información suficiente para determinar algo, indícalo como "No confirmado".
No propongas soluciones técnicamente innecesariamente complejas.
No desarrolles código.
No asumas que un modelo de Machine Learning funcionará correctamente hasta disponer de datos adecuados.
EJEMPLO: Si desconocemos si el dataset contiene suficientes registros de usuarios que compraron, no afirmes que existe un problema de desbalance; registra que el nivel de desbalance es "No confirmado" y explica cómo verificarlo.

Análisis de vacíos, supuestos y riesgos técnicos — MVP Predicción de Intención de Compra
ID	Riesgo o vacío	Por qué importa	Impacto	Cómo verificarlo	Acción recomendada
R1	Origen del dataset no confirmado (propio, público o simulado)	Define la arquitectura de ingesta, las variables reales disponibles y todo el pipeline posterior	Alto	Confirmar con la fuente/asesor si habrá acceso a datos de una tienda real, o si se usará un dataset público (ej. UCI)	Definir esta decisión en la semana 1, antes de diseñar cualquier componente
R2	No existe etiquetado de intención de compra en 3 niveles (baja/media/alta) en ninguna fuente confirmada	Sin ground truth de 3 clases no hay forma objetiva de entrenar ni validar un modelo supervisado	Alto	Revisar si el dataset elegido trae alguna etiqueta multinivel; si no, definir si se construirá manualmente o con reglas heurísticas	Documentar y justificar el criterio de discretización (umbrales) antes de modelar, no durante
R3	Enfoque de modelado no definido (supervisado vs. no supervisado/agrupamiento)	Ambos enfoques requieren arquitecturas, tiempos de desarrollo y validaciones distintas	Alto	Depende de la resolución de R2	Decidir el enfoque en semana 1-2, condicionado a la disponibilidad de etiquetas
R4	Variables realmente disponibles y su granularidad — "No confirmado"	El diseño de features y el flujo de preparación de datos dependen directamente de esto	Alto	Hacer un análisis exploratorio (EDA) apenas se tenga el dataset definitivo	Reservar una fase explícita de EDA antes de comprometerse con variables específicas
R5	Volumen y balance de clases del dataset a utilizar — "No confirmado"	Un modelo de 3 clases con pocos datos o fuerte desbalance puede no generalizar, sin que esto sea evidente de inmediato	Alto	Verificar mediante EDA cuando se tenga el dataset; no asumir que el modelo funcionará sin esta validación	Planificar tiempo para manejo de desbalance (si aplica) solo después de confirmarlo, no de forma preventiva
R6	Si se usa el dataset UCI como respaldo, no incluye variable explícita de "producto agregado al carrito"	Esa variable aparece como central en la propuesta de valor y el problema planteado	Medio	Revisar el diccionario de columnas del dataset finalmente elegido	Si se usa UCI, documentar la limitación en el alcance y ajustar la propuesta de valor en consecuencia
R7	No hay criterio de desempeño mínimo aceptable para el modelo	Sin un umbral de éxito no se puede determinar cuándo el MVP "funciona" ni cuándo detener la iteración	Medio	Consultar con el asesor/jurado qué criterio de evaluación aplicarán	Definir métrica (ej. F1 macro, dado el riesgo de desbalance) y umbral objetivo antes de entrenar
R8	Audiencia principal ambigua (operadores/analistas de tienda vs. jurado académico)	Afecta qué se prioriza mostrar en la interfaz y el nivel de detalle técnico expuesto	Medio	Definir con el equipo/asesor cuál audiencia es prioritaria para el diseño de UI	Documentar la decisión antes de iniciar el diseño de la interfaz
R9	Stack tecnológico (frontend, backend, framework de ML) no especificado	Condiciona directamente si el cronograma de 12 semanas es realista	Medio	Evaluar el stack contra las habilidades reales del equipo	Fijar el stack en la semana 1, priorizando herramientas ya conocidas por el equipo
R10	Las habilidades del equipo en ML y desarrollo web para completar el MVP en 12 semanas son un supuesto no validado	Si el supuesto es falso, compromete todo el cronograma, no solo una tarea	Alto	Autoevaluación honesta del equipo + una prueba de concepto reducida	Ejecutar un piloto mínimo (carga de datos → modelo simple → visualización básica) en semana 1-2 para validar viabilidad real
R11	No hay protocolo de evaluación definido para un modelo de 3 clases (métricas, validación, manejo de desbalance)	Sin protocolo, no se puede afirmar con rigor que el modelo "funciona" frente al jurado	Medio	Definir el protocolo de evaluación como parte del diseño técnico, antes de entrenar	Documentar métricas, técnica de validación (ej. hold-out o k-fold) y cómo se reportarán resultados
R12	Trazabilidad/reproducibilidad del pipeline (datos → features → modelo → visualización) no está definida	Riesgo de no poder reproducir resultados ante el jurado o al retomar el proyecto	Bajo	Revisar si existe control de versiones de datos y código	Usar control de versiones y documentar cada etapa del pipeline desde el inicio
R13	No confirmado si se trabajará sobre datos reales de una tienda o completamente simulados	Afecta la validez y el alcance de las conclusiones que se puedan presentar	Alto	Confirmar con la fuente del proyecto/asesor lo antes posible	Tratarlo como bloqueante: resolverlo antes de avanzar en cualquier otro componente del pipeline
1. Información crítica que todavía necesitamos
Origen real y disponibilidad del dataset (propio de una tienda, público o simulado).
Existencia (o no) de un etiquetado previo de intención de compra en 3 niveles.
Variables exactas disponibles en los datos y su granularidad real.
Volumen de registros y balance de clases del dataset que finalmente se use.
Criterio de desempeño mínimo que el jurado/asesor considerará aceptable.
2. Riesgos que debemos resolver primero
Falta de ground truth para una clasificación de 3 niveles (bloquea el enfoque de modelado).
Decisión pendiente entre modelado supervisado y no supervisado.
Dataset no confirmado — bloquea el diseño de todo el pipeline de datos.
Habilidades del equipo en ML/desarrollo web frente al cronograma de 12 semanas, aún sin validar con un piloto.
Audiencia principal de la interfaz sin definir, lo que retrasa decisiones de diseño.
3. Preguntas para el equipo
¿Tenemos ya acceso a un dataset real de una tienda, o vamos a trabajar con uno público (ej. UCI) o simulado?
¿Existe algún criterio o etiquetado previo de intención de compra, o tendremos que definirlo nosotros mismos y justificarlo?
¿Qué variables tendremos garantizadas en los datos, y con qué nivel de detalle (tiempo exacto, número de clics, etc.)?
¿Qué métrica y qué umbral usaremos para decir que el modelo es "suficientemente bueno" dado el tiempo disponible?
¿A quién priorizamos como usuario principal del sistema: el analista/operador de la tienda o el jurado académico?