def is_rectangular_triangle(x1, x2, x3):
    """Return true if rectangular triangle can be made of given parameters."""
    x1, x2, x3 = sorted([x1, x2, x3])
    return x1**2 + x2**2 == x3**2
