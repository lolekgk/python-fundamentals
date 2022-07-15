def case_check(a, b):
    """Check wheather given strings have the same case"""
    if isinstance(a, str) and isinstance(b, str):
        return a.islower() and b.islower() or a.isupper() and b.isupper()
    return -1


print(case_check("a", "b"))
print(case_check("A", "b"))
print(case_check("B", "A"))
print(case_check("a", "B"))
print(case_check(1, "b"))
