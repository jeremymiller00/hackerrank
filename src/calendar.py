# for input year, find 256th dat of that year
# Two systems, start with 2020
# Add system for prior to 1918
# Add system for 1918

def dayOfProgrammer(year):
    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = "12.09." + str(year)
        else:
            day = "13.09." + str(year)
    elif year < 1918:
        if year % 4 == 0:
            day = "12.09." + str(year)
        else:
            day = "13.09." + str(year)
    else:
        day = "26.09." + str(year)
    return(day)
