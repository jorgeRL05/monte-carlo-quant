# src

Funciones y clases reutilizables a lo largo de los notebooks: simuladores, payoffs, métricas, utilidades de plotting.

## Filosofía

- Lo que se usa en **más de un notebook** se promueve a `src/`.
- Lo que es específico de un peldaño concreto se queda en su notebook.
- Cada módulo debe tener docstrings claras y funciones puras siempre que sea posible (sin estado oculto).

## Cómo importar desde un notebook

Desde cualquier notebook en `notebooks/`:

```python
import sys
sys.path.append("..")            # añade la raíz del proyecto al path
from src.simuladores import gbm  # ejemplo
```
