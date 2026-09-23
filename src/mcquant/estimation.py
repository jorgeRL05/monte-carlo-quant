"""Calibración del GBM: estimación de mu y sigma a partir de precios.

Estimadores de máxima verosimilitud del Módulo 2 (§3.2), anualizados, junto con
sus errores estándar teóricos (§3.3) — que evidencian la asimetría entre un
drift prácticamente inestimable y una volatilidad bien estimada.
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

Array = npt.NDArray[np.float64]

DIAS_ANIO = 252  # días de mercado por año → Δt = 1/252


def estimar_parametros(
    precios: Array | list[float], dias_anio: int = DIAS_ANIO
) -> tuple[float, float]:
    """Estima ``(mu, sigma)`` anualizados por máxima verosimilitud.

    Toma una serie de precios (array o secuencia), calcula las rentabilidades
    logarítmicas y devuelve el drift (con corrección de Jensen) y la volatilidad
    anualizados. Acepta un ``pandas.Series`` sin conversión previa.
    """
    p = np.asarray(precios, dtype=float)
    log_ret = np.log(p[1:] / p[:-1])
    dt = 1 / dias_anio
    sigma = float(log_ret.std(ddof=1) / np.sqrt(dt))
    mu = float(log_ret.mean() / dt + 0.5 * sigma**2)
    return mu, sigma


def errores_estandar(sigma: float, n: int, T: float) -> tuple[float, float]:
    """Errores estándar teóricos de los estimadores: ``(SE_mu, SE_sigma)``.

    ``SE(mu) ≈ sigma / sqrt(T)`` depende solo del horizonte temporal ``T`` (años),
    mientras que ``SE(sigma) ≈ sigma / sqrt(2n)`` mejora con el número de
    observaciones ``n``. De ahí que muestrear más a menudo ayude a la volatilidad
    pero no al drift.
    """
    se_mu = sigma / np.sqrt(T)
    se_sigma = sigma / np.sqrt(2 * n)
    return se_mu, se_sigma
