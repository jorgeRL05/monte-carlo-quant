"""Valoración de opciones europeas: Monte Carlo y Black-Scholes.

Dos caminos independientes al mismo precio (Módulo 3):

- :func:`precio_mc` — simula ``S_T`` bajo la medida neutral al riesgo (drift = r)
  y promedia el pago descontado, devolviendo también el error estándar.
- :func:`black_scholes` — la fórmula cerrada, patrón de oro para validar el MC.
"""

from __future__ import annotations

from typing import Literal

import numpy as np
from scipy.stats import norm

from .gbm import simular_precio_final
from .payoffs import payoff_call, payoff_put

Tipo = Literal["call", "put"]


def precio_mc(
    S0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
    N: int,
    rng: np.random.Generator,
    tipo: Tipo = "call",
) -> tuple[float, float]:
    """Precio Monte Carlo de una opción europea, con su error estándar.

    Muestrea ``S_T`` bajo la medida neutral al riesgo (el drift es la tasa libre
    de riesgo ``r``, no el drift real ``mu``) y promedia el pago descontado.
    Devuelve ``(precio, error_estandar)``, donde ``SE = s / sqrt(N)``.
    """
    S_T = simular_precio_final(S0, r, sigma, T, N, rng)
    payoff = payoff_call(S_T, K) if tipo == "call" else payoff_put(S_T, K)
    descontado = np.exp(-r * T) * payoff
    precio = float(descontado.mean())
    se = float(descontado.std(ddof=1) / np.sqrt(N))
    return precio, se


def black_scholes(
    S0: float, K: float, r: float, sigma: float, T: float, tipo: Tipo = "call"
) -> float:
    """Precio Black-Scholes cerrado de una call o put europea."""
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if tipo == "call":
        return float(S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    return float(K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1))
