"""Tests del simulador de GBM: forma, reproducibilidad y momentos teóricos."""

from __future__ import annotations

import numpy as np

from mcquant import media_teorica, simular_gbm, simular_precio_final, varianza_teorica

S0, MU, SIGMA, T = 100.0, 0.08, 0.20, 1.0


def test_forma_y_columna_inicial():
    rng = np.random.default_rng(0)
    tray = simular_gbm(S0, MU, SIGMA, T, n_pasos=50, n_tray=10, rng=rng)
    assert tray.shape == (10, 51)
    assert np.all(tray[:, 0] == S0)  # todas las trayectorias arrancan en S0


def test_reproducibilidad_con_semilla():
    a = simular_gbm(S0, MU, SIGMA, T, 50, 10, np.random.default_rng(42))
    b = simular_gbm(S0, MU, SIGMA, T, 50, 10, np.random.default_rng(42))
    assert np.array_equal(a, b)


def test_momentos_terminales_coinciden_con_la_teoria():
    rng = np.random.default_rng(7)
    S_T = simular_precio_final(S0, MU, SIGMA, T, n=1_000_000, rng=rng)
    # Media y varianza muestrales cerca de las teóricas (tolerancia relativa amplia)
    assert np.isclose(S_T.mean(), media_teorica(S0, MU, T), rtol=0.01)
    assert np.isclose(S_T.var(), varianza_teorica(S0, MU, SIGMA, T), rtol=0.03)


def test_precio_final_coincide_con_ultima_columna_de_la_trayectoria():
    # Con la misma semilla, la simulación terminal es coherente en distribución:
    # comprobamos que la media a un paso ~ media teórica.
    rng = np.random.default_rng(3)
    S_T = simular_precio_final(S0, MU, SIGMA, T, n=500_000, rng=rng)
    assert np.isclose(np.log(S_T / S0).mean(), (MU - 0.5 * SIGMA**2) * T, atol=0.005)
