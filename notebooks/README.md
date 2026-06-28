# Notebooks

Cada peldaño del proyecto vive en un notebook Jupyter independiente. La nomenclatura es `peldano_NN_descripcion.ipynb`.

## Estructura de un notebook (plantilla)

1. **Motivación** — qué problema se aborda y por qué.
2. **Marco matemático** — derivación o repaso de los conceptos clave.
3. **Implementación** — código limpio, importando funciones reutilizables desde `src/`.
4. **Resultados y gráficos** — números, visualizaciones, comparativas.
5. **Validación** — comparación con baseline analítico, análisis de convergencia, errores estándar.
6. **Cierre honesto** — qué funciona, qué no, limitaciones, qué viene después.

## Índice

| Peldaño | Notebook | Tema |
|---------|----------|------|
| 1 | `peldano_01_montecarlo_puro.ipynb` | Estimación de π, paseo aleatorio, TCL |
| 2 | `peldano_02_gbm.ipynb` | Movimiento Browniano Geométrico |
| 3 | `peldano_03_opciones_bs.ipynb` | Opciones europeas: MC vs Black-Scholes |
| 4 | `peldano_04_var.ipynb` | Valor en Riesgo por Monte Carlo |
| 5 | `peldano_05_ampliacion.ipynb` | Reducción de varianza, Griegas |
