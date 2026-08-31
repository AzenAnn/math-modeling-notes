from __future__ import annotations

import numpy as np
import pytest

from implementation import topsis


def test_topsis_returns_expected_best_alternative() -> None:
    matrix = np.array([[8.0, 4.0, 7.0], [6.0, 8.0, 5.0], [9.0, 3.0, 9.0]])
    scores, ranking = topsis(matrix, np.array([0.4, 0.2, 0.4]), np.array([True, False, True]))
    assert ranking[0] == 2
    assert np.all((0.0 <= scores) & (scores <= 1.0))


def test_identical_alternatives_receive_neutral_scores() -> None:
    matrix = np.array([[1.0, 2.0], [1.0, 2.0]])
    scores, ranking = topsis(matrix, np.array([1.0, 1.0]))
    np.testing.assert_allclose(scores, np.array([0.5, 0.5]))
    np.testing.assert_array_equal(ranking, np.array([0, 1]))


def test_invalid_weight_shape_is_rejected() -> None:
    with pytest.raises(ValueError):
        topsis(np.ones((2, 3)), np.ones(2))
