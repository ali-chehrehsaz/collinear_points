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


from typing import List, Tuple, Any
from decimal import Decimal
from math import inf
from random import choice


def get_collinears(xy_list: List[Tuple[Any, Any]] = None) -> List[Tuple[float, float]]:

    # Check input   --------------------------------------------------------------------------------
    if xy_list == []:  # Do not refactor with `if not xy_list:`
        return []

    if xy_list is None:
        raise ValueError('Expected input argument is missing.')

    if not isinstance(xy_list, list):
        raise TypeError(f'Expected input type is list. {type(xy_list)} received.')

    try:
        x, y = choice(xy_list)
        _ = x + y
    except TypeError:
        raise
    except ValueError:
        raise

    # Ensure a unique collection of points.
    # Duplicates carry no meaningful information and are dropped.
    xy_list = list(set(xy_list))

    # Core Algorithm    --------------------------------------------------------------------------------

    # To exactly represent Decimal numbers and avoid floating-point representation error.
    # Prevents having same line (fake duplicates) in results because of the floating-point representation error.
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
                lines[line] = False  # Seen once so far i.e. a line with 2 points
            else:
                lines[line] = True  # Seen more than once i.e. a line with 3 or more collinears

    return [(float(line[0]), float(line[1])) for line in lines.keys() if lines[line]]


if __name__ == '__main__':
    raise RuntimeError(f'{__name__} is not intended to run independently.')


