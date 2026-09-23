"""Tests de valoración de opciones: Black-Scholes, payoffs y Monte Carlo."""

from __future__ import annotations

import numpy as np
import pytest

from mcquant import black_scholes, payoff_call, payoff_put, precio_mc

# Ejemplo canónico usado en el Módulo 3
S0, K, R, SIGMA, T = 100.0, 100.0, 0.05, 0.20, 1.0


def test_black_scholes_call_atm_valor_conocido():
    # Valor de libro de la call ATM (Hull): 10.4506
    assert black_scholes(S0, K, R, SIGMA, T, "call") == pytest.approx(10.4506, abs=1e-4)


def test_black_scholes_put_atm_valor_conocido():
    assert black_scholes(S0, K, R, SIGMA, T, "put") == pytest.approx(5.5735, abs=1e-4)


def test_paridad_put_call():
    # C - P = S0 - K·e^{-rT}, identidad libre de modelo
    c = black_scholes(S0, K, R, SIGMA, T, "call")
    p = black_scholes(S0, K, R, SIGMA, T, "put")
    assert (c - p) == pytest.approx(S0 - K * np.exp(-R * T), abs=1e-10)


def test_payoff_call_valores():
    S_T = np.array([80.0, 100.0, 120.0])
    assert np.allclose(payoff_call(S_T, K), [0.0, 0.0, 20.0])


def test_payoff_put_valores():
    S_T = np.array([80.0, 100.0, 120.0])
    assert np.allclose(payoff_put(S_T, K), [20.0, 0.0, 0.0])


@pytest.mark.parametrize("tipo", ["call", "put"])
def test_monte_carlo_converge_a_black_scholes(tipo):
    # El precio MC debe caer a menos de 5 errores estándar del valor exacto.
    rng = np.random.default_rng(12345)
    mc, se = precio_mc(S0, K, R, SIGMA, T, N=500_000, rng=rng, tipo=tipo)
    bs = black_scholes(S0, K, R, SIGMA, T, tipo)
    assert abs(mc - bs) < 5 * se


def test_error_estandar_decrece_con_n():
    rng = np.random.default_rng(0)
    _, se_bajo = precio_mc(S0, K, R, SIGMA, T, N=10_000, rng=rng, tipo="call")
    _, se_alto = precio_mc(S0, K, R, SIGMA, T, N=1_000_000, rng=rng, tipo="call")
    # 100x muestras → ~10x menos error
    assert se_alto < se_bajo / 5
