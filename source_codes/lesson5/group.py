import re

pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"
match = re.match(pattern, "25-03-2026")
print(re.sub(pattern, r"\3-\2-\1", "25-03-2026"))

if match:
    print("Match found!", match.group())
    day = match.group(1)
    month = match.group(2)
    year = match.group(3)

    print(day, month, year)
    print(year, month, day)