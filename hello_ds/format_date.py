# Formatting the date
def format_date(s):
    MONTH_MAP = {
        "jan": "01",
        "feb": "02",
        "may": "05",
        "jun": "06",
        "mar": "03",
        "apr": "04",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }
    s = s.strip().lower().replace(",", "")
    m, d, y = s.split()
    if len(y) == 2:
        y = "19" + y
    if len(d) == 1:
        d = "0" + d
    return y + "-" + MONTH_MAP[m[:3]] + "-" + d


x = "may 24 1941"
y = "January 19, 1943"
z = "Feb. 9, 1941"

print(format_date(x))
print(format_date(y))
print(format_date(z))
