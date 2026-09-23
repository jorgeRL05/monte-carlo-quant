"""Funciones de pago (payoffs) de opciones europeas.

Interfaz deliberadamente desacoplada del motor de valoración: un payoff solo
sabe *qué* paga la opción dado el precio, no *cómo* se descuenta ni bajo qué
modelo se simula. Esto permite reutilizar el mismo pricer con cualquier payoff
y es la base para extender a opciones exóticas en módulos posteriores.

Los pagos se devuelven **sin descontar**; el factor ``e^{-rT}`` lo aplica el
motor (:mod:`mcquant.pricing`) por separado.
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

Array = npt.NDArray[np.float64]


def payoff_call(S_T: Array, K: float) -> Array:
    """Pago de una call europea: ``max(S_T - K, 0)``."""
    return np.maximum(S_T - K, 0.0)


def payoff_put(S_T: Array, K: float) -> Array:
    """Pago de una put europea: ``max(K - S_T, 0)``."""
    return np.maximum(K - S_T, 0.0)
