def func(birth_year: int, current_year: int) -> int:
    return abs(birth_year - current_year)


print(func.__annotations__)
