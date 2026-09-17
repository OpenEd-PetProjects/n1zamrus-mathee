"""Utilities for solving real quadratic equations."""

from __future__ import annotations

from math import sqrt


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, ...]:
    """Return the real roots of ``a*x**2 + b*x + c = 0`` in ascending order.

    A linear equation is supported when ``a`` is zero. A constant non-zero
    equation has no roots, while ``0*x + 0 = 0`` is rejected because it has
    infinitely many solutions rather than a finite root tuple.
    """
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("the zero equation has infinitely many solutions")
            return ()
        return (-c / b,)

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ()
    if discriminant == 0:
        return (-b / (2 * a),)

    root = sqrt(discriminant)
    return tuple(sorted(((-b - root) / (2 * a), (-b + root) / (2 * a))))


def find_roots(a: float, b: float, c: float) -> tuple[float, ...] | None:
    """Return real roots using the public ``None`` result for no roots.

    A negative discriminant produces complex roots; this real-valued API
    represents that case with ``None`` instead of returning complex numbers.
    """
    roots = solve_quadratic(a, b, c)
    return roots or None
