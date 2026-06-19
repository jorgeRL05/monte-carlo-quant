# Métodos de Monte Carlo en Finanzas Cuantitativas

Proyecto educativo en Python que implementa, paso a paso, **métodos de Monte Carlo aplicados a problemas reales de finanzas cuantitativas**: simulación de precios de activos, valoración de opciones por simulación frente a fórmula cerrada (Black-Scholes) y cálculo de medidas de riesgo (VaR).

> El proyecto se construye **por peldaños**: cada peldaño es un hito autocontenido que se puede ejecutar y explicar de forma independiente.

---

## Motivación

Monte Carlo es uno de los pilares numéricos del *quant*: resolver problemas complejos **simulando el azar muchas veces y promediando**. En este repo se parte de probabilidad pura (estimar π por simulación) y se llega a aplicaciones financieras con la misma idea de fondo, manteniendo el rigor en cada paso (validación fuera de muestra, comparación con baselines analíticos, honestidad con los resultados).

---

## Estructura del proyecto

```
PROYECTO_QUANT/
├── notebooks/        # Notebooks Jupyter: explicación + experimentos + gráficos
├── src/              # Funciones reutilizables (simuladores, payoffs, etc.)
├── requirements.txt  # Dependencias congeladas con versiones exactas
├── .gitignore
└── README.md
```

---

## Cómo ejecutarlo

Requisitos previos: **Python 3.13** y **Git**.

```powershell
# 1. Clonar el repo
git clone <url-del-repo>
cd PROYECTO_QUANT

# 2. Crear y activar el entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Lanzar Jupyter
jupyter lab
```

En Linux / macOS, sustituir el paso 2 por `source venv/bin/activate`.

---

## Hoja de ruta

| Peldaño | Tema | Estado |
|---------|------|--------|
| 0 | Setup del entorno (venv, Git, dependencias) | ✅ |
| 1 | Monte Carlo puro: π, paseo aleatorio, Teorema Central del Límite | 🔜 |
| 2 | Simulación de precios con Movimiento Browniano Geométrico | ⬜ |
| 3 | Valoración de opciones europeas (MC vs Black-Scholes) | ⬜ |
| 4 | Métrica de riesgo: Valor en Riesgo (VaR) por Monte Carlo | ⬜ |
| 5 | Ampliación: reducción de varianza, Griegas, redacción final | ⬜ |

---

## Stack

`Python 3.13` · `numpy` · `pandas` · `scipy` · `statsmodels` · `matplotlib` · `jupyter` · `yfinance`

---

## Autor

Jorge Rodríguez Lázaro — estudiante del doble grado Ingeniería Informática + Matemáticas, URJC.
