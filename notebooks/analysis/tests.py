import numpy as np
from scipy.stats import stats


def vargha_delaney_a12(x, y):
    """Vargha & Delaney Â12 pour données appariées."""
    x, y = np.array(x), np.array(y)
    mask = ~np.isnan(x) & ~np.isnan(y)
    x, y = x[mask], y[mask]

    diffs = y - x
    n = len(diffs)

    wins = np.sum(diffs > 0)
    ties = np.sum(diffs == 0)

    A = (wins + 0.5 * ties) / n
    return A


def a12_label(a12):
    diff = abs(a12 - 0.5)

    if diff < 0.06:
        return "Aucun effet"

    if diff < 0.11:
        return "Effet faible"

    if diff < 0.21:
        return "Effet moyen"

    return "Effet fort"


def cohens_d(x, y):
    diff = x - y

    return diff.mean() / diff.std(ddof=1)