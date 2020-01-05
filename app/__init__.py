"""Group collinear Points and represent/return them as distinct lines in Cartesian coordinate system.
A line in Cartesian coordinate system can be represented as y = slop * x + intercept

Notes:
    There could more than 3 collinear points which will be represented with a distinct line together.
    Lines represented as a tuple of 2 elements (slop, intercept)
    Input:  list of (x, y)
    Output: list of (slop, intercept)

    We chose `immutable` tuple data structure for (x, y) as this data is not to change.
    We use functional programming per project requirement. (Rather alternative class-based solution)

    Per project requirement the function must be imported to other parts of a main app.
    It purposely raise a RuntimeError if run independently.

    To avoid inherent floating point error we use built-in Decimal module.
    Example:
        number = 0.1 + 0.1 + 0.1
        number = 0.30000000000000004

        number = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
        float(Decimal('0.3') = 0.3



Please return your project in a zipped folder that contains your
- code,
- test cases, and a
- ReadMe.

Success Criteria:We will be assessing your
- project's architecture,
- execution, and
- coding style.
-  extensible, well organized, and
- well documented project.

Please take time to code to your highest professional standard.

Constraints:Please refrain from using external libraries.
Built-in Python libraries are fine.
"""

from itertools import combinations
from typing import List, Tuple, Any
from decimal import Decimal  # To `exactly` represent Decimal numbers
from math import inf


def is_collinear(points: List[Tuple[Any, Any]]) -> bool:
    """Return True if points are collinear."""
    assert len(points) == 3
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    # Collinear points are all located on the same line. Points will be collinear if:
    return (x2 - x1) * (y0 - y1) == (x0 - x1) * (y2 - y1)


def get_lines(points: List[Tuple[Any, Any]]) -> List[Tuple[float, float]]:
    """Return all distinct and possible lines of 3 or more points.
    Lines are represented as a tuple of two with Slope-Intercept equation i.e. `y = slop * x + intercept`
    :raise: TypeError if input is not a list
    :raise:
    """

    if not isinstance(points, list):
        raise TypeError(f"Expected input was list but {type(points)} received.")

    # Core algorithm handles this edge case but for clarity explicitly implemented here.
    if len(points) < 3:
        return []  # No lines with not enough number of collinears.

    # Ensure a unique collection of points.
    # Duplicates carry no meaningful information and increase complexity.
    points = list(set(points))

    # itertools.combinations returns a generator therefore during the main algorithm for loop we only travers possible
    # combinations `once` giving us O( (n * n-1 * n-2)/6 ) i.e. O(n^3) far from ideally a linear runtime complexity.
    # The worst-case space complexity returning the results is O( n/3 )
    all_three_pnts_combinations = combinations(points, 3)
    lines_set = set()
    for cmb in all_three_pnts_combinations:
        if is_collinear(cmb):
            x0, y0 = cmb[0]
            x1, y1 = cmb[1]

            # `Exactly` represent Decimal numbers and avoid floating-point representation error.
            # Prevent having same line (fake duplicates) in results because of the floating-point representation error.
            delta_y = Decimal(str(y1 - y0))
            delta_x = Decimal(str(x1 - x0))
            if not delta_x:
                slop = inf
                # The mathematical intercept is None but we use this notation `only when slop is infinite`
                # i.e x = Constant to distinguish between parallel lines to y-axis.
                intercept = x0  # or x1
            elif not delta_y:
                slop = 0.0
                intercept = y0  # or y1
            else:
                slop = delta_y / delta_x
                intercept = Decimal(str(y0)) - slop * Decimal(str(x0))

            curr_line = (float(slop), float(intercept))
            lines_set.add(curr_line)

    return list(lines_set)


if __name__ == "__main__":
    raise RuntimeError(f'{__name__} is not intended to run independently.')
