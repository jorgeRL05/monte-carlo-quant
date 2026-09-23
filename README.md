# Métodos de Monte Carlo en Finanzas Cuantitativas

[![CI](https://github.com/jorgeRL05/monte-carlo-quant/actions/workflows/ci.yml/badge.svg)](https://github.com/jorgeRL05/monte-carlo-quant/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/)
[![Ruff](https://img.shields.io/badge/lint-ruff-orange)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/types-mypy-blue)](https://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Proyecto en Python que implementa, **derivando la matemática paso a paso**, métodos de Monte Carlo aplicados a finanzas cuantitativas: simulación de precios de activos, valoración de opciones por simulación frente a la fórmula cerrada de Black-Scholes, y medidas de riesgo (VaR).

> Doble naturaleza: los **notebooks** son piezas didácticas (motivación → derivación → código → validación → análisis honesto); el **paquete `mcquant`** contiene la implementación reutilizable, con *type hints*, tests y CI.

---

## Motivación

Monte Carlo es uno de los pilares numéricos del *quant*: resolver problemas complejos **simulando el azar muchas veces y promediando**. El proyecto parte de probabilidad pura (estimar π por simulación) y llega a valorar derivados, manteniendo en cada paso el rigor que se espera en la práctica: errores estándar e intervalos de confianza, validación fuera de muestra, comparación contra *baselines* analíticos, y honestidad con las limitaciones de cada modelo.

---

## Resultados destacados

- **Convergencia $1/\sqrt{N}$** del estimador de Monte Carlo, medida empíricamente (π y precios de opciones).
- **GBM calibrado sobre SPY** (2015–2023): σ̂ ≈ 18 %. Se demuestra que el *drift* es prácticamente inestimable — `SE(μ̂) ∝ 1/√T` no mejora muestreando más a menudo —, lo que motiva la valoración neutral al riesgo.
- **Monte Carlo reproduce Black-Scholes**: call ATM = **10.4506**, con el precio exacto dentro del intervalo de confianza del 95 % en todos los escenarios (call/put × ITM/ATM/OTM).
- **Diagnóstico de normalidad** de rentabilidades reales: colas gruesas (curtosis en exceso ≈ 13.5) y rechazo de Jarque-Bera, delimitando dónde falla el GBM.

---

## Estructura del proyecto

```
monte-carlo-quant/
├── src/mcquant/          # Paquete instalable: código reutilizable y testeado
│   ├── gbm.py            #   Simulación del GBM y momentos teóricos
│   ├── estimation.py     #   Calibración MLE de μ y σ + errores estándar
│   ├── payoffs.py        #   Pagos de opciones (interfaz desacoplada del motor)
│   └── pricing.py        #   Motor Monte Carlo + fórmula de Black-Scholes
├── notebooks/            # Notebooks didácticos, uno por módulo
├── tests/                # Suite pytest (validación numérica y estadística)
├── data/                 # Datos de mercado cacheados (reproducibilidad offline)
├── .github/workflows/    # Integración continua (ruff + mypy + pytest)
├── pyproject.toml        # Empaquetado y configuración de herramientas
└── LICENSE
```

---

## Instalación

Requisitos: **Python ≥ 3.11** y **Git**.

```bash
git clone https://github.com/jorgeRL05/monte-carlo-quant.git
cd monte-carlo-quant

python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\Activate.ps1

pip install -e ".[dev,notebooks]"   # paquete + herramientas + jupyter
```

---

## Uso

El paquete se importa como `mcquant`:

```python
import numpy as np
from mcquant import black_scholes, precio_mc, estimar_parametros

rng = np.random.default_rng(42)

# Precio Monte Carlo de una call europea, con su error estándar
precio, se = precio_mc(S0=100, K=100, r=0.05, sigma=0.20, T=1.0, N=1_000_000, rng=rng)
print(f"MC: {precio:.4f} ± {1.96 * se:.4f}")

# Contraste con la fórmula cerrada
print(f"Black-Scholes: {black_scholes(100, 100, 0.05, 0.20, 1.0):.4f}")
```

Ejecutar la suite de tests y las comprobaciones de calidad:

```bash
pytest                 # tests + convergencia numérica
ruff check .           # linting
mypy src/mcquant       # type checking
```

---

## Hoja de ruta

| Módulo | Tema | Estado |
|--------|------|--------|
| 0 | Setup del entorno (venv, Git, dependencias) | ✅ |
| 1 | Monte Carlo puro: π, paseo aleatorio, Teorema Central del Límite | ✅ |
| 2 | Simulación de precios con Movimiento Browniano Geométrico | ✅ |
| 3 | Valoración de opciones europeas (MC vs Black-Scholes) | ✅ |
| 4 | Métrica de riesgo: Valor en Riesgo (VaR) por Monte Carlo | ⬜ |
| 5 | Ampliación: reducción de varianza, Griegas, redacción final | ⬜ |

---

## Stack

`Python ≥ 3.11` · `numpy` · `scipy` · `pandas` · `matplotlib` · `yfinance` · `jupyter`
Calidad: `pytest` · `ruff` · `mypy` · GitHub Actions

---

## Autor

Jorge Rodríguez Lázaro — doble grado Ingeniería Informática + Matemáticas, URJC.
