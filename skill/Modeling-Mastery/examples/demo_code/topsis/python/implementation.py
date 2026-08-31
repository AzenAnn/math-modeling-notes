"""Reusable TOPSIS implementation.

Source evidence: E-TEXT-P002-TOPSIS-DEMO
The generic normalization and zero-norm handling are EXTERNAL_REFERENCE safeguards.
"""

from __future__ import annotations

import numpy as np


def topsis(matrix: np.ndarray, weights: np.ndarray, benefit: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Return closeness scores and descending ranking indices.

    Parameters
    ----------
    matrix:
        Two-dimensional alternatives-by-indicators array.
    weights:
        Nonnegative indicator weights. They are normalized internally.
    benefit:
        Boolean mask. True means larger is better; False means smaller is better.
    """
    values = np.asarray(matrix, dtype=float)
    weight_values = np.asarray(weights, dtype=float)
    if values.ndim != 2 or values.shape[0] == 0 or values.shape[1] == 0:
        raise ValueError("matrix must be a non-empty 2D array")
    if weight_values.shape != (values.shape[1],):
        raise ValueError("weights length must equal the number of indicators")
    if np.any(~np.isfinite(values)) or np.any(~np.isfinite(weight_values)):
        raise ValueError("matrix and weights must contain finite values")
    if np.any(weight_values < 0) or np.sum(weight_values) <= 0:
        raise ValueError("weights must be nonnegative and have a positive sum")
    benefit_mask = np.ones(values.shape[1], dtype=bool) if benefit is None else np.asarray(benefit, dtype=bool)
    if benefit_mask.shape != (values.shape[1],):
        raise ValueError("benefit mask length must equal the number of indicators")

    norms = np.linalg.norm(values, axis=0)
    if np.any(norms == 0):
        raise ValueError("an indicator column has zero vector norm")
    normalized = values / norms
    normalized_weights = weight_values / np.sum(weight_values)
    weighted = normalized * normalized_weights

    positive = np.where(benefit_mask, np.max(weighted, axis=0), np.min(weighted, axis=0))
    negative = np.where(benefit_mask, np.min(weighted, axis=0), np.max(weighted, axis=0))
    distance_positive = np.linalg.norm(weighted - positive, axis=1)
    distance_negative = np.linalg.norm(weighted - negative, axis=1)
    denominator = distance_positive + distance_negative
    closeness = np.divide(distance_negative, denominator, out=np.full_like(denominator, 0.5), where=denominator > 0)
    ranking = np.argsort(-closeness, kind="stable")
    return closeness, ranking
