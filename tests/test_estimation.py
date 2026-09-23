"""Tests de calibración: recuperar mu y sigma de datos simulados."""

from __future__ import annotations

import numpy as np
import pytest

from mcquant import errores_estandar, estimar_parametros, simular_gbm


def test_recupera_parametros_de_datos_simulados():
    # Simulamos una trayectoria con parámetros conocidos y los reestimamos.
    mu_real, sigma_real = 0.10, 0.18
    n_anios = 30  # horizonte largo para que el drift sea estimable
    rng = np.random.default_rng(2024)
    tray = simular_gbm(100.0, mu_real, sigma_real, T=n_anios, n_pasos=n_anios * 252,
                       n_tray=1, rng=rng)
    precios = tray[0]

    mu_est, sigma_est = estimar_parametros(precios)
    n_obs = len(precios) - 1
    se_mu, se_sigma = errores_estandar(sigma_real, n_obs, T=n_anios)

    # La volatilidad se estima con gran precisión...
    assert abs(sigma_est - sigma_real) < 5 * se_sigma
    # ...y el drift, dentro de su (amplio) error estándar.
    assert abs(mu_est - mu_real) < 5 * se_mu


def test_se_mu_depende_solo_del_horizonte_no_de_la_frecuencia():
    # Mismo T, distinto n: SE(mu) apenas cambia, SE(sigma) cae con n.
    se_mu_diario, se_sigma_diario = errores_estandar(0.2, n=252 * 5, T=5)
    se_mu_mensual, se_sigma_mensual = errores_estandar(0.2, n=12 * 5, T=5)
    assert np.isclose(se_mu_diario, se_mu_mensual)
    assert se_sigma_diario < se_sigma_mensual


def test_acepta_pandas_series_si_esta_disponible():
    pd = pytest.importorskip("pandas")  # se salta si pandas no está instalado
    serie = pd.Series([100.0, 101.0, 102.5, 101.2, 103.0])
    mu, sigma = estimar_parametros(serie)
    assert np.isfinite(mu) and np.isfinite(sigma)
