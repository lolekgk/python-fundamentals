def is_rectangular_triangle(x1, x2, x3):
    """Return true if rectangular triangle can be made of given parameters."""
    x1, x2, x3 = sorted([x1, x2, x3])
    return x1**2 + x2**2 == x3**2


cond1 = is_rectangular_triangle(3, 4, 5)
cond2 = is_rectangular_triangle(4, 3, 5)
cond3 = is_rectangular_triangle(4, 3, 2)
cond4 = is_rectangular_triangle(4, 4, 4)
print(cond1, cond2, cond3, cond4)
