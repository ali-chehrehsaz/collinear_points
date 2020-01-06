"""Group collinear 2D input (x, y) points and representing them as distinct lines.
The return value is a list of computed lines of collinear points.
Each line is represented with a tuple of two floats as (slop, y-intercept) in Cartesian coordinate system.
"""


from decimal import \
    Decimal  # To avoid inherent floating-point binary representation error.
from math import inf  # Represent infinity for vertical lines slops.
from random import choice  # Choose a random element when examining input args.
from typing import Any, List, Tuple  # Optional type deceleration.


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

    # Algorithm:
    # This is a O(n^2) runtime improved algorithm over the trivial O(n^3). The straight-forward approach is verify
    # collinear points in each possible combination of 3 points, i.e. brut-forcing, which is O(n^3).
    # Instead we travers points two times saving all possible lines in between two points in a hashtable/dictionary and
    # assign two-pointer lines them with False value. {(slop, y-intercept): False}
    # During this double travers if a line already exist it indicates there are more than collinear points in our input
    # for than line. We change the value of those lines as True to filter the False lines from return value.


    # To exactly represent Decimal numbers and avoid floating-point representation error.
    # Prevents including fake distinct lines in results because of the floating-point representation error.
    # Example:
    #       n = 0.1 + 0.1 + 0.1
    #       n = 0.30000000000000004
    #
    #       n = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
    #       float(n) = 0.3
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
                # Add line between two points with False as value indicating no 3rd or more points yet on this line.
                lines[line] = False
            else:
                # When line already exist with new points it indicate there are more than 2 points or collinear points.
                lines[line] = True

    # Return all lines with 3 or more collinears
    return [(float(line[0]), float(line[1])) for line in lines.keys() if lines[line]]


if __name__ == "__main__":
    raise RuntimeError(f"{__name__} is not intended to run independently.")
