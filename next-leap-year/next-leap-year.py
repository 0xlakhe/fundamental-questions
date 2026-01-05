# To find next leap year
year = int(input("Year:"))
user_year = year
leap_year = False

while not leap_year:
    year += 1
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    elif year % 4 == 0:
        leap_year = True

print(f"The next leap year after {user_year} is {year}")
