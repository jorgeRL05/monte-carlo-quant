"""mcquant — Métodos de Monte Carlo en finanzas cuantitativas.

Paquete con el código reutilizable del proyecto: simulación del GBM, calibración
de parámetros y valoración de opciones europeas. Los notebooks de ``notebooks/``
derivan y explican cada pieza; aquí vive la implementación canónica, cubierta por
la suite de tests de ``tests/``.
"""

from __future__ import annotations

from .estimation import errores_estandar, estimar_parametros
from .gbm import (
    media_teorica,
    simular_gbm,
    simular_precio_final,
    varianza_teorica,
)
from .payoffs import payoff_call, payoff_put
from .pricing import black_scholes, precio_mc

__version__ = "0.3.0"

__all__ = [
    "black_scholes",
    "errores_estandar",
    "estimar_parametros",
    "media_teorica",
    "payoff_call",
    "payoff_put",
    "precio_mc",
    "simular_gbm",
    "simular_precio_final",
    "varianza_teorica",
]
