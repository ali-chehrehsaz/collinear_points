"""Group collinear Points and represent/return them as distinct lines in Cartesian coordinate system.
"""


from decimal import \
    Decimal  # To avoid inherent floating-point binary representation error
from math import inf  # Represent infinity for vertical lines slops
from random import choice  # Choose a random element when examining input args
from typing import Any, List, Tuple  # Optional type deceleration


def get_lines(xy_list: List[Tuple[Any, Any]] = None) -> List[Tuple[float, float]]:

    if xy_list == []:  # Do not refactor with `if not xy_list:`
        return []

    # Pass (raise) exceptions to invoking caller if input is erroneous.
    if xy_list is None:
        raise ValueError("Expected input argument is missing.")

    if not isinstance(xy_list, list):
        raise TypeError(f"Expected input type is list. {type(xy_list)} received.")

    try:
        x, y = choice(xy_list)
        _ = x + y
    except TypeError:
        raise
    except ValueError:
        raise

    # Ensure a unique collection of Cartesian points. Duplicates do not contribute to desired return.
    xy_list = list(set(xy_list))

    # Core Algorithm:
    # A O(n^2) runtime improved algorithm over the trivial O(n^3). Instead of looking for collinear points
    # in each possible combination of 3 i.e. brut-forcing, we travers points two times saving all possible lines in
    # between two points a hash-table (Python dictionary) and flag then with a value of False. If an existing line is
    # seen again that indicates there is 3 or more points in our data forming that line that make them collinear points.
    # We then flag those lines with value True. The output would be all lines in dictionary with True value.

    # To exactly represent Decimal numbers and avoid floating-point representation error.
    # Prevents including fake distinct lines in results because of the floating-point representation error.
    xy_list = [(Decimal(str(xy[0])), Decimal(str(xy[1]))) for xy in xy_list]

    lines = {}
    for i, xy in enumerate(xy_list[:-1]):
        x0, y0 = xy
        for x1, y1 in xy_list[i+1:]:

            # Special case: parallel lines with y-axis
            if not x1 - x0:
                slop = inf
                # There is no mathematical intercept for parallel lines with y-axis, but
                # We use (inf, x) to represent this special case to identify distinct vertical lines.
                intercept = x0
            # All other cases:
            else:
                slop = (y1 - y0) / (x1 - x0)
                intercept = y1 - slop * x1

            line = (slop, intercept)
            if line not in lines:
                lines[line] = False  # New line with 2 points
            else:
                lines[line] = True  # Seen more than once i.e. a line with 3 or more collinears

    # Return all lines with 3 or more collinears
    return [(float(line[0]), float(line[1])) for line in lines.keys() if lines[line]]


if __name__ == "__main__":
    raise RuntimeError(f"{__name__} is not intended to run independently.")
