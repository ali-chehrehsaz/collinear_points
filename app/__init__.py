"""Distinct set of lines intersecting 3 or more points in 2-dimensional space
input: a list of x, y coordinates in 2-dimensional space as an input, and
returns a distinct list of lines that intersect 3 or more points from the input set.
"""

from itertools import combinations
from typing import List, Tuple, Any
from decimal import Decimal  # To `exactly` represent Decimal numbers
from math import inf


def is_collinear(points: List[tuple]) -> bool:
    """Return True if points are collinear."""
    assert len(points) == 3
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    # Collinear points are all located on the same line. Points will be collinear if:
    return (x2 - x1) * (y0 - y1) == (x0 - x1) * (y2 - y1)


def three_collinears_lines(points: List[Tuple[Any, Any]]) -> List[Tuple[float, float]]:
    """Return all distinct and possible lines of 3 or more points.
    Lines are represented as a tuple of two with Slope-Intercept equation i.e. `y = slop * x + intercept`
    """

    # Ensure a unique collection of points.
    # Duplicates carry no meaningful information and increase complexity.
    points = list(set(points))

    point_sets = combinations(points, 3)
    lines = set()
    for point_set in point_sets:
        if is_collinear(point_set):
            x0, y0 = point_set[0]
            x1, y1 = point_set[1]

            # `Exactly` represent Decimal numbers and avoid floating-point representation error.
            # Prevent having same line (fake duplicates) in results because of the floating-point representation error.
            delta_y = Decimal(str(y1 - y0))
            delta_x = Decimal(str(x1 - x0))
            if not delta_x:
                slop = inf
                # The mathematical intercept is None but we use this notation `only when slop is infinite` to
                # distinguish between parallel lines to y-axis.
                intercept = x0  # or x1
            elif not delta_y:
                slop = 0.0
                intercept = y0  # or y1
            else:
                slop = delta_y / delta_x
                intercept = Decimal(str(y0)) - slop * Decimal(str(x0))

            line = (slop, intercept)
            lines.add(line)

    return [(float(slop), float(intercept)) for slop, intercept in lines]


if __name__ == "__main__":
    pass
