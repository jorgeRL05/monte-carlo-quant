# Proyecto: Métodos de Monte Carlo para Finanzas Cuantitativas

> Documento de contexto para arrancar el proyecto en Claude Code.
> Pégalo al inicio de una conversación nueva de Claude Code.

---

## 1. Quién soy (contexto del estudiante)

- Estudiante de **doble grado en Ingeniería Informática y Matemáticas** en la URJC (Madrid).
- Acabo de terminar **3º** (verano de 2026); el curso que viene empiezo 4º.
- **Base matemática fuerte**, sobre todo en probabilidad y estadística: variables aleatorias, distribuciones (normal, Poisson, exponencial), Teorema Central del Límite, Bayes, funciones de distribución. Vengo de un curso intenso de probabilidad y estadística.
- **Programación**: Python, Java, C, Scala, JavaScript. Sé C (buena base para C++ más adelante).
- **Objetivo a medio plazo**: introducirme en el mundo **quant / machine learning / datos** en unos años. Este proyecto es para tener algo serio y presentable en CV/LinkedIn.

## 2. Cómo quiero trabajar (instrucciones para el asistente)

- **Háblame en español.**
- **Enséñame mientras construimos**: explícame cada concepto con intuición *antes o mientras* escribimos el código. No quiero copiar código que no entiendo.
- **Nada de jerga sin explicar**: cuando aparezca un término de finanzas o mates nuevo, dame una explicación de una línea en lenguaje llano. Soy nuevo en finanzas (las mates las llevo bien).
- **Prioriza el rigor** por encima de lo vistoso: es lo que de verdad impresiona en quant. Eso significa: evaluar fuera de muestra, no "mirar el futuro" (lookahead bias), comparar con un baseline honesto, y ser sincero con los resultados (si algo no funciona, decirlo).
- **Construye por peldaños**: cada peldaño es un hito que funciona y se puede enseñar por sí solo. No saltes pasos.
- **Git desde el día uno**: un commit por hito.
- **No sobre-ingenierizar** al principio: prioriza que yo entienda, no la elegancia.
- Cuando termine un peldaño, hazme un mini-resumen de qué aprendí y qué viene después.

## 3. Stack y configuración

- **Python 3** con entorno virtual (venv).
- Librerías: `numpy`, `pandas`, `scipy`, `statsmodels`, `matplotlib`, `jupyter`. (`scikit-learn` más adelante si hace falta.)
- **Git + GitHub** desde el inicio (el repo es donde voy a "presumir" el proyecto).
- **Jupyter notebooks** para la parte de investigación/experimentos (mezclar código, gráficos y notas).
- Para datos de mercado (peldaños avanzados): librería gratuita tipo `yfinance`.

## 4. El proyecto y su plan por peldaños

**Idea central:** "Monte Carlo" = resolver problemas **simulando el azar muchísimas veces** y mirando el promedio. Es uno de los cimientos del quant. El proyecto sube de dificultad poco a poco, empezando por probabilidad pura que ya domino y terminando en finanzas.

### Peldaño 0 — Setup
Instalar Python, crear el entorno virtual, inicializar el repositorio Git, instalar librerías, dejar un esqueleto de README. Objetivo: entorno funcionando y primer commit.

### Peldaño 1 — Monte Carlo puro (probabilidad, sin finanzas todavía)
- Estimar el número π tirando puntos al azar en un cuadrado.
- Simular un paseo aleatorio (random walk).
- **Ver** el Teorema Central del Límite en acción con simulaciones.
- Objetivo: afianzar la idea "simular el azar muchas veces → promediar".

### Peldaño 2 — Simular el precio de un activo
- Modelo de movimiento browniano geométrico (en intuición: un paseo aleatorio con tendencia + ruido).
- Entender rentabilidades logarítmicas y los parámetros del modelo (deriva `mu`, volatilidad `sigma`).
- Simular y dibujar muchas trayectorias de precio.
- Objetivo: pasar de probabilidad pura a probabilidad aplicada a un precio.

### Peldaño 3 — Valorar una opción con Monte Carlo
- Qué es una opción (contrato financiero) y una opción europea call/put en lenguaje llano.
- Valorarla por Monte Carlo: simular muchas trayectorias, calcular el pago (payoff), descontarlo y promediar.
- Comparar el resultado con la fórmula cerrada de **Black-Scholes** y ver que convergen.
- Objetivo: que Black-Scholes deje de ser "una fórmula mágica" y sea algo que yo mismo he simulado.

### Peldaño 4 — Una métrica de riesgo
- Calcular el Valor en Riesgo (VaR) por Monte Carlo: cuánto podría perder en un mal día.
- Objetivo: aplicar lo mismo a un problema de riesgo real.

### Peldaño 5 (ampliación, opcional)
- Técnicas de reducción de varianza (variables antitéticas, de control).
- Las "Griegas" por Monte Carlo, análisis de convergencia.
- Redacción final: README detallado + post de LinkedIn explicando la metodología.

## 5. Cómo se ve "terminado" y presentable

- Repo de GitHub limpio con **README que explique la metodología y la intuición**, no solo el código.
- Notebooks con explicaciones y gráficos.
- Un texto breve (post de LinkedIn / sección del README) contando qué aprendí y por qué el método es riguroso.
- Cada peldaño se puede enseñar por separado aunque no termine toda la escalera.

## 6. Glosario en lenguaje llano (para no perderme)

- **Monte Carlo**: resolver algo simulando el azar muchas veces y promediando.
- **Random walk / paseo aleatorio**: una trayectoria que en cada paso se mueve al azar.
- **Movimiento browniano geométrico (GBM)**: el modelo estándar para simular cómo evoluciona un precio (paseo aleatorio con tendencia y ruido).
- **Opción (call/put)**: contrato que da derecho a comprar/vender un activo a un precio fijado.
- **Payoff**: lo que cobras al final según cómo haya ido el precio.
- **Descontar**: traer dinero del futuro a valor de hoy.
- **Black-Scholes**: fórmula clásica para ponerle precio a una opción.
- **Volatilidad**: cuánto se mueve un precio (su "nerviosismo").
- **VaR (Valor en Riesgo)**: cuánto podrías perder en un escenario malo, con cierta probabilidad.
- **Out-of-sample / fuera de muestra**: evaluar con datos que el modelo no ha visto.
- **Lookahead bias**: error de usar información del futuro que no tendrías en ese momento. Hay que evitarlo.

## 7. Contexto extra (no urgente)

- Herramientas que importan en quant, por prioridad: **Python** (núcleo), **SQL** (básico), **C++** (más adelante; ya sé C), **Git** y **Jupyter**. MATLAB y R quedan en segundo plano.
- Tengo aparte una hoja de seguimiento de prácticas/empresas (Arfima, BSC, KPMG Data Scientist, etc.) para el verano de 2027.

---

**Primer mensaje sugerido para Claude Code:**
"Hola, quiero empezar este proyecto. Vamos con el Peldaño 0 (setup): guíame paso a paso para dejar Python, el entorno virtual, Git y las librerías listos, explicándome qué hace cada cosa."
