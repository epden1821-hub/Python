def is_year_leap(year: int):
    if year % 4 == 0:
        return True
    else:
        print(year % 4)
        return False


year = 2020

result = is_year_leap(year)


print(f"год {year}: {result}")
