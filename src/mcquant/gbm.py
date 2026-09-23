"""Movimiento Browniano Geométrico: simulación y momentos teóricos.

Modelo del Módulo 2. El GBM describe el precio de un activo como

    S_T = S_0 · e^{(mu - sigma²/2) T + sigma W_T},   W_T ~ N(0, T)

Se ofrecen dos simuladores: uno de trayectorias completas (para visualización o
pagos dependientes de la trayectoria) y uno del precio final (más rápido, para
pagos europeos que solo dependen de S_T).
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

Array = npt.NDArray[np.float64]


def simular_gbm(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    n_pasos: int,
    n_tray: int,
    rng: np.random.Generator,
) -> Array:
    """Simula trayectorias de GBM con el esquema exacto (sin error de discretización).

    Devuelve una matriz ``(n_tray, n_pasos + 1)``; la columna ``k`` contiene el
    precio en el instante ``t_k = k · T / n_pasos``, y la columna 0 es ``S0``.
    """
    dt = T / n_pasos
    log_rent = rng.normal(
        (mu - 0.5 * sigma**2) * dt, sigma * np.sqrt(dt), size=(n_tray, n_pasos)
    )
    log_S = np.log(S0) + np.cumsum(log_rent, axis=1)
    return np.hstack([np.full((n_tray, 1), S0), np.exp(log_S)])


def simular_precio_final(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    n: int,
    rng: np.random.Generator,
) -> Array:
    """Muestrea ``n`` valores de ``S_T`` directamente de la lognormal.

    Equivale a la última columna de :func:`simular_gbm`, pero sin construir la
    trayectoria intermedia. Es el muestreo adecuado para pagos europeos.
    """
    Z = rng.standard_normal(n)
    S_T: Array = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    return S_T


def media_teorica(S0: float, mu: float, T: float) -> float:
    """Media teórica del GBM: ``E[S_T] = S_0 e^{mu T}``."""
    return float(S0 * np.exp(mu * T))


def varianza_teorica(S0: float, mu: float, sigma: float, T: float) -> float:
    """Varianza teórica del GBM: ``S_0² e^{2 mu T} (e^{sigma² T} - 1)``."""
    return float(S0**2 * np.exp(2 * mu * T) * (np.exp(sigma**2 * T) - 1))
